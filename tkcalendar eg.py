import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def func1(event):
    mmddyyyy=dateentry.get()
    ddmmyyyy=str(mmddyyyy[3:5]+"/"+mmddyyyy[0:2]+"/"+mmddyyyy[6:])
    print(ddmmyyyy)
    
root=tk.Tk()

dateentry = DateEntry(root,locale='en_US', date_pattern='MM/dd/yyyy',weekendbackground="white",weekendforeground="black")
dateentry.pack()
dateentry.bind("<<DateEntrySelected>>",func1)

root.mainloop()
