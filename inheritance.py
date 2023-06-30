class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("Child classes must implement this")


class Dog(Animal):
    def speak(self):
        return "woof"


class Cat(Animal):
    def speak(self):
        return "meow"


dog = Dog("Bosco", "brown")
print(dog.name)
print(dog.color)
print(dog.speak())
cat = Cat("Roy", "black")
print(cat.name)
print(cat.speak())
print(cat.color)
