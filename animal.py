from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

ani = Blueprint('animal', __name__)

@ani.route('/animal')
def animal():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Animal')
    data= cur.fetchall()
    return render_template('animal.html', animales = data)

@ani.route('/animalInsertar')
def insertAnimal():
    return render_template('animalInsertar.html')

@ani.route('/animalAgregar', methods=['POST'])
def addAnimal():
    if request.method == 'POST':
       cod_animal = request.form['cod_animal']
       tipo_animal = request.form['tipo_animal']
       peso = request.form['peso']
       ano_nacimiento = request.form['ano_nacimiento']
       utilidad_animal = request.form['utilidad_animal']
       produccion_animal = request.form['produccion_animal']
       od_animal = request.form['od_animal']
       
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO Animal (cod_animal, tipo_animal, peso, ano_nacimiento, utilidad_animal, ' +
                   'produccion_animal, od_animal) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                   (cod_animal, tipo_animal, peso, ano_nacimiento, utilidad_animal, produccion_animal, od_animal))
       mysql.connection.commit()
       flash('Agregado exitosamente')
       
       return redirect(url_for('animal.animal'))
       

@ani.route('/animalEditar/<cod_animal>')
def getAnimal(cod_animal):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Animal WHERE cod_animal = %s', (str(cod_animal),))
    data= cur.fetchall()
    return render_template('animalEditar.html', animal = data[0])

@ani.route('/animalActualizar/<cod_animal_bus>', methods = ['POST'])
def updateAnimal(cod_animal_bus):
     if request.method == 'POST':
        cod_animal = request.form['cod_animal']
        tipo_animal = request.form['tipo_animal']
        peso = request.form['peso']
        ano_nacimiento = request.form['ano_nacimiento']
        utilidad_animal = request.form['utilidad_animal']
        produccion_animal = request.form['produccion_animal']
        od_animal = request.form['od_animal']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Animal
            SET cod_animal = %s,
                tipo_animal = %s,
                peso = %s,
                ano_nacimiento = %s,
                utilidad_animal = %s,
                produccion_animal = %s,
                od_animal = %s
            WHERE cod_animal = %s
        """, (cod_animal, tipo_animal, peso, ano_nacimiento, utilidad_animal, produccion_animal, 
              od_animal, cod_animal_bus))
        mysql.connection.commit()
        flash('Animal actualizado exitosamente')
        return redirect(url_for('animal.animal'))

@ani.route('/animalEliminar/<string:cod_animal>')
def deleteAnimal(cod_animal):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM Animal WHERE cod_animal = %s', (str(cod_animal),))
    mysql.connection.commit()
    flash('Animal eliminado exitosamente')
    return redirect(url_for('animal.animal'))