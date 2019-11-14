from flask import Flask, render_template, jsonify, url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired

from Negocio.bebidas import NegocioBebida
from Datos.bebida import Bebida
from flask_bootstrap import Bootstrap
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField, \
    BooleanField, SubmitField, IntegerField, FormField, validators,StringField,Label,Field


from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import os
import urllib.parse, hashlib
from nav import nava
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION


app = Flask(__name__)
Bootstrap(app)
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)

class VinoForm(Form):

    """def __init__(self,titulo):

        self.name = titulo"""

    txtNombre = Label(1,'Vino')

def get_datos(bebidas):
    imagenes = []
    for bebida in bebidas:
        imagenes.append(str(bebida.imagen).split("'")[1])

    datos = [bebidas,imagenes]
    return datos


@app.route('/')
def default():

    return redirect(url_for("get_bebidas",tipo_bebida="vino"))

@app.route('/<string:tipo_bebida>',methods=["GET","POST"])
def get_bebidas(tipo_bebida):
    negocio_bebida = NegocioBebida()
    bebidas = negocio_bebida.get_all_tipo_bebida(tipo_bebida)

    datos = get_datos(bebidas)
    rango = range(len(datos[0]))

    return render_template("index.html",datos=datos,rango=rango)

@app.route('/compra',methods=["GET","POST"])
def compra():
    if request.method == "POST":
        return "Hola has comprado "+request.form['cantidad']+" de "+request.form['id']
    return "Chau"

@app.route('/admin')
def admin():

    return render_template("admin.html")

@app.route('/admin/<string:tipo_bebida>')
def admin_bebidas(tipo_bebida):
    negocio_bebida = NegocioBebida()
    vinos = negocio_bebida.get_all_tipo_bebida(tipo_bebida)

    datos = get_datos(vinos)
    rango = range(len(datos[0]))

    return render_template("listadoDeProductosLocales.html",datos=datos,rango=rango)

@app.route('/insert/default')
def insert_default():
    negocio_vino = NegocioBebida()
    negocio_vino.alta(Vino(titulo_vino='Malbec',cantidad=15,precio=75))

    return 'Proceso completado.'

@app.route('/get/item')
def get_item():
    negocio_vino = NegocioVino()
    vino = negocio_vino.get(7)
    lista = str(vino.imagen).split("'")
    return render_template('imagen.html',imagen=lista[1])

@app.route('/get_all_vinos')
def get_all_vinos():
    vinos = []
    negocio_vino = NegocioVino()
    listaVinos = negocio_vino.get_all()
    diccionario = {}

    for i in listaVinos:
        diccionario["id"] = i.codigo_vino
        diccionario["titulo"] = i.titulo_vino
        diccionario["cantidad"] = i.cantidad
        diccionario["precio"] = i.precio
        vinos.append(diccionario)
        diccionario = {}

    #return jsonify({"vinos":vinos})

    return vinos

    #print(vinos)

    #return render_template('vista.html',vinos=vinos)

if __name__ == "__main__":
    app.run(port=5313)