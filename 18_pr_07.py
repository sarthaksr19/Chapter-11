class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]   #list slicing as we don't want + in the last.

    def __add__(self, vec2):  #sum product.
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):  #dot product.
        if len(self.vec) == len(vec2):  #checking the length of the gievn vector if they are equal in length then it goes in for loop otherwise
            sum = 0
            for i in range (len(self.vec)):
                sum += self.vec[i] * vec2.vec[i]
            return sum
        else:   # this block of code will be exceute.
            return f"given vectors are not equal"

    def __len__(self):   #__len__ dunder used here to determine the length of the vector list.
        return len(self.vec)


v1 = Vector([1,4,3])
v2 = Vector([1,4,6])
print(v1*v2)
print(len(v1))
print(len(v2))


