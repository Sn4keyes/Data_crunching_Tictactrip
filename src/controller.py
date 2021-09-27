from distance import *
from price import *
from duration import *
from company import *
from category import *
from numpy import tile
import pandas
import pandas as pd

def manage(origin_city, destination_city, data_cities):
    data_ticket = pandas.read_csv('../data/ticket_data.csv')
    data_providers = pandas.read_csv('../data/providers.csv')
    print("The Itinerary", origin_city, "-", destination_city)
    gap = distance(origin_city, destination_city, data_cities)
    print("\t📏 Distance : ", round(gap), "Km")
    price(origin_city, destination_city, data_ticket, data_cities)
    duration(data_ticket, data_cities, origin_city, destination_city)
    company(origin_city, destination_city, data_ticket, data_providers, data_cities)
    # category(origin_city, destination_city, data_ticket, data_providers)
