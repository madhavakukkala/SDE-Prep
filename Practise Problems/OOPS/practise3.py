# class Person:

#     year = 2024

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# obj_1 = Person("Max", 30) 

# obj_2 = Person("madhav", 24)

# print(obj_1.name)
# print(obj_1.age)
# print()
# print(obj_2.name)
# print(obj_2.age)


class Animal:
    alive = True

class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Dog(Animal):
    def speak(self):
        print("Bow!")

class Car():

    alive = True

    def speak(self):
        print("Honk!")
        

animals = [Cat(), Dog(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)


    