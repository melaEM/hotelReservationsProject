import random
from datetime import timedelta, datetime, date
import time
from tkinter import *
from tkcalendar import DateEntry
days_selected = True

class Reservations:
    def __init__(self, room_type, start_date, end_date, alr_reserved_on):
        self.room_type = room_type
        self.start_date = start_date
        self.end_date = end_date
        self.alr_reserved_on = alr_reserved_on

    def reserve_dates(start_date, end_date):
        pass
   

room_count = 101
room_list = []

Alr_reserved = False
min_date_evil = date.today() + timedelta(days=1)
max_date_evil = date(2027, 12, 31)


allowed_range = (max_date_evil - min_date_evil).days

arrival_date = date(2027, 2,1)
arrival_date = arrival_date.strftime("%d/%m/%Y")
departure_date = date(2027, 5, 20)
departure_date = departure_date.strftime("%d/%m/%Y")

for random_reservation_amount in range(random.randint(3, 8)):
    room_list.append(room_count)
    rand_type = random.choice(["Single","Double"])
    rand_start = random.randint(0, allowed_range)
    print(rand_start)
    rand_end = random.randint(1,14)
    print(rand_end)
    rand_arr_date = min_date_evil + timedelta(days=rand_start)
    rand_dep_date = rand_arr_date + timedelta(days=rand_end)
    rand_arr_date = rand_arr_date.strftime("%d/%m/%Y")
    rand_dep_date = rand_dep_date.strftime("%d/%m/%Y")
    print(f"rand_arr: {rand_arr_date}")
    print(f"rand_dep: {rand_dep_date}")
    arr_timestamp = date.strptime(str(rand_arr_date), "%d/%m/%Y")
    dep_timestamp = date.strptime(str(rand_dep_date), "%d/%m/%Y")
    if days_selected:
        user_arrival_stamp = date.strptime(str(arrival_date), "%d/%m/%Y")
        user_departure_stamp = date.strptime(str(departure_date), "%d/%m/%Y")
        # print(f"arr_date < dep_stamp: {user_arrival_stamp < dep_timestamp} \, arr_date > arr_stamp: {arr_timestamp < user_arrival_stamp}")
        # print(f"dep_date < dep_stamp: {user_arrival_stamp < dep_timestamp} \, dep_date > arr_stamp: {arr_timestamp < user_arrival_stamp}")
        # if arr_timestamp <= user_arrival_stamp <= dep_timestamp or arr_timestamp >= user_departure_stamp >= dep_timestamp:
        stamp_check_1 = user_arrival_stamp <= arr_timestamp < dep_timestamp <= user_departure_stamp
        stamp_check_2 = arr_timestamp <= user_arrival_stamp < user_departure_stamp <= dep_timestamp
        stamp_check_3 = user_arrival_stamp <= arr_timestamp < user_departure_stamp <= dep_timestamp
        stamp_check_4 = arr_timestamp <= user_arrival_stamp < dep_timestamp <= user_departure_stamp
        if stamp_check_1 or stamp_check_2 or stamp_check_3 or stamp_check_4:
            Alr_reserved = True 
            # print(stamp_check_1)
            # print(stamp_check_2)
            # print(stamp_check_3)
            # print(stamp_check_4)
        else:
            Alr_reserved = False
    room_list[random_reservation_amount] = Reservations(rand_type,arr_timestamp,dep_timestamp,Alr_reserved)
    print(room_list[random_reservation_amount].room_type)
    print(room_list[random_reservation_amount].alr_reserved_on)
