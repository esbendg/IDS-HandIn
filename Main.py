import tkinter as tk
from tkinter import *
import sys
from datoTid import getDate, getTime

run = True
window = tk.Tk()
window.update_idletasks()
time_string_label = StringVar()
time_string_label.set('hello')
#window.wm_attributes('-fullscreen','true')
#window.wm_attributes('-transparentcolor', '#185e05')
informationer = tk.Label(textvariable=time_string_label, fg="white", bg="black", font=("Helvetica",40))
informationer.pack()
def tid():
    time_string_label.set(getTime() + "  " + getDate())

    window.after(1000, tid)

tid()


"""if __name__ == '__main__':
    while(run):
        tid()
"""
window.mainloop()