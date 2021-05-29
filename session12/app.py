from user import User
from flask import Flask
from flask import request
import db

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/users', methods=['POST'])
def create_user():
    session = db.Session()
    # Crear un usuario
    user = request.json
    # crear nueva instancia de modelo User
    new_user = User()
    new_user.nombre = user["nombre"]
    new_user.apellido = user["apellido"]
    new_user.dni = user["dni"]
    new_user.telefono = user["telefono"]
    new_user.correo = user["correo"]

    session.add(new_user)
    session.commit()

    return "OK", 201


