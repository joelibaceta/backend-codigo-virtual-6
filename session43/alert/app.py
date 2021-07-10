
from flask import Flask
from flask import request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

import os
import httpx
from flask import Response

app = Flask(__name__)
connection_string = "mysql+pymysql://developer:rootcodigo@db:3306/alerts"
app.config["SQLALCHEMY_DATABASE_URI"] = connection_string
db = SQLAlchemy(app)

load_dotenv()

@app.route('/')
def hello():
    return "hello"

@app.route('/alert', methods=['POST'])
async def create_alert():
    from alert.models.alert import Alert    
    data = request.json
    auth_url = f'{os.getenv("AUTH_SERVICES_URL")}/validate'
    headers = {
        "authorization": request.headers["authorization"]
    }
    
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(auth_url)
 
    if response.status_code == 200:
        payload = response.json()
        uid = payload["uid"]
    else:
        return Response(status=401)

    alert = Alert(**data)
    alert.uid = uid
    db.session.add(alert)
    db.session.commit()

    return "DONE"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)