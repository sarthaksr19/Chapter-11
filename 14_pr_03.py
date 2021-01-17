class Employee:
    basicSalary = 1000
    increment = 2.0

    @property
    def salaryAfterIncrement(self):
        return self.basicSalary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment =  sai/self.basicSalary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 3000
print(e.salaryAfterIncrement)
print(e.increment)
