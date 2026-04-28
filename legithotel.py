# from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry
from datetime import date, datetime, timedelta
import time
import random


class Reservations:
    def __init__(self, room_num, room_type, start_date, end_date, alr_reserved_on):
        self.room_type = room_type
        self.start_date = start_date
        self.end_date = end_date
        self.alr_reserved_on = alr_reserved_on
        self.room_num = room_num

    def create_random_dates(self, room_type, rand_arr_timestamp, rand_dep_timestamp, room_num, room_list):
        self.rand_dates_created = True
        self.room_list = []
        min_date_evil = date.today() + timedelta(days=1)
        max_date_evil = date(2027, 12, 31)
        allowed_range = (self.max_date_evil - min_date_evil).days
        for random_reservation_amount in range(random.randint(3, 8)):
            self.room_count += 1
            self.room_list.append(room_count)
            self.rand_type = random.choice(["Single","Double"])
            self.rand_start = random.randint(0, allowed_range)
            self.rand_end = random.randint(1,14)
            self.rand_arr_date = min_date_evil + timedelta(days=rand_start)
            self.rand_dep_date = rand_arr_date + timedelta(days=rand_end)
            self.rand_arr_date = rand_arr_date.strftime("%d/%m/%Y")
            self.rand_dep_date = rand_dep_date.strftime("%d/%m/%Y")
            self.rand_arr_timestamp = date.strptime(str(rand_arr_date), "%d/%m/%Y")
            self.rand_dep_timestamp = date.strptime(str(rand_dep_date), "%d/%m/%Y")
            reserve_random_dates(rand_arr_timestamp, rand_dep_timestap, start_date, end_date, room_num, room_type)

    def reserve_random_dates(self, rand_arr, rand_dep, start_date, end_date, room_num, room_type, rand_dates_created):
        if rand_dates_created:
            self.Alr_reserved = False

            self.start_date = start_date.strftime("%d/%m/%Y")
            self.end_date = end_date.strftime("%d/%m/%Y")

            if days_selected:
                self.user_arrival_stamp = date.strptime(str(start_date), "%d/%m/%Y")
                self.user_departure_stamp = date.strptime(str(end_date), "%d/%m/%Y")
                self.stamp_check_1 = user_arrival_stamp <= rand_arr < rand_dep <= user_departure_stamp
                self.stamp_check_2 = rand_arr <= user_arrival_stamp < user_departure_stamp <= rand_dep
                self.stamp_check_3 = user_arrival_stamp <= rand_arr < user_departure_stamp <= rand_dep
                self.stamp_check_4 = rand_arr <= user_arrival_stamp < rand_dep <= user_departure_stamp
                if stamp_check_1 or stamp_check_2 or stamp_check_3 or stamp_check_4:
                    self.Alr_reserved = True 

                else:
                    self.Alr_reserved = False
                self.room_list[self.random_reservation_amount] = Reservations(self.room_num, self.rand_type,self.arr_timestamp,self.dep_timestamp,self.Alr_reserved)
                print(f"{arr_timestamp}")
        else:
            self.create_random_dates("placeholder", "placeholder", "placeholder", "placeholder", "placeholder")


Room_list = Reservations(100, "Placeholder", date(2026,12,10), date(2026,12,15), False)
print(Room_list.reserve_random_dates( "placeholder", "placeholder", "placeholder", "placeholder", "placeholder", "placeholder", False))
print(Room_list.alr_reserved_on)

