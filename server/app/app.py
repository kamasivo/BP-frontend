from flask import Flask, jsonify
from flask_cors import CORS
import json
import threading
import time

from database.select import select
from database.connect import connect
from scan import scan
from pingScan import pingScan

from spoofer import *
from sniffer import sniffer


def onStartup():
    print('MyFlaskApp is starting up!')
    snifferThread = threading.Thread(target=sniffer, name="sniffer_function", args=())
    snifferThread.deamon = True
    snifferThread.start()

    spooferThread = threading.Thread(target=spoofer, name="spoofer_function", args=())
    spooferThread.daemon = True
    spooferThread.start()
    # thread = threading.Thread(target=run_job())
    # thread.start()  

class MyFlaskApp(Flask):
  def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
      with self.app_context():
        onStartup()
    super(MyFlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)


app = MyFlaskApp(__name__)
CORS(app, resources=r'/api/*')
app.run()


# scan network ang get all IP adresses on this network every 30 seconds, update MITM
def startScanNetwork():
    print("start app")
    # def run_job():
    snifferThread = threading.Thread(target=sniffer, name="sniffer_function", args=())
    snifferThread.deamon = True
    snifferThread.start()
        # while True:
            # spooferThread = threading.Thread(target=spoofer, name="spoofer_function", args=())
            # spooferThread.daemon = True
            # spooferThread.start()

            # targets = pingScan()
            # print(targets)   # tu mam vzdy pole IP adries...treba ich dostat do spoofera a vediet ich dynamicky menit
            # time.sleep(10)
            # spooferThread.stop()
    # thread = threading.Thread(target=run_job())
    # thread.start()  


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
