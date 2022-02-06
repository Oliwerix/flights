import json
import math
import numpy as np
import geopy.distance
from datetime import datetime
from gmplot import gmplot
#lat = 42.12591
#lon = 14.55570

myLocation = (46.12595787972877, 14.5555221083642)

azimuth = math.pi/2
pitch = math.pi / 32 

succ = 0
fail = 0
gmap = gmplot.GoogleMapPlotter(46.126032240711595, 14.555414824791287, 8)
earth_radius = geopy.distance.EARTH_RADIUS * 10**3
earth_circum = earth_radius * 2 * math.pi
azimuth += math.pi / 2

def translate(lat, lon, height):
    global fail, succ
    try:
        d = height / math.sin(pitch)
        a = math.cos(azimuth) * d
        b = math.sin(azimuth) * d
        offset = lambda x: math.degrees(math.asin((x/2)/earth_radius)*2)
        lat -= offset(b)
        lon += offset(a)
        succ +=1 
        global gmap
        if not None in [lat, lon]:
            gmap.marker(lat, lon, 'cornflowerblue')
        return (lat, lon)
    except Exception as e:
        #print('problem', e)
        fail +=1 
        return (lat, lon)

def distance(flight):
   # if flight[13] is None:
   #     print(flight)
    location = translate(flight[6], flight[5], flight[13])
    #print(flight, location)
    return geopy.distance.distance(location, myLocation)
    
with open('data.json') as json_file:
    data = json.load(json_file)
    print(datetime.fromtimestamp(data["time"]).strftime('%Y-%m-%d %H:%M:%S'))
    flights = np.array(data["states"])
#    data1 = np.array([])
    #distance = lambda flight: geopy.distance.distance((flight[6], flight[5]), myLocation)
#    distances = np.apply_along_axis(distance, axis=1, arr=flights)
#    print(flights[np.argmin(distances)][1])
##    print(data)
    distances = list(map(distance, flights))
    print(sorted(distances)[:10])
    print(f"succ: {succ}, fail: {fail}")
    print(flights[np.argmin(distances)][1])
    
    print(10000 / math.sin(pitch))
    gmap.draw("big_map.html")
   # print(flights[np.argmin(distances)][1])
##    print(data)
#    for flight in flight:
#
#        #print(location)
#
#        distance = geopy.distance.distance(location, myLocation)
#        if distance < 50:
#            print(flight[1], distance)
