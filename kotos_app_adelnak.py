# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 13:27:10 2023

@author: Gergely Kuroli
"""
from tkinter  import *
import tkinter as tk

count=0
num_events=21 # Ennyi sort tudsz rögzíteni a kötésedről

def sima(event):
    global num_events
    myLabel=Label(frame,text="Sima")
    myLabel.config(bg= "pink", fg= "white",font = "Verdana 10 bold")
    myLabel.pack()
    count=len(frame.winfo_children()[2:])  
    if count == num_events:                    # ez a feltétel megnézi, hogy mennyi adatot rögzítettél
        for item in frame.winfo_children()[2:]:
            item.destroy()
        
def fordított(event):
    global num_events
    myLabel=Label(frame,text="Fordított")
    myLabel.config(bg= "skyblue", fg= "black",font = "Verdana 10 bold")
    myLabel.pack()
    count=len(frame.winfo_children()[2:])
    if count == num_events:
        for item in frame.winfo_children()[2:]:
            item.destroy()

def clear_frame(event):
   for item in frame.winfo_children()[2:]:
        item.destroy()



root = Tk()
root.geometry("800x600")
frame =Frame(root,width=800,height=600)
frame.pack()

init=Label(frame,text="Bal egérklikk - Sima \n Billentyűzet - Fordított \n Enter - Törlés")
init.pack()

myButton=Button(frame,text="Elkezdek kötni!")
myButton.bind("<Button-1>",sima) 
myButton.pack(pady=20)
myButton.bind("<Key>",fordított)
myButton.bind("<Return>",clear_frame) # Button for manual deletion


root.mainloop()
