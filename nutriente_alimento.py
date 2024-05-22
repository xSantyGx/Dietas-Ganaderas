from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

nut_ali = Blueprint('nutriente_alimento', __name__)

@nut_ali.route('/nutriente_alimento')
def nutriente_alimento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Nutriente_Alimento')
    data= cur.fetchall()
    return render_template('nutriente_alimento.html', nutriente_alimentos = data)

@nut_ali.route('/nutriente_alimentoInsertar')
def insertNutriente_alimento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre_nutriente FROM Nutriente')
    dataN = [nutri[0] for nutri in cur.fetchall()]
    cur.execute('SELECT nombre_alimento FROM Alimento')
    dataA = [ali[0] for ali in cur.fetchall()]
    return render_template('nutriente_alimentoInsertar.html', nombres_nutrientes = dataN, nombres_alimentos = dataA)

@nut_ali.route('/nutriente_alimentoAgregar', methods=['POST'])
def addNutriente_alimento():
    if request.method == 'POST':
       nombre_nutriente = request.form['nombre_nutriente']
       nombre_alimento = request.form['nombre_alimento']
       cantidad_contenida = request.form['cantidad_contenida']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Nutriente_Alimento (nombre_nutriente, nombre_alimento, cantidad_contenida) VALUES (%s, %s, %s)',
                   (nombre_nutriente, nombre_alimento, cantidad_contenida))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('nutriente_alimento.nutriente_alimento'))
       

@nut_ali.route('/nutriente_alimentoEditar/<nombre_nutriente>/<nombre_alimento>')
def getNutriente_alimento(nombre_nutriente, nombre_alimento):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Nutriente_Alimento WHERE nombre_nutriente = %s AND nombre_alimento = %s', (str(nombre_nutriente),str(nombre_alimento),))
    data= cur.fetchall()
    
    return render_template('nutriente_alimentoEditar.html', nutriente_alimento = data[0])

@nut_ali.route('/nutriente_alimentoActualizar/<nombre_nutriente_bus>', methods = ['POST'])
def updateNutriente_alimento(nombre_nutriente_bus): 
     if request.method == 'POST':
        nombre_nutriente = request.form['nombre_nutriente']
        nombre_alimento = request.form['nombre_alimento']
        cantidad_contenida = request.form['cantidad_contenida']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Nutriente_Alimento
            SET nombre_nutriente = %s,
                nombre_alimento = %s,
                cantidad_contenida = %s
            WHERE nombre_nutriente = %s
            AND nombre_alimento = %s
        """, (nombre_nutriente, nombre_alimento, cantidad_contenida, nombre_nutriente_bus, nombre_alimento))
        mysql.connection.commit()
        flash('Nutriente Alimento actualizado exitosamente')
        return redirect(url_for('nutriente_alimento.nutriente_alimento'))

@nut_ali.route('/nutriente_alimentoEliminar/<string:nombre_nutriente>/<string:nombre_alimento>')
def deleteNutriente_alimento(nombre_nutriente, nombre_alimento):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Nutriente_Alimento WHERE nombre_nutriente = %s AND nombre_alimento = %s', (str(nombre_nutriente), str(nombre_alimento),))
    mysql.connection.commit()
    flash('Nutriente Alimento eliminado exitosamente')
    return redirect(url_for('nutriente_alimento.nutriente_alimento'))