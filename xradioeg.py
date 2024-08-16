import tkinter as tk
from tkinter import ttk

def Func():
     print("Element Selected: "+selection.get())
     
app = tk.Tk() 
app.geometry('700x100')

labelTop = tk.Label(app,text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

selection=tk.StringVar(None,"JANUARY") #default value to be selected goes in ""

R1=tk.Radiobutton(app,text="Jan",variable=selection,value="JANUARY",command=Func)
R2=tk.Radiobutton(app,text="Feb",variable=selection,value="FEBRUARY",command=Func)
R3=tk.Radiobutton(app,text="Mar",variable=selection,value="MARCH",command=Func)
R4=tk.Radiobutton(app,text="Apr",variable=selection,value="APRIL",command=Func)

R1.grid(column=1,row=0)
R2.grid(column=2,row=0)
R3.grid(column=3,row=0)
R4.grid(column=4,row=0)

app.mainloop()
