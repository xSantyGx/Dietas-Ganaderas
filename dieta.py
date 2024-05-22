from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

die = Blueprint('dieta', __name__)

@die.route('/dieta')
def dieta():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Dieta')
    data= cur.fetchall()
    return render_template('dieta.html', dietas = data)

@die.route('/dietaInsertar')
def insertDieta():
    cur = mysql.connection.cursor()
    return render_template('dietaInsertar.html')

@die.route('/dietaAgregar', methods=['POST'])
def addDieta():
    if request.method == 'POST':
       cod_dieta = request.form['cod_dieta']
       finalidad = request.form['finalidad']
       od_dieta = request.form['od_dieta']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Dieta (cod_dieta, finalidad, od_dieta) VALUES (%s, %s, %s)',
                   (cod_dieta, finalidad, od_dieta))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('dieta.dieta'))
       

@die.route('/dietaEditar/<cod_dieta>')
def getDieta(cod_dieta):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Dieta WHERE cod_dieta = %s', (str(cod_dieta),))
    data= cur.fetchall()
    return render_template('dietaEditar.html', dieta = data[0])

@die.route('/dietaActualizar/<cod_dieta_bus>', methods = ['POST'])
def updateDieta(cod_dieta_bus):
     if request.method == 'POST':
        cod_dieta = request.form['cod_dieta']
        finalidad = request.form['finalidad']
        od_dieta = request.form['od_dieta']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Dieta
            SET cod_dieta = %s,
                finalidad = %s,
                od_dieta = %s
            WHERE cod_dieta = %s
        """, (cod_dieta, finalidad, od_dieta, cod_dieta_bus))
        mysql.connection.commit()
        flash('Dieta actualizada exitosamente')
        return redirect(url_for('dieta.dieta'))

@die.route('/dietaEliminar/<string:cod_dieta>')
def deleteDieta(cod_dieta):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Dieta WHERE cod_dieta = %s', (str(cod_dieta),))
    mysql.connection.commit()
    flash('Dieta eliminada exitosamente')
    return redirect(url_for('dieta.dieta'))