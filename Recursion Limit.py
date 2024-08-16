i=1
def recurr():
    global i
    print(i)
    i+=1
    recurr()
recurr()
    
