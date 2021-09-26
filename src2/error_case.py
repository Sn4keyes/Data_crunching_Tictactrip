from main import *
from os import terminal_size
from controller import *
import getopt, sys
import pandas

def check_cities(origin_city, destination_city):
    data_cities = pandas.read_csv('../data/cities.csv')
    is_o_city = False
    is_d_city = False

    for i in range(len(data_cities["unique_name"])):
        if data_cities["unique_name"][i] == origin_city:
            is_o_city = True
        if data_cities["unique_name"][i] == destination_city:
            is_d_city = True
    if is_o_city == True and is_d_city == True:
        print("cool")
        manage(origin_city, destination_city, data_cities)
    elif is_o_city != True and is_d_city == True:
        print("Désolé mais la 1ère ville n'existe pas. Recommencez svp !!")
        exit(0)
    elif is_o_city == True and is_d_city != True:
        print("Désolé mais la 2ème ville n'existe pas. Recommencez svp !!")
        exit(0)
    elif is_o_city != True and is_d_city != True:
        print("Désolé mais aucune des villes n'existent. Recommencez svp !!")
        exit(0)

def check_args(argv):
    argumentList = sys.argv[1:]
    options = "h"
    long_options = ["Help"]

    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--Help"):
                print("How to use this data_crunching script:")
                print("Show help:\n \t./main.py -h")
                print("Usage:\n \t./main.py [Origin_city] [Destination_city]")
    except getopt.error as err:
        print(str(err))
    if len(sys.argv) != 3:
        exit(0)
    check_cities(sys.argv[1], sys.argv[2])