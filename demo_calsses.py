from typing import final
class Person:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary

    def greet(self):
        return "Hello World"
    
    @final
    def display_user(self):
        return f"{self.name} is a user with salary:{self.salary}"

class User(Person):
    def __init__(self,name,salary,age):
        super().__init__(name,salary)
        self.age = age

    def display_user(self):
        return f"{self.name} is a user with age:{self.age} and salary:{self.salary}"


p1 = Person("Anshu",10000)
print(p1.name)
print(p1.greet())

p2 = Person("John",25000)
print(p2.name)
print(p2.greet())

p2.name = "vishwas"
print(p2.name)

p3 = User("Srikanth",25000,25)
print(p3.display_user())

p1.school = "St.Johns"
print(p1.school)

