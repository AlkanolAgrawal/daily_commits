class Car:
    def __init__(self,brand,model,year):
     self.brand =brand
     self.model = model
     self.year = year
b=input("Enter Brand :")
m=input("Enter Model :")
y=input("Enter Year :")

c1 = Car(b,m,y)
print(c1.brand,c1.model,c1.year)