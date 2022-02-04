import json
import numpy as np
import geopy.distance
from datetime import datetime
lat = 42.12591
lon = 14.55570

myLocation = (46.12595787972877, 14.5555221083642)

azimuth = 120
pitch = 60



with open('data.json') as json_file:
    
    data = json.load(json_file)
    print(datetime.fromtimestamp(data["time"]).strftime('%Y-%m-%d %H:%M:%S'))
    flights = np.array(data["states"])
    data1 = np.array([])
    distance = lambda flight: geopy.distance.distance((flight[6], flight[5]), myLocation)
    distances = np.apply_along_axis(distance, axis=1, arr=flights)
#    distances = np.fromiter((distance(flight) for flight in flights), flights.dtype)
    print(flights[np.argmin(distances)][1])
##    print(data)
#    for flight in flights:
#        location = (flight[6], flight[5])
#        #print(location)
#
#        distance = geopy.distance.distance(location, myLocation)
#        if distance < 50:
#            print(flight[1], distance)
