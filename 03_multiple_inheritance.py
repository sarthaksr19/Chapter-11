class Employee:
    company = "Visa"
    
class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee,Freelancer):  #one important thing to remember that here in parenthesis it prioritize which class name is written first so it prioritize Employee's method and his function.
    name = "Mohit"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)

