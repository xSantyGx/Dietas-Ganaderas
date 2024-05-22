from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

tom = Blueprint('toma', __name__)

@tom.route('/toma')
def toma():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Toma')
    data= cur.fetchall()
    return render_template('toma.html', tomas = data)

@tom.route('/tomaInsertar')
def insertToma():
    cur = mysql.connection.cursor()
    return render_template('tomaInsertar.html')

@tom.route('/tomaAgregar', methods=['POST'])
def addToma():
    if request.method == 'POST':
       cod_toma = request.form['cod_toma']
       nombre_toma = request.form['nombre_toma']
       hora_inicio = request.form['hora_inicio']
       hora_fin = request.form['hora_fin']
       od_toma = request.form['od_toma']
       
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Toma (cod_toma, nombre_toma, hora_inicio, hora_fin, od_toma) VALUES (%s, %s, %s, %s, %s)',
                   (cod_toma, nombre_toma, hora_inicio, hora_fin, od_toma))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('toma.toma'))
       

@tom.route('/tomaEditar/<cod_toma>')
def getToma(cod_toma):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Toma WHERE cod_toma = %s', (str(cod_toma),))
    data= cur.fetchall()
    return render_template('tomaEditar.html', toma = data[0])

@tom.route('/tomaActualizar/<cod_toma_bus>', methods = ['POST'])
def updateAnimal(cod_toma_bus):
     if request.method == 'POST':
        cod_toma = request.form['cod_toma']
        nombre_toma = request.form['nombre_toma']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        od_toma = request.form['od_toma']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Toma
            SET cod_toma = %s,
                nombre_toma = %s,
                hora_inicio = %s,
                hora_fin = %s,
                od_toma = %s
            WHERE cod_toma = %s
        """, (cod_toma, nombre_toma, hora_inicio, hora_fin, od_toma, cod_toma_bus))
        mysql.connection.commit()
        flash('Toma actualizada exitosamente')
        return redirect(url_for('toma.toma'))

@tom.route('/tomaEliminar/<string:cod_toma>')
def deleteAnimal(cod_toma):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Toma WHERE cod_toma = %s', (str(cod_toma),))
    mysql.connection.commit()
    flash('Toma eliminada exitosamente')
    return redirect(url_for('toma.toma'))