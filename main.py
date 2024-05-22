from flask import Flask, render_template, redirect, url_for
from config import Config
from app import appD
from animal import ani
from nutriente import nut
from animal_nutriente import ani_nut
from alimento import ali
from nutriente_alimento import nut_ali
from toma import tom
from dieta import die
from alimento_dieta_toma import ali_die_tom
from dieta_animal_fechaInicio import die_ani_fec
from reportes import rep
from baseDatos import mysql

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(appD)
app.register_blueprint(ani)
app.register_blueprint(nut)
app.register_blueprint(ani_nut)
app.register_blueprint(ali)
app.register_blueprint(nut_ali)
app.register_blueprint(tom)
app.register_blueprint(die)
app.register_blueprint(ali_die_tom)
app.register_blueprint(die_ani_fec)
app.register_blueprint(rep)
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


if __name__ == '__main__':
    app.run(port=8088, debug=True)

