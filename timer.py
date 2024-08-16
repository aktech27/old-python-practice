from tkinter import *
import time

second=0
minute=0
hour=0

def main():
    def changer(root,second,minute,hour):
        if(second==60):
            second=0
            minute+=1
        if(minute==60):
            minute=0
            hour+=1
        #{index:tobefilledwith>numberofplaces}    
        l1['text']='{:0>2}'.format(hour)
        l2['text']='{:0>2}'.format(minute)
        l3['text']='{:0>2}'.format(second)
        print('{:0>2}'.format(second))
        second+=1
        root.after(1000,lambda:changer(root,second,minute,hour))
        
    global second,minute,hour
    root=Tk()
    root.geometry('500x500')
    
    l1=Label(root,text=hour,bg='white',font=('Times','24'))
    l1.place(x=100,y=100)
    
    l4=Label(root,text=':',bg='white',font=('Times','24'))
    l4.place(x=135,y=100)
    
    l2=Label(root,text=minute,bg='white',font=('Times','24'))
    l2.place(x=150,y=100)
    
    l5=Label(root,text=':',bg='white',font=('Times','24'))
    l5.place(x=185,y=100)
    
    l3=Label(root,text=second,bg='white',font=('Times','24'))
    l3.place(x=200,y=100)

    root.after(0,lambda:changer(root,second,minute,hour))
    
    root.mainloop()

main()    
