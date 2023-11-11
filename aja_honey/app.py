import sqlite3
import requests
from flask import Flask, render_template, request, redirect, session, flash 
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#conexion con la base de datos
db = sqlite3.connect("PCB.db")

#cursor para consultas
cursor = db.cursor()

@app.route("/")
def index():
    print(session)
    
    return render_template("index.html")

@app.route("/comprar")
def comprar():
    a= "i fell special"
    return render_template("comprar.html", a=a)

@app.route("/cartelera")
def cartelera():
    eventos= "cine", "conciertos", "deportes"
    # a = cursor.execute("SELECT * FROM eventos")
    # conn.commit()
    # conn.close()

    return render_template("cartelera.html", eventos=eventos)

@app.route("/login")
def login():

    return render_template("login.html")
    
@app.route("/register")
def register():
    
    return render_template("register.html")