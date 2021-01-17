## opertors in python can be overload with the help of dunder method. __add__,__mul__,etc are the dunder methods in python.
# for more we can see online on python documentation about operator overloading in python.

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's Multiply")
        return self.num * num2.num

n1 = Number(40)  #number object.
n2 = Number(5)
sum = n1 + n2 ##it enables the __add__ dunder function and return the value based on the operations. 
mul = n1 * n2
print(sum)
print(mul)

