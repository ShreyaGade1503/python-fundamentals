Dict = {
    
}

for i in range (1,6):
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    Dict[name] = marks

avg = sum(Dict.values()) / len(Dict)

print("Total Student Count: ", len(Dict))
print("Average Marks : ", avg)
print("Highest Marks : ", max(Dict.values()))
print("Lowest Marks : ", min(Dict.values()))

print("\nStudents who passed : " )
for name , marks in Dict.items():
    if marks >= 40:
        print(name)

print("\nStudents scored below average : ")
for name , marks in Dict.items():
    if marks <= avg:
        print(name)


print("Student who are failed : ")
for name, marks in Dict.items():
    if marks < 40:
        print(name)

print("students who scored above avg : ")
for name, marks in Dict.items():
    if marks > avg:
        print(name)

for name, marks in Dict.items():
    if marks == max(Dict.values()):
        print(name, "has scored the highest marks")

for name, marks in Dict.items():
    if marks == min(Dict.values()):
        print(name, "has scored the lowest marks")
        