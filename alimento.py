from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

ali = Blueprint('alimento', __name__)

@ali.route('/alimento')
def alimento():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Alimento')
    data= cur.fetchall()
    return render_template('alimento.html', alimentos = data)


@ali.route('/alimentoInsertar')
def insertAlimento():
    return render_template('alimentoInsertar.html')

@ali.route('/alimentoAgregar', methods=['POST'])
def addAlimento():
    if request.method == 'POST':
       nombre_alimento = request.form['nombre_alimento']
       tipo_alimento = request.form['tipo_alimento']
       magnitud_alimento = request.form['magnitud_alimento']
       coste_alimento = request.form['coste_alimento']
       od_alimento = request.form['od_alimento']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Alimento (nombre_alimento, tipo_alimento, magnitud_alimento, coste_alimento, od_alimento) VALUES (%s, %s, %s, %s, %s)',
                   (nombre_alimento, tipo_alimento, magnitud_alimento, coste_alimento, od_alimento))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('alimento.alimento'))
       

@ali.route('/alimentoEditar/<nombre_alimento>')
def getAlimento(nombre_alimento):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Alimento WHERE nombre_alimento = %s', (str(nombre_alimento),))
    data= cur.fetchall()
    return render_template('alimentoEditar.html', alimento = data[0])

@ali.route('/alimentoActualizar/<nombre_alimento_bus>', methods = ['POST'])
def updateAlimento(nombre_alimento_bus):
     if request.method == 'POST':
        nombre_alimento = request.form['nombre_alimento']
        tipo_alimento = request.form['tipo_alimento']
        magnitud_alimento = request.form['magnitud_alimento']
        coste_alimento = request.form['coste_alimento']
        od_alimento = request.form['od_alimento']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Alimento
            SET nombre_alimento = %s,
                tipo_alimento = %s,
                magnitud_alimento = %s,
                coste_alimento = %s,
                od_alimento = %s
            WHERE nombre_alimento = %s
        """, (nombre_alimento, tipo_alimento, magnitud_alimento, coste_alimento, od_alimento, nombre_alimento_bus))
        mysql.connection.commit()
        flash('Alimento actualizado exitosamente')
        return redirect(url_for('alimento.alimento'))

@ali.route('/alimentoEliminar/<string:nombre_alimento>')
def deleteAlimento(nombre_alimento):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Alimento WHERE nombre_alimento = %s', (str(nombre_alimento),))
    mysql.connection.commit()
    flash('Alimento eliminado exitosamente')
    return redirect(url_for('alimento.alimento'))