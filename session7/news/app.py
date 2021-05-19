from flask import Flask
from flask import render_template
from flask import request
import json

app=Flask(__name__)

@app.route('/')
def index():
    token = request.args.get("token")
    raw = open('data/new.json', 'r')
    data = json.load(raw)
    ispremium = token != None
    return render_template('lista.html', news=data, ispremium=ispremium)