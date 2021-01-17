class Employee:
    company = "Indian gas"
    salary = 5000
    bonusSalary = 0

    @property     #getter decorater or property decorator.
    def totalSalary(self):   
        return self.salary + self.bonusSalary
    
    @totalSalary.setter   #setter decorater
    def totalSalary(self, val):
        self.bonusSalary = val - self.salary


e = Employee()
# print(e.totalSalary)
e.totalSalary = 8000
print(f"total salary",e.totalSalary)
print(e.salary)
print(e.bonusSalary)