from tkinter import *
root=Tk()
root.geometry('500x500')
loc=r'C:\Users\RIYALUDEEN\Desktop\BCA AK\Pics\Logo.png'
img=PhotoImage(file=loc)
c=Canvas(width=500,height=500,bg='black')
c.place(x=0,y=0)
c.create_image(0,0,image=img,anchor=NW)
root.mainloop()
