class Person:
    country = "India"

    def __init__(self):
        print("Intializing person....\n")
    
    def language(self):
        print("I speak hindi")

class Employee(Person):
    company = "FaceBook"

    def getSalary(self):
        print(f"Employee's Salary is {self.salary}")

    def language(self):
        super().language()   #takes methods language from his base class.
        print("I am an employee who speaks hindi")

class Programmer(Employee):
    company = "Freelancing"

    def getSalary(self):
        print("No salary for programmer")

    def language(self):
        super().language() #this super() method used when we use base class method in derived class so here base class is employee so it takes employee language method in derived class.
        print("I am an Programmer who speaks hindi")

p = Person()
p.language()
e = Employee()
e.language()
pr = Programmer()
pr.language()