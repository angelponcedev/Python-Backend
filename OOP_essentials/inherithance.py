# Father Class: -person
# Child Classes: -student  -employee

# the clild classes have to implment properties and methods of their own
# they have to have at least one method shared across the 3 classes, use polymorphism

class person:
    def __init__(self,Name,Age,School):
        self.name=Name
        self.age=Age
        self.school=School

    #Method to inherit to child classes
    def identify_Yourself():
        pass

class student(person):
    def __init__(self, Name, Age, School, Grade):
        # parent class init
        super().__init__(Name, Age, School)
        # child class property
        self.grade=Grade
    
    #Polymorphism of the inherited method
    def identify_Yourself(self):
        return f"{self.name} is a student and studies the {self.grade} grade"
    #Own method of the class student
    def studying(self,subject):
        return f"{self.name} is studying {subject}"

class employee(person):
    def __init__(self, Name, Age, School, Schedule):
        # parent class init
        super().__init__(Name, Age, School)
        # child class property
        self.schedule=Schedule

    #Polymorphism of the inherited method
    def identify_Yourself(self):
        return f"{self.name} is a employee and works {self.schedule} hours"
    #Own method of the class employee
    def working(self,matter):
        return f"{self.name} is working on {matter}"
    
student = student("Pedro",20,"UAA","4th")
employee = employee("Fernando",60,"UAA",8)

print(student.identify_Yourself())
print(student.studying("Math"))
print(employee.identify_Yourself())
print(employee.working("excel sheets"))