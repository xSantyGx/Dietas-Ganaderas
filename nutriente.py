from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

nut = Blueprint('nutriente', __name__)

@nut.route('/nutriente')
def nutriente():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Nutriente')
    data= cur.fetchall()
    return render_template('nutriente.html', nutrientes = data)

@nut.route('/nutrienteInsertar')
def insertNutriente():
    return render_template('nutrienteInsertar.html')

@nut.route('/nutrienteAgregar', methods=['POST'])
def addNutriente():
    if request.method == 'POST':
       nombre_nutriente = request.form['nombre_nutriente']
       magnitud_nutriente = request.form['magnitud_nutriente']
       estado = request.form['estado']
       od_nutriente = request.form['od_nutriente']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Nutriente (nombre_nutriente, magnitud_nutriente, estado, od_nutriente) VALUES (%s, %s, %s, %s)',
                   (nombre_nutriente, magnitud_nutriente, estado, od_nutriente))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('nutriente.nutriente'))
       

@nut.route('/nutrienteEditar/<nombre_nutriente>')
def getNutriente(nombre_nutriente):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Nutriente WHERE nombre_nutriente = %s', (str(nombre_nutriente),))
    data= cur.fetchall()
    return render_template('nutrienteEditar.html', nutriente = data[0])

@nut.route('/nutrienteActualizar/<nombre_nutriente_bus>', methods = ['POST'])
def updateNutriente(nombre_nutriente_bus):
     if request.method == 'POST':
        nombre_nutriente = request.form['nombre_nutriente']
        magnitud_nutriente = request.form['magnitud_nutriente']
        estado = request.form['estado']
        od_nutriente = request.form['od_nutriente']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Nutriente
            SET nombre_nutriente = %s,
                magnitud_nutriente = %s,
                estado = %s,
                od_nutriente = %s
            WHERE nombre_nutriente = %s
        """, (nombre_nutriente, magnitud_nutriente, estado, od_nutriente, nombre_nutriente_bus))
        mysql.connection.commit()
        flash('Nutriente actualizado exitosamente')
        return redirect(url_for('nutriente.nutriente'))

@nut.route('/nutrienteEliminar/<string:nombre_nutriente>')
def deleteNutriente(nombre_nutriente):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Nutriente WHERE nombre_nutriente = %s', (str(nombre_nutriente),))
    mysql.connection.commit()
    flash('Nutriente eliminado exitosamente')
    return redirect(url_for('nutriente.nutriente'))