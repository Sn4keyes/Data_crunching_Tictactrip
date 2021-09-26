from controller import search_id_city
from controller import *
import math

def distance(origin_city, destination_city, data_cities):
    print("distance")
    id_o_city = search_id_city(origin_city, data_cities)
    id_d_city = search_id_city(destination_city, data_cities)
    print(id_o_city, id_d_city)
    # lat1, lon1 = origin
    # lat2, lon2 = destination
    # radius = 6371 # km

    # dlat = math.radians(lat2-lat1)
    # dlon = math.radians(lon2-lon1)
    # a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
    #     * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    # d = radius * c

    # return d