from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

rep = Blueprint('reportes', __name__)

@rep.route('/reporte_1')
def reporte1():
    cur = mysql.connection.cursor()
    cur.execute('SELECT a.cod_animal, a.tipo_animal, an.cantidad_necesitada FROM Animal a INNER JOIN Animal_Nutriente an ON a.cod_animal = an.cod_animal WHERE an.nombre_nutriente = "Riboflavina"')
    data= cur.fetchall()
    return render_template('reporte_1.html', animales = data)

@rep.route('/reporte_2')
def reporte2():
   cur = mysql.connection.cursor()
   cur.execute('SELECT cod_animal FROM Dieta_Animal_FechaInicio WHERE cod_dieta = 342567 AND fecha_inicio = STR_TO_DATE("01/01/1999", "DD/MM/YYYY") AND cod_animal IN (SELECT cod_animal FROM Animal WHERE tipo_animal = "Vaca" AND peso > 550)')
   data= cur.fetchall()
   return render_template('reporte_2.html', animales = data)

@rep.route('/reporte_3')
def reporte3():
    cur = mysql.connection.cursor()
    cur.execute('SELECT coste_alimento, nombre_alimento FROM Alimento WHERE coste_alimento = (SELECT MIN(coste_alimento) FROM Alimento WHERE nombre_alimento IN (SELECT a.nombre_alimento FROM Nutriente_Alimento a INNER JOIN Animal_Nutriente b ON a.nombre_nutriente = b.nombre_nutriente WHERE a.nombre_nutriente = "Vitamina A" AND b.cod_animal = "L-03-D8"))')
    data= cur.fetchall()
    return render_template('reporte_3.html', animales = data)

@rep.route('/reporte_4')
def reporte4():
    cur = mysql.connection.cursor()
    cur.execute('SELECT a.cod_animal, a.tipo_animal, an.cantidad_necesitada FROM Animal a INNER JOIN Animal_Nutriente an ON a.cod_animal = an.cod_animal WHERE an.nombre_nutriente = "Riboflavina"')
    data= cur.fetchall()
    return render_template('reporte_4.html', animales = data)

@rep.route('/reporte_5')
def reporte5():
    cur = mysql.connection.cursor()
    cur.execute('SELECT b.cod_animal, b.cod_dieta, A.tipo_animal FROM Dieta_Animal_FechaInicio b INNER JOIN Animal A ON b.cod_animal = A.cod_animal WHERE b.fecha_inicio = STR_TO_DATE("01/01/1999", "DD/MM/YYYY")')
    data= cur.fetchall()
    return render_template('reporte_5.html', animales = data)

@rep.route('/reporte_6')
def reporte6():
    cur = mysql.connection.cursor()
    cur.execute('SELECT a.cod_animal, a.tipo_animal, an.cantidad_necesitada FROM Animal a INNER JOIN Animal_Nutriente an ON a.cod_animal = an.cod_animal WHERE an.nombre_nutriente = "Riboflavina"')
    data= cur.fetchall()
    return render_template('reporte_6.html', animales = data)

@rep.route('/reporte_7')
def reporte7():
    cur = mysql.connection.cursor()
    cur.execute('SELECT a.cod_animal, a.tipo_animal, an.cantidad_necesitada FROM Animal a INNER JOIN Animal_Nutriente an ON a.cod_animal = an.cod_animal WHERE an.nombre_nutriente = "Riboflavina"')
    data= cur.fetchall()
    return render_template('reporte_7.html', animales = data)

@rep.route('/reporte_8')
def reporte8():
    cur = mysql.connection.cursor()
    cur.execute('SELECT a.cod_animal, a.tipo_animal, an.cantidad_necesitada FROM Animal a INNER JOIN Animal_Nutriente an ON a.cod_animal = an.cod_animal WHERE an.nombre_nutriente = "Riboflavina"')
    data= cur.fetchall()
    return render_template('reporte_8.html', animales = data)

