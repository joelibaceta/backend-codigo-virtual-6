import json
from os import stat
import requests
import csv
from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    """Retornar informe de salud de la aplicacion"""
    pass

@app.route('/check_health')
def check_health():
    status_log = open("status_log.csv", "a") 
    with open('config.json') as config_file:
        config = json.load(config_file)
    services = config["services"]
    print(services) 

    for key in services:
        response = requests.get(services[key])
        status = response.status_code
        elapsed = response.elapsed.microseconds
        log_item = {
            "id": key,
            "path": services[key],
            "status": (status == 200),
            "datetime": datetime.now(),
            "elapsed": elapsed
        }
        writer = csv.writer(status_log)
        writer.writerow(log_item.values())
    status_log.close() 
    return "done"

@app.route('/ping')
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3500", debug=True)