class Employee:   #parent class  or Base class
    company = "Google"

    def getName(self):
        print(f"Employee name is {self.name}")

class Programmer(Employee):   #child class or Derived class.  #inherits the property of base class Employee.
    company = "YouTube"  #overridiing the parent class attribute as we see we override a class attribute of child class over parent class.
    language = "Python"
    def getLang(self):
        print(f"Language of the programmer in {self.company} is {self.language}")   #takes comapny name from it parent class i.e, Google.

e = Employee()
p = Programmer()
e.name = "Ram"
e.getName()
p.getLang()
print(p.company)