class Employee:
    company = "Amul"
    salary = "3000"
    location = "Delhi"

    # def changeSalary(self, sal):  # here it doesn't change the class attribute salary but only change instance attribute in change salary.
    #     self.salary = sal   # so now we can change the class attribute with the help of class method. lets see..
    
    @classmethod   # pronounced as Decorater.
    ## with the help of class method keyword 'cls' we can actually change or add the attribute of class.
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(5000)
print(e.salary)
print(Employee.salary)