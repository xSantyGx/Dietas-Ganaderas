from flask import Blueprint, render_template, request, redirect, url_for, flash
from baseDatos import mysql

appD = Blueprint('app', __name__)

@appD.route('/')
def Index():
    return render_template('index.html')
