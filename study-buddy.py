#!/usr/bin/python
import pyttsx3
from tkinter import *

engine = pyttsx3.init()
def run(speech):
    engine.say(speech)
    engine.runAndWait()
    e1.delete(0,END)

if __name__=='__main__':
    master=Tk()
    Label(master, text="Enter Sentence").grid(row=0)
    e1 = Entry(master)
    e1.grid(row= 0,column=3)
    Button(master, text='Speak', command=lambda: run(e1.get())).grid(row=3, column=0, sticky=W, pady=4)
    mainloop()