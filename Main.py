#SpotifyCurrentSong.py needs a token from https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= put into the SPOTIFY ACCESS TOKEN

from pickle import STRING
from tkinter import *
# from typing import Literal
from datoTid import getDate, getTime
from SpotifyCurrentSong import get_current_track, SPOTIFY_ACCESS_TOKEN
from MoodData import *
from PIL import Image, ImageTk
import hand_track_class
import threading
import time
from nyheder import NewsFromBBC

#VARIABLES for Canvas
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600

#Starting the hand-tracker object we created
track_obj = hand_track_class.Hand_track()
track_obj.start()
track_obj.img_on()
track_obj.set_window_size(CANVAS_WIDTH, CANVAS_HEIGHT) #SET WINDOW SIZE

#Making TK window
window = Tk() #master tk window
window.title('SmortMirror') #window title
#Crating canvas on in window
canvas = Canvas(window, width=1000, height=1000, bg="black") #creates a new canvas with coordinates and master window
canvas.pack() #packs the canvas
canvas.place(x = 0, y = 0)

#Window size
window.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")
window.update_idletasks()

#Making label variables for texts
news_string_label = StringVar()
time_string_label = StringVar()
spotify_string_label = StringVar()

# Saving the right mood in the pickle file  
def assign_mood(mood_event):
    if mood_event == 0:
        dato = getDate () +" : "+ getTime()
        add_data (dato, "happy")
    elif mood_event == 1:
        dato = getDate () +" : " + getTime ()
        add_data (dato, "neutral")
    elif mood_event == 2:
        dato = getDate () + " : "+ getTime()
        add_data (dato, "sad")

# Making the rectangle "buttons" for the mood tracker
rectangles = [[600,0,950,50], [600, 70, 950, 120], [600, 150, 950, 200]]

happy_rectangle = canvas.create_rectangle(rectangles[0][0],rectangles[0][1],rectangles[0][2],rectangles[0][3], fill='green')
neutral_rectangle = canvas.create_rectangle(rectangles[1][0],rectangles[1][1],rectangles[1][2],rectangles[1][3], fill='yellow')
sad_rectangle = canvas.create_rectangle(rectangles[2][0],rectangles[2][1],rectangles[2][2],rectangles[2][3], fill='red')
rect_list = [happy_rectangle, neutral_rectangle, sad_rectangle] #Putting them in a list to be able to call the index

#Creating the texts
time_label = Label(canvas, textvariable=time_string_label, fg="white", bg="black", font=("Helvetica",20)) #label for time
time_label.pack()
canvas.create_window(20, 20, window=time_label, anchor="nw") 

spotifylbl = Label(canvas, textvariable=spotify_string_label, fg="#191414", bg="#1DB954", font=("Helvetica",20))
spotifylbl.pack()
canvas.create_window(CANVAS_WIDTH/2, CANVAS_HEIGHT-200, window=spotifylbl, anchor="n")

news_list = NewsFromBBC() # Getting the news from BBC
newslbl = Label(canvas, textvariable=news_string_label, fg="white", bg="black", font=("Helvetica",20))
newslbl.pack(pady=20)
canvas.create_window(CANVAS_WIDTH/2, CANVAS_HEIGHT-100, window=newslbl, anchor="n") 
news_string_label.set("News are incoming")

# Calling this function to place the ball to the index finger tip
def move_ball():
   global image
   image = ImageTk.PhotoImage(Image.open('ball.png'))
   if track_obj.hand_on_img:
    index_x, index_y = track_obj.get_relative_index_pos()
    img = canvas.create_image(index_x, index_y, image=image)


#WHEN EVENTS HAPPENS:
def pinch_on(event): # While fingers pinched
    pass

repaint_boxes = False
def pinch_one(event): # Called onced when pinching. Like mouse click.
    global repaint_boxes
    for i in range(3):
        if (track_obj.is_inside_box(rectangles[i][0],rectangles[i][1],rectangles[i][2],rectangles[i][3])):
                assign_mood(i) # Saving the mood
                canvas.itemconfig(rect_list[i], fill='white') # Changing rect to white to show click
                repaint_boxes = True

count_seconds = 0
news_i = 0
def do_secondly(event): #This function is called in every second
    global repaint_boxes
    time_string_label.set(getTime() + "  " + getDate()) # Update time label
    spotify_string_label.set(get_current_track(SPOTIFY_ACCESS_TOKEN)) # Update spotify label
    global count_seconds
    count_seconds += 1
    if count_seconds > 3: #Happens every 3 seconds
        global news_i
        news_string_label.set(news_list[news_i]) # Update news label
        news_i += 1
        if news_i > 9:
            news_i = 0
        count_seconds = 0
    if repaint_boxes: #Changing back the color of the boxes after "click"
        canvas.itemconfig(rect_list[0], fill='green')
        canvas.itemconfig(rect_list[1], fill='yellow')
        canvas.itemconfig(rect_list[2], fill='red')
        repaint_boxes = False

def do_centisecondly(event): # Called in every centisecond
    move_ball()

# MAKE EVENTS FOR TKINTER
def getEvent():
    pinch_previous_frame = False
    time_here_for_sec = time.time()
    while True: # This runs throughout the program checking the state of variables and creating events accordingly
        if not run_Thread:
            break
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

run_Thread = True #Using it to stop the thread
Thr=threading.Thread(target=getEvent)
Thr.start()

#Binding events to window
window.bind('<<PINCH_ON>>', pinch_on)
window.bind('<<PINCH_ONE>>', pinch_one)
window.bind('<<SECONDLY_UPDATE>>', do_secondly)
window.bind('<<10MILLISEC_UPDATE>>', do_centisecondly)

# window.wm_attributes('-fullscreen','true')
window.wm_attributes('-transparentcolor', '#185e05')

window.mainloop()

#If program is closed
run_Thread = False
Thr.join()
track_obj.stop()
close_pkl()