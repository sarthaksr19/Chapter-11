class Person:
    country = "India"
    
    def language(self):
        print("I speak hindi")

class Employee(Person):
    company = "FaceBook"

    def getSalary(self):
        print(f"Employee's Salary is {self.salary}")

    def language(self):
        print("I am an employee who speaks hindi")

class Programmer(Employee):
    company = "Freelancing"

    def getSalary(self):
        print("No salary for programmer")

p = Person()
p.language()
e = Employee()
e.language()
print(e.company)
pr = Programmer()
print(pr.company)
print(pr.country)
pr.language()



    