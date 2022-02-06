import json
import math
import numpy as np
import geopy.distance
from datetime import datetime

def findFlight(myLocation, azimuth, pitch):

    earth_radius = geopy.distance.EARTH_RADIUS * 10**3
    earth_circum = earth_radius * 2 * math.pi
    azimuth += math.pi / 2

    def translate(lat, lon, height):
        try:
            d = height / math.sin(pitch)
            a = math.cos(azimuth) * d
            b = math.sin(azimuth) * d
            offset = lambda x: math.degrees(math.asin((x/2)/earth_radius)*2)
            lat -= offset(b)
            lon += offset(a)
            return (lat, lon)
        except Exception as e:
            return (lat, lon)

    def distance(flight):
        location = translate(flight[6], flight[5], flight[13])
        return geopy.distance.distance(location, myLocation)
        
    with open('data.json') as json_file:
        data = json.load(json_file)
        flights = np.array(data["states"])
        distances = list(map(distance, flights))
        return flights[np.argmin(distances)][1]
