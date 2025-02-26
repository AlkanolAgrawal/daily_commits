class Animal:
    def __init__(self):
        print("Sounds Differently")
        
    def feet(self,x):
        self.leg = x;

class Dog(Animal):
    def __init__(self):
        print("Sounds WOOF")
        self.leg = 4
        
d1 = Dog()
print(d1.leg)
a = Animal()
a.feet(5)
print(a.leg)