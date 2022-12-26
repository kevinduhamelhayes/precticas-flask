from flask import Flask, request, url_for, redirect, abort, render_template
app = Flask(__name__)

import mysql_connector

midb =_mysql_.connector.connect(
    host="localhost",
    user="chanchitofeliz",
    password="holamundo",
    database="pueba"
)

cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'hola mundo'
# get, post, put, patch, delete
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala():
    if request.method == 'GET':
        return 'EL ID DEL POST ES:' + post_id
    else:
        return 'este es otro metodo y no GET'

@app.route('/lele',methods=['POST', 'GET'])
def lele ():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    #abort(404)
    #return redirect(url_for('lala', post_id=2))

    #print(request.form)
    #print(request.form['llave1'])
    #print(request.form['llave2'])
    #return {
    #    "username": 'Chanchito Feliz',
    #    "email": 'chanchitofeliz@usuario.com'
    #}
    return render_template('lele.html', usuarios=usuarios)
@app.route('/home', methods=['GET'])
def home ():
    return render_template('home.html', mensaje='Hola Mundo')