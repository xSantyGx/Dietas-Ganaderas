from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

ani_nut = Blueprint('animal_nutriente', __name__)

@ani_nut.route('/animal_nutriente')
def animal_nutriente():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Animal_Nutriente')
    data= cur.fetchall()
    return render_template('animal_nutriente.html', animal_nutrientes = data)

@ani_nut.route('/animal_nutrienteInsertar')
def insertAnimal_Nutriente():
    cur = mysql.connection.cursor()
    cur.execute('SELECT cod_animal FROM Animal')
    dataC = [codigo[0] for codigo in cur.fetchall()]
    cur.execute('SELECT nombre_nutriente FROM Nutriente')
    dataN = [nombre[0] for nombre in cur.fetchall()]
    return render_template('animal_nutrienteInsertar.html', codigos_animales = dataC, nombres_nutrientes = dataN)

@ani_nut.route('/animal_nutrienteAgregar', methods=['POST'])
def addAnimal_Nutriente():
    if request.method == 'POST':
       cod_animal = request.form['cod_animal']
       nombre_nutriente = request.form['nombre_nutriente']
       cantidad_necesitada = request.form['cantidad_necesitada']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Animal_Nutriente (cod_animal, nombre_nutriente, cantidad_necesitada) VALUES (%s, %s, %s)',
                   (cod_animal, nombre_nutriente, cantidad_necesitada))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('animal_nutriente.animal_nutriente'))
       

@ani_nut.route('/animal_nutrienteEditar/<cod_animal>/<nombre_nutriente>')
def getAnimal_nutriente(cod_animal, nombre_nutriente):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Animal_Nutriente WHERE cod_animal = %s AND nombre_nutriente = %s', (str(cod_animal), str(nombre_nutriente)))
    data= cur.fetchall()
    return render_template('animal_nutrienteEditar.html', animal_nutriente = data[0])

@ani_nut.route('/animal_nutrienteActualizar/<cod_animal_bus>', methods = ['POST'])
def updateAnimal_nutriente(cod_animal_bus):
     if request.method == 'POST':
        cod_animal = request.form['cod_animal']
        nombre_nutriente = request.form['nombre_nutriente']
        cantidad_necesitada = request.form['cantidad_necesitada']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Animal_Nutriente
            SET cod_animal = %s,
                nombre_nutriente = %s,
                cantidad_necesitada = %s
            WHERE cod_animal = %s
            AND nombre_nutriente = %s
        """, (cod_animal, nombre_nutriente, cantidad_necesitada, cod_animal_bus, nombre_nutriente))
        mysql.connection.commit()
        flash('Animal_Nutriente actualizado exitosamente')
        return redirect(url_for('animal_nutriente.animal_nutriente'))

@ani_nut.route('/animal_nutrienteEliminar/<string:cod_animal>/<string:nombre_nutriente>')
def deleteAnimal_nutriente(cod_animal, nombre_nutriente):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Animal_Nutriente WHERE cod_animal = %s AND nombre_nutriente = %s', (str(cod_animal), str(nombre_nutriente)))
    mysql.connection.commit()
    flash('Animal_Nutriente eliminado exitosamente')
    return redirect(url_for('animal_nutriente.animal_nutriente'))