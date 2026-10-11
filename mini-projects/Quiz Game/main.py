print("WELCOME TO THE QUIZ GAME! ")

name = input("What is your name?")

list =[
    {
        "Q1": "What is the capital of india?",
        "Options" : ["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "Answer": "A"
    },
    {
        "Q2": "What is the largest state of india?",
        "Options" : ["A. Madhya Pradesh", "B. Uttar Pradesh", "C. Maharashtra","D. Rajasthan"],
        "Answer": "D"
    },
    {
        "Q3": "What is the national animal of india?",
        "Options" : ["A. Lion", "B. Tiger", "C. Elephant", "D. Peacock"],
        "Answer": "B"
    },
    {
        "Q4": "What is the prime number among the following?",
        "Options" : ["A. 4", "B. 6","C. 11", "D. 9"],
        "Answer": "C"
    },
    {
        "Q5": "What is the national bird of india?",
        "Options" : ["A. Peacock", "B. Sparrow", "C. Parrot", "D. Eagle"],
        "Answer": "A"
    },
]

print(list[0]["Q1"])
print(list[0]["Options"])
answer = input("Enter your answer (A/B/C/D): ")

if list[0]["Answer"] == answer:     
    score = 10

print(list[1]["Q2"])
print(list[1]["Options"])
answer = input("Enter your answer (A/B/C/D): ")

if list[1]["Answer"] == answer:
    score += 10

print(list[2]["Q3"])
print(list[2]["Options"])
answer = input("Enter your answer (A/B/C/D): ")

if list[2]["Answer"] == answer:
    score += 10

print(list[3]["Q4"])
print(list[3]["Options"])
answer = input("Enter your answer (A/B/C/D): ")

if list[3]["Answer"] == answer:
    score += 10

print(list[4]["Q5"])
print(list[4]["Options"])
answer = input("Enter your answer (A/B/C/D): ")

if list[4]["Answer"] == answer:
    score += 10

print(f"Your final score is: {score} out of 50") 