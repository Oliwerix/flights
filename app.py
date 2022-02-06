from flask import Flask
from flask import request
from math import radians
import FlightLocator
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    lat = float(request.values["lat"])
    lon = float(request.values["lon"])
    azi = radians(float(request.values["azi"]))
    com = radians(float(request.values["pit"]))
    print((lat,lon), azi, com)
    return FlightLocator.findFlight((lat, lon), azi, pit)
