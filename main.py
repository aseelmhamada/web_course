class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self._age = age 
        self.__salary = salary
    def getSalary(self):
        print(f"The Employee Salary is {self.__salary}")
e1=Employee("ahamed",25,4000)
print(e1.name)
print(e1._age)
#print(e1.__salary)
e1.getSalary()