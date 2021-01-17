class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Let's Multiply")
        return self.num * num2.num

    def __str__(self):   #other dinder methods __str__ executes directly when we want object to be printed.
        return (f"Decimal number: {self.num}")

    def __len__(self):   ## another dunder method.
        return 1

n = Number(9)
print(n)
print(len(n))

