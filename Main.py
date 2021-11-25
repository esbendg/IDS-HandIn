#SpotifyCurrentSong.py needs a token from https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= put into the SPOTIFY ACCESS TOKEN

import tkinter as tk
from tkinter import *
import sys
from typing import Literal
from datoTid import getDate, getTime
from SpotifyCurrentSong import get_current_track, SPOTIFY_ACCESS_TOKEN


from MoodData import *
from PIL import Image, ImageTk

window = tk.Tk()
window.title('SmortMirror')
# Define a Canvas widget

# Define a Canvas widget
canvas = Canvas(window, width=5000, height=5000, bg="white")
canvas.pack(anchor= CENTER, padx = 10, pady=10)
canvas.place(x = 0, y =0)

# Add Images to Canvas widget
image = ImageTk.PhotoImage(Image.open('ball.png'))
img = canvas.create_image(250, 120, anchor=NW, image=image)


#position of middle of the screen

window.geometry("1000x1000")

window.update_idletasks()

time_string_label = StringVar()
spotify_string_label = StringVar()

#window.wm_attributes('-fullscreen','true')
#window.wm_attributes('-transparentcolor', '#185e05')

#variables that can be set as globals in functions. They count
tick6 = 0
story_count = 0
total_tick = 0
tid = 0

# tdt = time date text
def tdt():
    global total_tick
    global tick6
    #runs every second
    time_string_label.set(getTime() + "  " + getDate())
    
    total_tick = total_tick + 10

    tick6=tick6+1
    if (tick6 >= 1000):
        spotify_string_label.set(get_current_track(SPOTIFY_ACCESS_TOKEN))
        tick6=0
        #print("track")
    window.after(1000, tdt)
    
#button to be put in the right spot
"""
made three functions that save the right mood
"""
def save_happy ():
    dato = getDate () +" : "+ getTime()
    add_data (dato, "happy")
    close_pkl()
    
def save_neutral ():
    dato = getDate () +" : " + getTime ()
    add_data (dato, "neutral")
    close_pkl()

def save_sad ():
    dato = getDate () + " : "+ getTime()
    add_data (dato, "sad")
    close_pkl()
#put the functions above into buttons.
happy_button = Button(window, text="Happy", command=save_happy)
happy_button.pack(anchor=NE)
neutral_button = Button(window, text="Neutral", command=save_neutral)
neutral_button.pack(anchor=NE)
sad_button = Button(window, text="Sad", command=save_sad)
sad_button.pack(anchor=NE)

tdt()



infolbl = tk.Label(window,textvariable=time_string_label, fg="white", bg="grey", font=("Helvetica",40))
infolbl.pack(in_=window, side=BOTTOM)


spot = tk.Label(window)
spot.pack(anchor=S, fill=X, padx=45)
spot.configure(background='black')
spotifylbl = tk.Label(textvariable=spotify_string_label, fg="white", bg="black", font=("Helvetica",20), anchor='w')
spotifylbl.pack(in_=window, side=LEFT)

"""newslbl = tk.Label(textvariable=news_string_label, fg="white", bg="black", font=("Helvetica",20))
newslbl.place(x = 0, y = 0)
newslbl.pack()"""


window.wm_attributes('-fullscreen','false')


def left(e):
   x = -20
   y = 0
   canvas.move(image, x, y)

def right(e):
   x = 20
   y = 0
   canvas.move(image, x, y)

def up(e):
   x = 0
   y = -20
   canvas.move(image, x, y)

def down(e):
   x = 0
   y = 20
   canvas.move(image, x, y)

def move(e):
   global image
   image = ImageTk.PhotoImage(Image.open('ball.png'))
   img = canvas.create_image(e.x, e.y, image=image)

# Bind the move function
canvas.bind("<B1-Motion>", move)


window.mainloop()