# Make two objects of the class Alumn wich have to contain
# Fields: name, id , score
# Methods: study, do homework, attend classes


# class definition
class Alumn:
    # constructor of objetcs
    def __init__(self,Name,Id,Score):
        self.name=Name
        self.id=Id
        self.score=Score

    #Method definitions
    def study(self,subject):
        return f"{self.name} is studying {subject}"
    
    def do_homework(self,number_of_assignments,expected_time):
        return f"{self.name} will do {number_of_assignments} assignments in {expected_time} minutes"
    
    def attend_classes(self,subjects):
        for subject in subjects:
            print (f"{self.name} will attend {subject}")
        
    
#Making objects of the class
alumn1 = Alumn("Juan","100","8")
alumn2  = Alumn("Pedro","222","7.8")

#Accesing methods foreach object
print(alumn1.study("math"))
print(alumn1.do_homework(4,40))
alumn1.attend_classes(["math","english"])

print(alumn2.study("physics"))
print(alumn2.do_homework(2,25))
alumn2.attend_classes(["physics","chemistry","Physical Education"])