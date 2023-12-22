class Employee:
    def __init__(self,Name,Salary):
        self.name = Name
        self.salary  = Salary

    def get_properties(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    def aument_salary(self,porcent):
        augment = self.salary*(porcent/100)
        self.salary+=augment
        return f"Augment succesfully aplied, new salary is: ${self.salary}"
    
#Making employee instances
employee1 = Employee("Mike",1000)
employee2 = Employee("James",2000)

#Accesing first method
print(employee1.get_properties())
print(employee2.get_properties())

#Accesing second method
print(employee1.aument_salary(10))
print(employee2.aument_salary(15))

#printing updated salary
print(employee1.get_properties())
print(employee2.get_properties())