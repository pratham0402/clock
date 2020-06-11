from time import *
from tkinter import *
from tkinter import ttk

def find_day():
    n = event[6]
    if n == 0:
        day_name = 'Monday'
    elif n == 1:
        day_name = 'Tuesday'
    elif n == 2:
        day_name = 'Wednesday'
    elif n == 3:
        day_name = 'Thursday'
    elif n == 4:
        day_name = 'Friday'
    elif n == 5:
        day_name = 'Saturday'
    else:
        day_name = 'Sunday'
    return day_name

root = Tk()

date = ttk.Label(root)
date.pack()

day = ttk.Label(root)
day.pack()

time_frame = ttk.Frame(height=50, width=20)
time_frame.pack()

hour_val = IntVar()
hour_box = ttk.Entry(time_frame, width=2, textvariable=hour_val)
hour_box.grid(row=0, column=0, padx=7, pady=7)
min_val = IntVar()
min_box = ttk.Entry(time_frame, width=2, textvariable=min_val)
min_box.grid(row=0, column=1, padx=7, pady=7)
sec_val = IntVar()
sec_box = ttk.Entry(time_frame, width=2, textvariable=sec_val)
sec_box.grid(row=0, column=2, padx=7, pady=7)

while True:
    event = localtime()
    date.configure(text=f'{event[2]} - {event[1]} - {event[0]}')
    day.configure(text=f'{find_day()}')
    hour_box.insert(0, event[3])
    min_box.insert(0, event[4])
    sec_box.insert(0, event[5])
    time_frame.update()
    day.update()
    date.update()

root.mainloop()