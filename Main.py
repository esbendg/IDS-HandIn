#SpotifyCurrentSong.py needs a token from https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= put into the SPOTIFY ACCESS TOKEN

import tkinter as tk
from tkinter import *
import sys
from datoTid import getDate, getTime
from SpotifyCurrentSong import get_current_track, SPOTIFY_ACCESS_TOKEN
from nyheder import NewsFromBBC


window = tk.Tk()
window.title('SmortMirror')

#position of middle of the screen
"""windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/3 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))"""

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

    tick6=tick6+10
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



tdt()
tidnews()

screen = tk.Label(window)
screen.pack(anchor=NW, fill=X, padx=45)
screen.configure(background='black')

infolbl = tk.Label(window,textvariable=time_string_label, fg="white", bg="black", font=("Helvetica",40))
infolbl.pack(in_=screen, side=LEFT)
infolbl.place(relx=0.5, rely=0.5, anchor='nw')

spotifylbl = tk.Label(textvariable=spotify_string_label, fg="white", bg="black", font=("Helvetica",20))
spotifylbl.pack()

newslbl = tk.Label(textvariable=news_string_label, fg="white", bg="black", font=("Helvetica",30))
newslbl.pack(side=BOTTOM, anchor=W, fill=X)

window.wm_attributes('-fullscreen','true')
window.configure(background='black')

window.mainloop()