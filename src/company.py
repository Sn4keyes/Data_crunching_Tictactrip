from typing import List
from distance import *
import pandas as pd
import re

def find_companies(companies_clean, data_providers):
    # for y in range(len(data_providers["id"])):
    #     data_companies.append(re.findall(r'\d+' , str(data_providers["id"][y])))
        for i in range(len(companies_clean)):
            for y in range(len(data_providers["id"])):
                if companies_clean[i][0] == data_providers["id"][y]:
                    print("Trouvé == ", type(companies_clean[i]), type(data_providers["name"][y]))


def cleaning_companies(companies):
    companies_clean = []
    for i in range(len(companies)):
        if i >= len(companies):
            companies_clean.append(companies[i])
        elif i + 1 < len(companies) and companies[i + 1] == companies[i]:
            i += 1
        else:
            companies_clean.append(companies[i])
    return companies_clean

def sorting_companies(companies):
    companies_sort = []
    for i in range(len(companies)):
            if companies[i]:
                companies_sort.append(companies[i])
    companies_sort.sort()
    return companies_sort

    print("Companies are sort ==", companies)

def company(origin_city, destination_city, data_ticket, data_providers, data_cities):
    companies = []
    id_o_city = search_id_city(origin_city, data_cities)
    id_d_city = search_id_city(destination_city, data_cities)
    for i in range(len(data_ticket["company"])):
        if data_ticket["o_city"][i] == id_o_city and data_ticket["d_city"][i] == id_d_city:
            companies.append(re.findall(r'\d+' , str(data_ticket["company"][i])))
            companies.append(re.findall(r'\d+' , str(data_ticket["other_companies"][i])))
    companies_sort = sorting_companies(companies)
    companies_clean = cleaning_companies(companies_sort)
    companies_find = find_companies(companies_clean, data_providers)
    print("\t📮 Company :", companies_clean)