from flask import Flask, jsonify
from flask_cors import CORS
import json
from database.select import select
from database.connect import connect
from scan import scan

app = Flask(__name__)
# CORS(app)
CORS(app, resources=r'/api/*')

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
