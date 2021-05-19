from flask import Flask
from flask import request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def index():
    noticias = [
        "Debate del domingo 23 de mayo", 
        "¿Cómo saber si tengo multas electorales?",
        "El revelador informe que el Pentágono alista sobre todo lo que sabe EE.UU. de los ovnis"
    ]
    name = request.args.get('name')
    return render_template("index.html", title="Titulo", name=name, news=noticias)