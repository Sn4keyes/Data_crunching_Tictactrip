from distance import *

def price(origin_city, destination_city, data_ticket, data_cities):
    y = 0
    min = 0
    moy = 0
    max = 0
    id_o_city = search_id_city(origin_city, data_cities)
    id_d_city = search_id_city(destination_city, data_cities)

    for i in range(len(data_ticket["price_in_cents"])):
        if data_ticket["o_city"][i] == id_o_city and data_ticket["d_city"][i] == id_d_city:
            if data_ticket["price_in_cents"][i] < min or min == 0 :
                min = data_ticket["price_in_cents"][i]
            if data_ticket["price_in_cents"][i] > max or max == 0:
                max = data_ticket["price_in_cents"][i]
            moy += data_ticket["price_in_cents"][i]
            y += 1
    if y == 0:
        print("sorry there is no route between ", origin_city, " and ", destination_city)
        exit(0)
    moy = moy / y
    min /= 100
    max /= 100
    moy /= 100
    print("\t💵 Prices : From", min, "To", max, "€")
    print("\t\t    Average of", moy, "€")