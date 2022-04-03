class Dog:
    # creating class variables
    dogs = []
    x = 5

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _ in range(n):
            print("BARK!!!!")


tim = Dog("Tim")
brad = Dog("Brad")
# example of class variables, does not need any object definition like above
print(Dog.dogs)

# class-method example, doesn not need any object definition either
print(Dog.num_dogs())

# static-methods  also doesnt need explicit calling like above two
# also----used when we require particular static method declared as static for a considerable repititive use
Dog.bark(5)