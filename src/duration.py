from distance import *

def check_diff_time(d_time, a_time):
    d_hrs, d_mins = d_time.split(':')
    a_hrs, a_mins = a_time.split(':')
    d_hrs = int(d_hrs)
    d_mins = int(d_mins)
    a_hrs = int(a_hrs)
    a_mins = int(a_mins)
    d_total = d_hrs * 60 + d_mins
    a_total = a_hrs * 60 + a_mins
    if a_total > d_total:
        total = a_total - d_total
    else:
        total = d_total - a_total
        total = 1440 - total
    return total

def duration(data_ticket, data_cities, origin_city, destination_city):
    y = 0
    min = 0
    moy = 0
    max = 0
    d_time = 0
    a_time = 0
    id_o_city = search_id_city(origin_city, data_cities)
    id_d_city = search_id_city(destination_city, data_cities)
    for i in range(len(data_ticket)):
        if data_ticket["o_city"][i] == id_o_city and data_ticket["d_city"][i] == id_d_city:
            d_time = data_ticket["departure_ts"][i][11:16]
            a_time = data_ticket["arrival_ts"][i][11:16]
            diff = check_diff_time(d_time, a_time)
            if diff < min or min == 0 :
                min = diff
            if diff > max or max == 0:
                max = diff
            moy += diff
            y += 1
    moy = moy / y
    print("\t⏱  Duration : From", min, "To", max, "minutes")
    print("\t\t      Average of", moy, "minutes")