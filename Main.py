#SpotifyCurrentSong.py needs a token from https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= put into the SPOTIFY ACCESS TOKEN

import tkinter as tk
from tkinter import *
import sys
from typing import Literal
from datoTid import getDate, getTime
from SpotifyCurrentSong import get_current_track, SPOTIFY_ACCESS_TOKEN
from nyheder import NewsFromBBC
from newsapi import NewsApiClient
from MoodData import *


window = tk.Tk()
window.title('SmortMirror')


window.update_idletasks()

time_string_label = StringVar()
spotify_string_label = StringVar()
news_string_label = StringVar()

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
    window.after(10, tdt)
    
NEWS_DATA1 = NewsFromBBC()


def tidnews():
    global tick6

    global story_count
    news_string_label.set(NEWS_DATA1[0])

    story_count = story_count + 1
    news_string_label.set(NEWS_DATA1[story_count])
    print(story_count)

    if (story_count == 9):
        story_count = 0
    window.after(6000,tidnews)


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
buttons = happy_button = Button(window, text="Happy", command=save_happy)
happy_button.pack()
happy_button.place(anchor="e")
neutral_button = Button(window, text="Neutral", command=save_neutral)
neutral_button.pack()
sad_button = Button(window, text="Sad", command=save_sad)
sad_button.pack()

tdt()
tidnews()

screen = tk.Label(window)
screen.pack(anchor=W, fill=X, padx=45)
screen.configure(background='black')

infolbl = tk.Label(window,textvariable=time_string_label, fg="white", bg="black", font=("Helvetica",40))
infolbl.pack(in_=screen, side=LEFT)
#infolbl.place(relx=0.5, rely=0.5, anchor='nw')

spot = tk.Label(window)
spot.pack(anchor=W, fill=X, padx=45)
spot.configure(background='black')
spotifylbl = tk.Label(textvariable=spotify_string_label, fg="white", bg="black", font=("Helvetica",20), anchor='w')
spotifylbl.pack(in_=spot, side=LEFT)
spotifylbl.place(x=45,y=540)

newslbl = tk.Label(textvariable=news_string_label, fg="white", bg="black", font=("Helvetica",30))
newslbl.pack(side=BOTTOM, anchor=W, fill=X)

window.wm_attributes('-fullscreen','true')
window.configure(background='black')

window.mainloop()