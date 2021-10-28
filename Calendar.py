from tkinter import *
from tkcalendar import *


surface_display = Tk()
surface_display.title('Kalendar')
surface_display.geometry( '720x720' )

cal = Calendar(surface_display, selectmode="day", year = 2021, month= 10, day = 28)
cal.pack(pady=20,fill="both", expand=True)

def grab_date():
    my_label.config(text=cal.get_date())


my_button = Button(surface_display, text="Gimme date", command= grab_date)
my_button.pack(pady=20)

my_label = Label(surface_display, text = "")
my_label.pack(pady = 20, fill = "both", expand=True)

surface_display.mainloop()
