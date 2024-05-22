from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

die_ani_fec = Blueprint('dieta_animal_fechaInicio', __name__)

@die_ani_fec.route('/dieta_animal_fechaInicio')
def dieta_animal_fechaInicio():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Dieta_Animal_FechaInicio')
    data= cur.fetchall()
    return render_template('dieta_animal_fechaInicio.html', dieta_animal_fechaInicios = data)

@die_ani_fec.route('/dieta_animal_fechaInicioInsertar')
def insertdieta_animal_fechaInicio():
    cur = mysql.connection.cursor()
    cur.execute('SELECT cod_animal FROM Animal')
    dataCA = [ali[0] for ali in cur.fetchall()]
    cur.execute('SELECT cod_dieta FROM Dieta')
    dataCD = [codDie[0] for codDie in cur.fetchall()]
    return render_template('dieta_animal_fechaInicioInsertar.html', codigos_animales = dataCA, codigos_dietas = dataCD)

@die_ani_fec.route('/dieta_animal_fechaInicioAgregar', methods=['POST'])
def adddieta_animal_fechaInicio():
    if request.method == 'POST':
       cod_animal = request.form['cod_animal']
       fecha_inicio = request.form['fecha_inicio']
       cod_dieta = request.form['cod_dieta']
       od_resultado  = request.form['od_resultado']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Dieta_Animal_FechaInicio (cod_animal, fecha_inicio, cod_dieta, od_resultado) VALUES (%s, %s, %s, %s)',
                   (cod_animal, fecha_inicio, cod_dieta, od_resultado))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('dieta_animal_fechaInicio.dieta_animal_fechaInicio'))
       

@die_ani_fec.route('/dieta_animal_fechaInicioEditar/<cod_animal>/<fecha_inicio>')
def getdieta_animal_fechaInicio(cod_animal, fecha_inicio):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Dieta_Animal_FechaInicio WHERE cod_animal = %s AND fecha_inicio = %s', (str(cod_animal),str(fecha_inicio),))
    data= cur.fetchall()
    cur.execute('SELECT cod_dieta FROM Dieta')
    dataCD = [codDie[0] for codDie in cur.fetchall()]
    
    return render_template('dieta_animal_fechaInicioEditar.html', dieta_animal_fechaInicio = data[0], codigos_dietas = dataCD)

@die_ani_fec.route('/dieta_animal_fechaInicioActualizar/<cod_animal_bus>', methods = ['POST'])
def updatedieta_animal_fechaInicio(cod_animal_bus): 
     if request.method == 'POST':
        cod_animal = request.form['cod_animal']
        fecha_inicio = request.form['fecha_inicio']
        cod_dieta = request.form['cod_dieta']
        od_resultado  = request.form['od_resultado']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Dieta_Animal_FechaInicio
            SET cod_animal = %s,
                fecha_inicio = %s,
                cod_dieta = %s,
                od_resultado = %s
            WHERE cod_animal = %s
            AND fecha_inicio = %s
        """, (cod_animal, fecha_inicio, cod_dieta, od_resultado, cod_animal_bus, fecha_inicio))
        mysql.connection.commit()
        flash('Dieta Animal Fecha Inicio actualizado exitosamente')
        return redirect(url_for('dieta_animal_fechaInicio.dieta_animal_fechaInicio'))

@die_ani_fec.route('/dieta_animal_fechaInicioEliminar/<string:cod_animal>/<string:fecha_inicio>')
def deletedieta_animal_fechaInicio(cod_animal, fecha_inicio):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Dieta_Animal_FechaInicio WHERE cod_animal = %s AND fecha_inicio = %s', (str(cod_animal), str(fecha_inicio),))
    mysql.connection.commit()
    flash('Dieta Animal Fecha Inicio eliminado exitosamente')
    return redirect(url_for('dieta_animal_fechaInicio.dieta_animal_fechaInicio'))