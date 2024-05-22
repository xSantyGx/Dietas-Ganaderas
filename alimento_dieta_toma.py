from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

ali_die_tom = Blueprint('alimento_dieta_toma', __name__)

@ali_die_tom.route('/alimento_dieta_toma')
def alimento_dieta_toma():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Alimento_Dieta_Toma')
    data= cur.fetchall()
    return render_template('alimento_dieta_toma.html', alimento_dieta_tomas = data)

@ali_die_tom.route('/alimento_dieta_tomaInsertar')
def insertAlimento_dieta_toma():
    cur = mysql.connection.cursor()
    cur.execute('SELECT cod_dieta FROM Dieta')
    dataCD = [codDie[0] for codDie in cur.fetchall()]
    cur.execute('SELECT nombre_alimento FROM Alimento')
    dataNA = [ali[0] for ali in cur.fetchall()]
    cur.execute('SELECT cod_toma FROM Toma')
    dataCT = [ali[0] for ali in cur.fetchall()]
    return render_template('alimento_dieta_tomaInsertar.html', codigos_dietas = dataCD, nombres_alimentos = dataNA, codigos_tomas = dataCT)

@ali_die_tom.route('/alimento_dieta_tomaAgregar', methods=['POST'])
def addAlimento_dieta_toma():
    if request.method == 'POST':
       cod_dieta = request.form['cod_dieta']
       nombre_alimento = request.form['nombre_alimento']
       cod_toma = request.form['cod_toma']
       cantidad_toma = request.form['cantidad_toma']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Alimento_Dieta_Toma (cod_dieta, nombre_alimento, cod_toma, cantidad_toma) VALUES (%s, %s, %s, %s)',
                   (cod_dieta, nombre_alimento, cod_toma, cantidad_toma))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('alimento_dieta_toma.alimento_dieta_toma'))
       

@ali_die_tom.route('/alimento_dieta_tomaEditar/<cod_dieta>/<nombre_alimento>/<cod_toma>')
def getNutriente_alimento(cod_dieta, nombre_alimento, cod_toma):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Alimento_Dieta_Toma WHERE cod_dieta = %s AND nombre_alimento = %s AND cod_toma = %s', (str(cod_dieta),str(nombre_alimento),str(cod_toma),))
    data= cur.fetchall()
    
    return render_template('alimento_dieta_tomaEditar.html', alimento_dieta_toma = data[0])

@ali_die_tom.route('/alimento_dieta_tomaActualizar/<cod_dieta_bus>', methods = ['POST'])
def updateNutriente_alimento(cod_dieta_bus): 
     if request.method == 'POST':
        cod_dieta = request.form['cod_dieta']
        nombre_alimento = request.form['nombre_alimento']
        cod_toma = request.form['cod_toma']
        cantidad_toma = request.form['cantidad_toma']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Alimento_Dieta_Toma
            SET cod_dieta = %s,
                nombre_alimento = %s,
                cod_toma = %s,
                cantidad_toma = %s
            WHERE cod_dieta = %s
            AND nombre_alimento = %s
            AND cod_toma = %s
        """, (cod_dieta, nombre_alimento, cod_toma, cantidad_toma, cod_dieta_bus, nombre_alimento, cod_toma))
        mysql.connection.commit()
        flash('Alimento Dieta Toma actualizado exitosamente')
        return redirect(url_for('alimento_dieta_toma.alimento_dieta_toma'))

@ali_die_tom.route('/alimento_dieta_tomaEliminar/<string:cod_dieta>/<string:nombre_alimento>/<string:cod_toma>')
def deleteAlimento_dieta_toma(cod_dieta, nombre_alimento, cod_toma):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Alimento_Dieta_Toma WHERE cod_dieta = %s AND nombre_alimento = %s AND cod_toma = %s', (str(cod_dieta), str(nombre_alimento),str(cod_toma),))
    mysql.connection.commit()
    flash('Alimento Dieta Toma  eliminado exitosamente')
    return redirect(url_for('alimento_dieta_toma.alimento_dieta_toma'))