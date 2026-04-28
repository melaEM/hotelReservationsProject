import random
from datetime import timedelta, datetime, date
import time
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry


class Reservations:
    def __init__(self, room_num, room_type, start_date, end_date, alr_reserved_on):
        self.room_type = room_type
        self.start_date = start_date
        self.end_date = end_date
        self.alr_reserved_on = alr_reserved_on
        self.room_num = room_num
    
    # def pack_rooms():
    #     pass


# def reserve_dates(start_date_stamp, end_date_stamp, alr_reserved):
#     pass


min_date = date.today() + timedelta (days=1)
arrival_date = min_date
departure_date = min_date

room_count = 101
room_list = []
time_span_ok = False
days_selected = False
current_buttons = []

def date_picker():
    global time_span_ok
    global days_selected 
    global arrival_date
    global departure_date
    days_selected = False

    def confirm():
        global time_span_ok
        global days_selected
        global arrival_date
        global departure_date
        print(time_span_ok)
        if time_span_ok:
            print(arrival_date)
            print(departure_date)  
            days_selected = True
            calendar_window.destroy()
            show_rooms() 

    def date_check(date_parameter):
        global time_span_ok
        global departure_date
        global arrival_date
        
        arrival_date = arrival_enter.get_date()
        departure_date = departure_enter.get_date()
        
        if departure_date > min_date and departure_date > arrival_date and (departure_date - arrival_date).days <= 14:
            time_period = (departure_date - arrival_date).days
            # print(time_period)
            if time_period < 15 and time_period > 0:
                time_span_ok = True
            else:
                time_span_ok = False
                messagebox.showwarning("Error", "Stay must be between 1 and 14 days")
        else:
            messagebox.showwarning("Error", "You have selected dates and/or a time range that are not in line with our booking rules, please check the validity of your selection") 
            time_span_ok = False

    calendar_window = Toplevel(window)
    calendar_window.grab_set()
    calendar_window.title("Date picker")
    calendar_window.geometry("750x480")
    calendar_window.resizable(False, False)
    calendar_window.configure(bg ="#fffcf8")

    info_label = Label(calendar_window, text="Reservations cannot exceed two weeks and must be made a day prior to arrival.",font=("Times New Roman", 13),  bg="#fffcf8", fg="#bd8274", width = 60, height = 3)
    info_label.grid(column = 0, row = 0)

    arrival_label = Label(calendar_window, text="Arrival date:",font=("Times New Roman", 20,"bold"),  bg="#fffcf8", fg="#bd8274", width = 20, height = 5)
    arrival_label.grid(column = 0, row = 1)

    arrival_enter = DateEntry(calendar_window ,selectmode = "day",mindate = arrival_date, maxdate = date(2027, 12, 31), date_pattern="dd/mm/yyyy")
    arrival_enter.grid(column = 1, row = 1)
    arrival_enter.bind('<<DateEntrySelected>>',date_check)


    departure_label = Label(calendar_window, text="Departure date:  ",font=("Times New Roman", 20, "bold"),  bg="#fffcf8", fg="#bd8274", width = 20, height = 5)
    departure_label.grid(column = 0, row = 2)

    departure_enter = DateEntry(calendar_window ,selectmode = "day", mindate = departure_date, maxdate = date(2027, 12, 31),date_pattern="dd/mm/yyyy")
    departure_enter.grid(column = 1, row = 2)
    departure_enter.bind('<<DateEntrySelected>>', date_check)

    confirm_button = Button(calendar_window,text = "Confirm", font = ("Times New Roman", 15), width = 7, height = 2, bg = "#dfbd9c", activebackground = "#bd8274", command = confirm)
    confirm_button.grid(column = 0, row = 3)

def reserve(room_num):
    global days_selected 
    global arrival_date
    global departure_date
    
    if not days_selected:
        messagebox.showwarning("Error", "Please select dates first using the calendar button")
        return
    
    for room in room_list:
        if room.room_num == room_num:
            room.alr_reserved_on = True
            room.start_date = arrival_date
            room.end_date = departure_date
            messagebox.showinfo("Success", f"Room {room_num} has been reserved from {arrival_date.strftime('%d/%m/%Y')} to {departure_date.strftime('%d/%m/%Y')}")
            show_rooms() 
            break

def is_room_available(room, check_arrival, check_departure):
    if not room.alr_reserved_on:
        return True

    room_start = room.start_date
    room_end = room.end_date
    
    if (check_arrival <= room_start < check_departure) or (room_start <= check_arrival < room_end) or (check_arrival <= room_start < check_departure and room_start <= check_arrival < room_end):
        return False
    else:
        return True

def show_rooms():
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    selected_type = room_type_var.get()
    
    for room in room_list:
        type_match_any = selected_type == "Any" 
        type_match_either = room.room_type == selected_type
        
        available = True

        if days_selected:
            available = is_room_available(room, arrival_date, departure_date)
        
        if (type_match_any or type_match_either) and available:
            room_button = Button(main_frame, text = f"Room {room.room_num} - {room.room_type}", 
                               font = ("Times New Roman", 16), width = 30, height = 2,
                               bg = "#dfbd9c", activebackground = "#bd8274", 
                               command = lambda i =room.room_num: reserve(i))
            room_button.pack(pady = 5)


def on_type_change(*args):
    show_rooms()


window = Tk()
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.title("LegitHotel")
window.configure(bg ="#fffcf8")


main_frame_height = window.winfo_screenheight() - 100

main_frame = Frame(window, bg ="#fbf4e0", width = window.winfo_screenwidth(), height = main_frame_height)
main_frame.pack(side = BOTTOM, fill=BOTH, expand=True)

top_frame = Frame(window, bg = "#fffcf8", height = 100)
top_frame.pack(side = TOP)


calendar_button = Button(top_frame, text = "📅 Calendar", font = ("Times New Roman", 20), width = 10, height = 2, bg = "#dfbd9c", activebackground = "#bd8274", command = date_picker)
calendar_button.pack(padx = 10, side = LEFT)

room_type_label = Label(top_frame, text="Room type:", font=("Times New Roman", 22, "bold italic"), bg="#fffcf8", fg="#bd8274")
room_type_label.pack(padx = 10, side = LEFT)

room_type_var = StringVar()
room_type_var.set("Any")
room_type_menu = OptionMenu(top_frame, room_type_var, "Any", "Single", "Double")
room_type_menu.config(font = ("Times New Roman", 14), bg = "#dfbd9c", width = 8, height = 2, activebackground = "#bd8274")
room_type_menu.pack(padx = 10, side = LEFT)

room_count = 100
room_list = []

min_date_evil = date.today() + timedelta(days=1)
max_date_evil = date(2027, 12, 31)

allowed_range = (max_date_evil - min_date_evil).days

for room_num in range(101, 109):  
    room_count = room_num
    rand_type = random.choice(["Single", "Double"])
    
    alr_reserved = False
    rand_arr_date = None
    rand_dep_date = None
    
    if random.randint(0,12) <= 6:
        rand_start = random.randint(0, allowed_range)
        rand_end = random.randint(1, 14)
        rand_arr_date = min_date_evil + timedelta(days=rand_start)
        rand_dep_date = rand_arr_date + timedelta(days=rand_end)
        alr_reserved = True
    
    room_list.append(Reservations(room_count, rand_type, rand_arr_date, rand_dep_date, alr_reserved))

room_type_var.trace('w', on_type_change)

show_rooms()
    
window.mainloop()