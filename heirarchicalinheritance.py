class Animal:
    def __init__(self,name):
        self.name=name
    def eating(self):
        print("We can eat like humans as we are also living beings") 
class Cat(Animal):
    def meow(self):
        print("meow meow is the way of style that how i make sound")
class Dog(Animal):
    def bow(self):
        print("bow bow is like how i make sound")

c = Cat("chinmai")
c.eating()
c.meow()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
d=Dog("lucky")
d.eating()
d.bow()