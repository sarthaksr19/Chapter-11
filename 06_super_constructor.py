class Person:
    country = "India"

    def __init__(self):   #defining constructor
        print("Intializing person....\n")  # finally, this statement prints first as it is refreed from its derived class and then it goes into derived class.
    
    def language(self):
        print("I speak hindi")

class Employee(Person):
    company = "FaceBook"

    def __init__(self):     #defining constructor with super method as in below line.
        super().__init__()   #now here again a super method constuctor is used so it goes to its base class from where this class is derived.
        print("Intializing Employee....\n")  # after printing the base class statement. now this statement prints and goes into his derived class after printing this staement.

    def getSalary(self):
        print(f"Employee's Salary is {self.salary}")

    def language(self):
        super().language()   #takes methods language from his base class.
        print("I am an employee who speaks hindi")

class Programmer(Employee):
    company = "Freelancing"

    def __init__(self):    # defining constructor with super method as in below line.
        super().__init__()   # this super method first goes to its super class i.e, base class 
        print("Intializing Programmer....\n") # at last, this staement is print in the end. as his base class constructor is exceuted. 

    def getSalary(self):
        print("No salary for programmer")

    def language(self):
        super().language() 
        print("I am an Programmer who speaks hindi")

pr = Programmer()