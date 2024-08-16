class main:
    counter=0
    def __init__(self,num):
        self.num=num
        main.counter=main.counter+1
    def check(self):
        if((self.num)%2==0 and (self.num)!=0):
            print(self.num,"is even")
        elif((self.num)%2==1):
            print(self.num,"is odd")
        else:
            print(self.num,"is zero")
            
            
for i in range(1,100,1): 
    x=[None]*100  
    x[i]=eval(input("\nENTER A NUMBER(give an negative to stop):"))
    if(x[i]>=0):
     number=main(x[i])
     number.check()
    else:
       print("\nChecking over.Total tries are",main.counter)
       break
       
print("Thank You")
