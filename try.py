import random
import datetime
from datetime import timedelta, datetime
import time
days_selected = True

class Reservations:
    def __init__(self, room_type, start_date, end_date, alr_reserved_on):
        self.room_type = room_type
        self.start_date = start_date
        self.end_date = end_date
        self.alr_reserved_on = alr_reserved_on

    def reserve_dates(start_date, end_date):
        pass

arrival_date = input("arrival")
departure_date = input("departure")    

room_count = 101
room_list = []

Alr_reserved = False
min_date_evil = datetime.today() + timedelta(days=1)
max_date_evil = datetime()
allowed_range = (max_date_evil - min_date_evil).days

for random_reservation_amount in range(random.randint(3, 8)):
    room_list.append(room_count)
    rand_type = random.choice(["Single","Double"])
    rand_start = random.randint(0, allowed_range)
    rand_end = random.randint(1,14)
    rand_arr_date = min_date_evil + timedelta(days=rand_start)
    rand_dep_date = rand_arr_date + timedelta(days=rand_end)
    arr_timestamp = datetime.strptime(str(rand_arr_date), "%d/%m/%Y")
    dep_timestamp = datetime.striptime(str(rand_dep_date), "%d/%m/%Y")
    if days_selected:
        user_arrival_stamp = datetime.striptime(arrival_date, "%d/%m/%Y")
        user_departure_stamp = datetime.striptime(departure_date, "%d/%m/%Y")
        if arr_timestamp <user_arrival_stamp> dep_timestamp or arr_timestamp <user_departure_stamp> dep_timestamp:
            Alr_reserved = True 
    room_list[i] = Reservations(rand_type,arr_timestamp,dep_timestamp,Alr_reserved)
    print(room_list[i].room_type)
    print(room_list[i].reservations)