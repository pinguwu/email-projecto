from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template
from flask_mail import Mail, Message

import csv
import pprint
import os

app = Flask(__name__)

app.debug = True #Change this to False for production
app.secret_key = os.environ['SECRET_KEY'] #used to sign session cookies


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)

@app.route('/')
def Page1():
    return render_template('Page1.html')

@app.route('/Page2')
def Page2():
    return render_template('Page2.html')


@app.route('/next1',methods=["POST","GET"])
def rendernext1():
    #messg = request.form['data']
    return render_template('Page2.html')

@app.route('/next2',methods=["POST","GET"])
def rendernext2():

    messg = "'" + str(request.form['data']) + "'"
    msg = Message('User Dats', sender = '', recipients = [''])
    msg.attach("data.csv", "data/csv" , messg )

    mail.send(msg)
    return render_template('Page2.html' , sent="yes")


@app.route('/home',methods=["POST","GET"])
def renderhome():
    return render_template('Page1.html')

if __name__ == '__main__':
    os.system("echo json(array) > file")
    app.run()
