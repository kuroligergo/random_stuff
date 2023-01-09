# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:27:10 2023

@author: Gergely Kuroli
"""
from tkinter  import *
import tkinter as tk

count=0
num_events=20 # Ennyi sort tudsz rögzíteni a kötésedről
        
def sima(event):
    global num_events
    myLabel=Label(frame,text="Sima")
    myLabel.config(bg= "pink", fg= "white",font = "Verdana 10 bold")
    myLabel.pack()
    count=len(frame.winfo_children()[1:])  
    if count == num_events:                    # ez a feltétel megnézi, hogy mennyi adatot rögzítettél
        for item in frame.winfo_children()[1:]:
            item.destroy()
        
def fordított(event):
    global num_events
    myLabel=Label(frame,text="Fordított")
    myLabel.config(bg= "skyblue", fg= "black",font = "Verdana 10 bold")
    myLabel.pack()
    count=len(frame.winfo_children()[1:])
    if count == num_events:
        for item in frame.winfo_children()[1:]:
            item.destroy()

def total(event):
    print(count)
    print(num_events)
    print(frame.winfo_children()[1:])
    print()

root = Tk()
root.geometry("800x600")
frame =Frame(root,width=800,height=600)
frame.pack()


myButton=Button(frame,text="Elkezdek kötni!")
myButton.bind("<Button-1>",sima) 
myButton.pack(pady=20)
myButton.bind("<Key>",fordított)
myButton.bind("<Return>",total)


root.mainloop()
