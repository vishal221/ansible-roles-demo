from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect, url_for
import sys



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/date', methods=['GET', 'POST'])
def date():
    formData = request.form.get('date')
    formData = str(formData)
    birthDate = requests.post('http </>' + formData)

    prime = requests.post('http </>' + formData)
  
    return render_template('convertPrime.html', formData=formData, birthDate=</>, prime=</>)

