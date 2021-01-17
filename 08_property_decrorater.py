class Employee:
    company = "Indian gas"
    salary = 7000
    bonusSalary = 500
    # totalSalary = 7000+500  # we cannot hardcor the total salary as total salary may be varies from time to time so we use property decorator

    @property     #here we use property decorator as seems like a property
    def totalSalary(self):  #we make as a method but it actually acts as a property of the class just like all the property are written below the class name but it offers one very important thing that is it can't hardcore the value of any property. 
        return self.salary + self.bonusSalary

e = Employee()
print(e.totalSalary)