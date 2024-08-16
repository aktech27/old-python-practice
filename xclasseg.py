class Family:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("Details are:\n")
        print(self.name)
        print(self.age)


father=Family("Riyaludeen",51)
mother=Family("Sahira Banu",41)
daughter=Family("Fathima Jemisa",21)
son=Family("Ahamed Kabeer",18)

father.display()
mother.display()
daughter.display()
son.display()
