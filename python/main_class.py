class Dog:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def bark(self):
        print("bark")

    def get_info(self):
        print(f"My name is {self.name} and my age is {self.age}")

    def set_attribite(self, color):
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


perro = Dog("Cat", 10)
perro.bark()
perro.get_info()
perro.set_attribite("Rojo")
perro.set_age(50)


print(f"The new attribute added was the color: {perro.color}")

print(f"The age attribute is {perro.get_age()}")
print(f"The color attribute is {perro.get_color()}")
print(f"The name attribute is {perro.get_name()}")

