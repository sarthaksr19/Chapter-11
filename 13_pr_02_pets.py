class Animals:
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    
    @staticmethod
    def bark():
        print("Dog is barking")
    

# animal = Animals()
# pet = Pets()
dog = Dogs()
dog.bark()

