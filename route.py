import openrouteservice
import os
import pygeoj
import datetime

# API Key
key = os.environ.get('ORS_API_KEY')
client = openrouteservice.Client(key=key)


def route(start, end):
    start_point = openrouteservice.geocode.pelias_search(client, start, country= "GB")
    end_point = openrouteservice.geocode.pelias_search(client, end, country= "GB")
    start_coords = coord_parse(start_point)
    end_coords = coord_parse(end_point)
    distance, duration = dist_dur(start_coords, end_coords)
    duration = str(datetime.timedelta(seconds=duration))
    return distance, duration

def dist_dur(start_point, end_point):
    dd = start_point + end_point
    output = openrouteservice.distance_matrix.distance_matrix(client, dd, "driving-car",
                                                            metrics=["distance", "duration"],
                                                            units="km")
    dur = output['durations'][0][1]
    dis = output['distances'][0][1]
    return dis, dur

def coord_parse(point):
    x = []
    testfile = pygeoj.load(data=dict(point))
    for feature in testfile:
        p = feature.geometry.coordinates
        x.append(p)
        break
    return x
