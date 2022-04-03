class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'My name is {self.name} and my age is {self.age}')

    def talk(self):
        print("BARK BARK!")

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("Meow")


tippy = Dog("Tippy", 14)
tippy.speak()
tippy.talk()

gary = Cat("Gary", 8, 'orange')
gary.speak()
gary.talk()


