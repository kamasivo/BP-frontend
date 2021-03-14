from flask import Flask, jsonify
from flask_cors import CORS
import json
import threading
import time

from database.select import select
from database.connect import connect
from scan import scan
from pingScan import pingScan


app = Flask(__name__)
# CORS(app)
CORS(app, resources=r'/api/*')


# scan network ang get all IP adresses on this network every 30 seconds, update MITM
def startScanNetwork():
    def run_job():
        while True:
            print("start scan")
            targets = pingScan()
            print(targets)   # tu mam vzdy pole IP adries...treba ich dostat do spoofera a vediet ich dynamicky menit
            time.sleep(10)
    thread = threading.Thread(target=run_job())
    thread.start()  
@app.before_first_request(startScanNetwork())

@app.route("/api/greeting")
def greeting():
    return {"greeting": "Hello from Flask!"}


@app.route("/api/devices")
def devices():
    select_data = select('devices')
    return jsonify(data = select_data)

@app.route("/api/refresh_devices")
def refresh_devices():
    scan()
    select_data = select('devices')
    return jsonify(data = select_data)

@app.route("/api/devices_ports")
def devices_ports():
    select_data = select('ports')
    return jsonify(data = select_data)