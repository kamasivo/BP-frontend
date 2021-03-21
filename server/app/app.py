from flask import Flask, jsonify
from flask_cors import CORS
import json
import threading
import time
import pandas as panda

from spoofer import *
from sniffer import sniffer
from database.select import *
from database.connect import connect
from scan import scan


def onStartup():
    print('MyFlaskApp is starting up!')

    snifferThread = threading.Thread(target=sniffer, name="sniffer_function", args=())
    snifferThread.deamon = True
    snifferThread.start()

    spooferThread = threading.Thread(target=spoofer, name="spoofer_function", args=())
    spooferThread.daemon = True
    spooferThread.start()

class MyFlaskApp(Flask):
  def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
      with self.app_context():
        onStartup()
    super(MyFlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)


app = MyFlaskApp(__name__)
CORS(app, resources=r'/api/*')
app.run()


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

@app.route("/api/packets")
def packets():
    with open('networkdata/packets.json', 'r') as f:
        data = json.load(f)
    return jsonify(data = data)

@app.route("/api/ipAddresses")
def ipAdresses():
    with open('networkdata/ipAdresses.json', 'r') as f:
        data = json.load(f)
    return jsonify(data = data)
