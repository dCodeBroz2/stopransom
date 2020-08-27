import time
from flask import Flask
import sys
# Lets make path
import ransomWare


app = Flask(__name__)

@app.route('/time')
def get_current_time():
  return {'time': time.time()}

@app.route('/getupdate')
def updateJsonFile():
  ranW = ransomWare.ransomWare()
  ranW.updateJson()
  return {'UPDATED TO': ranW.lastUpdateDate}