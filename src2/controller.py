from distance import distance
from distance import *
from numpy import tile
import pandas as pd

def search_id_city(city, data_cities):
    id_city = 0

    for i in range(len(data_cities["unique_name"])):
        if data_cities["unique_name"][i] == city:
            id_city = data_cities["id"][i]
            return id_city
    return id_city

def manage(origin_city, destination_city, data_cities):
    print("The Itinerary", origin_city, "-", destination_city)
    distance(origin_city, destination_city, data_cities)