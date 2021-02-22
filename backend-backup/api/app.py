from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
# CORS(app)
CORS(app, resources=r'/api/*')

@app.route("/api/greeting")
def greeting():
    return {"greeting": "Hello from Flask!"}


@app.route("/api/devices")
def devices():
    devicesItem = { "ipAddress":"192.169.10.1", "os":"Linux", "name":"-", "vendor":"Linux", "osFamily":"Linux", "osGen":"-", "numOfVulns":"0", "openPorts":"0"}
    devicesItem2 = { "ipAddress":"192.169.10.1", "os":"Linux", "name":"-", "vendor":"Linux", "osFamily":"Linux", "osGen":"-", "numOfVulns":"0", "openPorts":"0"}
    deviceList = [(devicesItem), (devicesItem2)]
    return jsonify(data = deviceList)