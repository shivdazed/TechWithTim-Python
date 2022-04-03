class Person(object):

    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getpopulation(cls):
        return cls.population

    @staticmethod
    def isadult(a):
        if a >= 18:
            print("Adult")
        else:
            print("Not an adult")

    def display(self):
        print(f'{self.name} is my name and I am {self.age}')


a = Person('Anuroop',27)

print(Person.getpopulation())
Person.isadult(18)

a.display()
