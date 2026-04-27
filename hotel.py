#The program should maintain a list of rooms and a booking calendar. The user should be able to enter a period ( and end date) and book an available room. The program should check for availability and prevent double bookings in the same period.
#screen width -> 1536
#screen height -> 864

#too lazy to remove leftover comments


#tkinter for gui, tkcalendar for the date selectors, datetime for date calculations
from tkinter.ttk import *
from tkinter import *
from tkcalendar import DateEntry
from datetime import date
import time
import random

#minimum date to prevent people from trying to book past dates since people are stupid
min_date = date.today()
arrival_date = min_date
departure_date = min_date

room_count = 101
room_list = []
#for the confirm button so it can be checked whether the time span selected by the user fits the criteria
time_span_ok = False

days_selected = False

#the class for creating the rooms. 
class Reservations:
    def __init__(self, room_type, reservations):
        self.room_type = room_type
        self.reservations = reservations
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # ADD THE THINGS FROM THE PAPERS AND THE TRY.PY FILE!!!!!    #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

        
    

#button command to confirm slected time span. 

#button commnand to create toplevel window
def date_picker():
    global time_span_ok
    global days_selected 
    days_selected = False
    #didnt understand how to use class to remove this problem so for now it remains ¯\_(ツ)_/¯

    def confirm():
        global time_span_ok
        global days_selected
        print(time_span_ok)
        if time_span_ok:
            print(arrival_date)
            print(departure_date)  
            days_selected = True
            calendar_window.destroy()

    def date_check(date_parameter):    #-> selection event for the dateentries
        global time_span_ok
        global departure_date
        global arrival_date
        #print("ff15") -> selection event works so its smth else that got messed up prob the while loop? update: DO NOT ADD A LOOP THERE AGAIN

        while True:
            #gets the dates 
            arrival_date = arrival_enter.get_date()
            departure_date = departure_enter.get_date()
            # print("ff15") # -> ok so it does change as it should???
            # print(arrival_date)
            # print(departure_date)
            #makes sure its reserved at least a day in advanced and that you arrive before you leave
            if arrival_date > min_date and departure_date > min_date and departure_date > arrival_date:
                time_period = (departure_date - arrival_date).days #-> gets lenght of stay
                print(time_period)
                #makes sure it isnt longer than 14 days since thats a criteria
                if time_period < 15:
                    #
                    time_span_ok = True
                    # print(time_span_ok)
                    return arrival_date
                    return departure_date
                    break
                else:
                    time_span_ok = False
                    break
            else:
                time_span_ok = False
                break
            # break 
            # print(arrival_date > min_date)                
            # print(departure_date > min_date) 
            # print(arrival_date < departure_date)              
            # break

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

        
# for
        

# wth
    

#the bs mistake has been fixed, for tommorow:
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# finish up the date comparison!!! #  -> ✓ yay :D
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# GET_DATE() PROBLEM, POSSIBLE FIXES:                    #
#  1. Shove the function's def into the other function   #
# drawbacks:dont like that solution                      #
# advantages: if it works it'd be the easiest solution   #      Solution 1 was super easy 
#  2. Try to figure out how to make them non local vars  #   -> welp, leave it as is ig :(
# drawbacks: no idea how to do that                      #
# advantages: would be able to proceed as planned after  #
#  3. Add a while Data_Selected in the other function    #
# drawbacks: would be annoyingly split. Multiple tries   #
# advantages: idk ngl                                    #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

window = Tk()
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.title("LegitHotel")
window.configure(bg ="#fffcf8")


main_frame_height = window.winfo_screenheight() - 75

main_frame = Frame(window, bg ="#fbf4e0", width = window.winfo_screenwidth(), height = main_frame_height,)
main_frame.pack(side = BOTTOM)

top_frame = Frame(window, bg = "#fffcf8")
top_frame.pack(side = TOP)


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# ! POSSIBLE SOLUTION TO DATE SELECTION:                     #
#   1. Make it a new window                                  #       MAIN PROBLEM RESOLVED BY
#   2. Make a start and end date fields                      # ----> FINDING DATEENTRY WIDGET
#   3. Check if the difference is over 14 days               #
#   4. find a way (prob with a loop) to check availability   #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

# calender_box = Calendar(main_frame, selectmode = "day")
# calender_box.pack()


calendar_button = Button(top_frame, text = "📅 Calendar", font = ("Times New Roman", 20), width = 10, height = 6,bg = "#dfbd9c", activebackground = "#bd8274", command = date_picker)
calendar_button.pack(padx = 70, pady = 5, side = LEFT)

room_type_label = Label(top_frame, text="Room type:",font=("Times New Roman", 22, "bold italic"),  bg="#fffcf8", fg="#bd8274", width = 10, height = 5,)
room_type_label.pack(pady = 5, side=LEFT)

types = StringVar()
types.set("Single")
room_type = OptionMenu(top_frame, types, "Single", "Double")
room_type.config(font = ("Times New Roman", 20),bg = "#dfbd9c",height = 8 ,activebackground = "#bd8274")
room_type.pack(pady = 5, padx=2)



window.mainloop()



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# To-Do-List                                            #
#   1. Make the window ✓                                #
#   2. Make цalendar button ✓                           #
#   3. Make room type selector ✓                        #
#   4. Add the calendar✓  } these were completed by     #
#   5. Add  date selector✓}switching to using DateEntry #
#   6. Check room type                                   #
#   7. Add limitations to calendar ✓                     #
#   8. Check amount of days selected ✓                   #
#   9. Add rooms                                         #
#   10.Radnomize room availability                       #
#   11.Check room availability                           #
#   12.Enable change of room availability                #
#   13.Give rooms random type                            #
#   14.Show only selected type rooms                     #
#   Bonus: Add a monthly report                          #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

#~~~~~~~~~~~~~~~~~~~~~~#
#amount left: 7/14     #
#~~~~~~~~~~~~~~~~~~~~~~#

