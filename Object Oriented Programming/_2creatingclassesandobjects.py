class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'my name is {self.name} and my age is {self.age}')

    def change_name(self, name):
        self.name = name

    def change_age(self,age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


tippy = Dog('tujsifdg', 23)
lucky = Dog('alusdh', 31)

tippy.change_name('Tippy')
tippy.change_age(15)
tippy.add_weight(18)
tippy.speak()
print(f'and my weight is {tippy.weight}')

lucky.change_name('Lucky')
lucky.change_age(13)
lucky.add_weight(14)
lucky.speak()
print(f'and my weight is {lucky.weight}')

