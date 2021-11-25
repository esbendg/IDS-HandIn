#SpotifyCurrentSong.py needs a token from https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= put into the SPOTIFY ACCESS TOKEN

from pickle import STRING
import tkinter as tk
from tkinter import *
import sys
from typing import Literal
from datoTid import getDate, getTime
from SpotifyCurrentSong import get_current_track, SPOTIFY_ACCESS_TOKEN
from MoodData import *
from PIL import Image, ImageTk
import hand_track_class
import threading
import time
from nyheder import NewsFromBBC

#VARIABLES
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600

track_obj = hand_track_class.Hand_track()
track_obj.start()
track_obj.img_on()
track_obj.set_window_size(CANVAS_WIDTH, CANVAS_HEIGHT) #SET WINDOW SIZE

window = tk.Tk() #master tk window
window.title('SmortMirror') #window title

canvas = Canvas(window, width=1000, height=1000, bg="black") #creates a new canvas with coordinates and master window
canvas.pack() #packs the canvas
canvas.place(x = 0, y = 0)

# Add Images to Canvas widget
image = ImageTk.PhotoImage(Image.open('ball.png'))
img = canvas.create_image(250, 120, anchor=NW, image=image)

#position of middle of the screen

window.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")

window.update_idletasks()

news_string_label = StringVar()
time_string_label = StringVar()
spotify_string_label = StringVar()

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

def assign_event(mood_event):
    if mood_event == 0:
        save_happy()
    elif mood_event == 1:
        save_neutral()
    elif mood_event == 2:
        save_sad()

# class mood_buttons:
    #put the functions above into buttons.
rectangles = [[600,0,950,50], [600, 70, 950, 120], [600, 150, 950, 200]]

happyRectangle = canvas.create_rectangle(rectangles[0][0],rectangles[0][1],rectangles[0][2],rectangles[0][3], fill='green')
neutralRectangle = canvas.create_rectangle(rectangles[1][0],rectangles[1][1],rectangles[1][2],rectangles[1][3], fill='yellow')
sadRectangle = canvas.create_rectangle(rectangles[2][0],rectangles[2][1],rectangles[2][2],rectangles[2][3], fill='red')


infolbl = Label(canvas, textvariable=time_string_label, fg="white", bg="black", font=("Helvetica",20)) #label for time
infolbl.pack()
canvas.create_window(0, 100, window=infolbl, anchor="nw") 

spotifylbl = Label(canvas, textvariable=spotify_string_label, fg="#191414", bg="#1DB954", font=("Helvetica",20))
spotifylbl.pack()
canvas.create_window(CANVAS_WIDTH/2, CANVAS_HEIGHT-200, window=spotifylbl, anchor="n")

news_list = NewsFromBBC()

newslbl = tk.Label(canvas, textvariable=news_string_label, fg="white", bg="black", font=("Helvetica",20))
newslbl.pack(pady=20)
canvas.create_window(CANVAS_WIDTH/2, CANVAS_HEIGHT-100, window=newslbl, ) 
news_string_label.set("News are incoming")

def move():
   global image
   image = ImageTk.PhotoImage(Image.open('ball.png'))
   if track_obj.hand_on_img:
    index_x, index_y = track_obj.get_relative_index_pos()
    img = canvas.create_image(index_x, index_y, image=image)


#WHEN EVENTS HAPPENS:
def pinch_on(event):
    # print("Pinch")
    pass

def pinch_one(event):
    print("one pinch")
    for i in range(3):
        if (track_obj.is_inside_box(rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3])):
                assign_event(i)
                print(i)

count_seconds = 0
news_i = 0
def do_secondly(event):
    time_string_label.set(getTime() + "  " + getDate())
    spotify_string_label.set(get_current_track(SPOTIFY_ACCESS_TOKEN))
    #Happens every 10 seconds
    global count_seconds
    count_seconds += 1
    if count_seconds > 3:
        global news_i
        news_string_label.set(news_list[news_i])
        news_i += 1
        if news_i > 10:
            news_i = 0
        count_seconds = 0

def do_millisecondly(event):
    move()

# MAKE EVENTS FOR TKINTER
def getEvent():
    pinch_previous_frame = False
    time_here_for_sec = time.time()
    while True:
        if track_obj.is_pinch:
            try:
                window.event_generate('<<PINCH_ON>>', when='tail')
            except TclError:
                break
            if not pinch_previous_frame:
                window.event_generate('<<PINCH_ONE>>', when='tail')
        pinch_previous_frame = track_obj.is_pinch
        
        if time.time()-time_here_for_sec > 1:                   #Event that happens every second
            time_here_for_sec = time.time()
            try:
                window.event_generate('<<SECONDLY_UPDATE>>', when='tail')
            except TclError:
                break
        #This happens in every centisecond since the function sleeps after this
        try:
            window.event_generate('<<10MILLISEC_UPDATE>>', when='tail')
        except TclError:
            break
        time.sleep(0.01)


Thr=threading.Thread(target=getEvent)
Thr.start()

#Binding events to window
window.bind('<<PINCH_ON>>', pinch_on)
window.bind('<<PINCH_ONE>>', pinch_one)
window.bind('<<SECONDLY_UPDATE>>', do_secondly)
window.bind('<<10MILLISEC_UPDATE>>', do_millisecondly)

# window.wm_attributes('-fullscreen','true')
window.wm_attributes('-transparentcolor', '#185e05')

window.mainloop()

track_obj.stop()