from error_case import *
import sys
from os import error
import pandas
from csv import writer
from csv import reader
import matplotlib.pyplot as plt

def open_data_file():
    data_cities = pandas.read_csv('../data/cities.csv')
    data_providers = pandas.read_csv('../data/providers.csv')
    data_stations = pandas.read_csv('../data/stations.csv')
    data_ticket = pandas.read_csv('../data/ticket_data.csv')

    ##print("##########DATA CITIES##########")
    ##print(data_cities)
    ##print("##########DATA PROVIDERS##########")
    ##print(data_providers)
    ##print("##########DATA STATIONS##########")
    ##print(data_stations)
    ##print("##########DATA TICKET##########")
    ##print(data_ticket)

def main(argv):
    check_args(sys.argv)

if __name__ == "__main__":
    main(sys.argv)

