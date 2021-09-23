from csv import writer
from csv import reader
import pandas


data_cities = pandas.read_csv('../data/cities.csv')
data_providers = pandas.read_csv('../data/providers.csv')
data_stations = pandas.read_csv('../data/stations.csv')
data_ticket = pandas.read_csv('../data/ticket_data.csv')

print("##########DATA CITIES##########")
print(data_cities)
print("##########DATA PROVIDERS##########")
print(data_providers)
print("##########DATA STATIONS##########")
print(data_stations)
print("##########DATA TICKET##########")
print(data_ticket)