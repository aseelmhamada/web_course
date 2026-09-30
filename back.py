class Students:
    def __init__(self, name , major,laptopObj):
        self.name = name
        self.major = major
        self.is_graduted=False
        self.laptopObj = laptopObj
    def showDetails(self):
        print(self.name,self.major)
class laptop:
    def __init__(self , brand , year):
        self.brand = brand
        self.year = year
    def showBrand(self):
        print(f"This Laptops brand is {self.brand}")
l1=laptop("hp",2026)
s1=Students("Aseel" ,"Computer Science",l1)
#s2=Students("Yousef" ,"Managmenet")

print(s1.laptopObj.brand)
