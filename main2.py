class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def identify(self):
        print("This is an animal class")
class Cat(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color
        
    def identify(self):
        return super().identify()
c1=Cat("kiti",2,"black")   
c1.identify()