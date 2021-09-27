from controller import *
import math

def search_id_city(city, data_cities):
    id_city = 0

    for i in range(len(data_cities["unique_name"])):
        if data_cities["unique_name"][i] == city:
            id_city = data_cities["id"][i]
            return id_city
    return id_city

def distance(origin_city, destination_city, data_cities):
    for i in range(len(data_cities["unique_name"])):
        if data_cities["unique_name"][i] == origin_city:
            lat1 = data_cities["latitude"][i]
            lon1 = data_cities["longitude"][i]
        if data_cities["unique_name"][i] == destination_city:
            lat2 = data_cities["latitude"][i]
            lon2 = data_cities["longitude"][i]
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d