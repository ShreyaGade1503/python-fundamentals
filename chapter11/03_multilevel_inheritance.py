class student:
    a = 10

class teacher(student):
    b = 20

class principal(teacher):
    c = 30

#o = student()
#print(o.a) 
#print(o.b)
#print(o.c)

o = principal()
print(o.a) 
print(o.b)
print(o.c)