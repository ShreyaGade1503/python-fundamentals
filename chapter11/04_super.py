class Employee:
    def __init__(self):
        print("Constructor of Employee class")
    a = 10

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer class")
    b = 20

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager class")
    c = 30

# o = Employee()
# print(o.a) 

# o = Programmer()
# print(o.a , o.b)

o = Manager()
print(o.a, o.b, o.c)