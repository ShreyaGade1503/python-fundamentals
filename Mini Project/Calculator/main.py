
print("Simple Calculator")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Select Operator : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter Choice (1/2/3/4): ")

if choice == '1':
    result = add(num1 , num2)
    print("Result: ", result)
elif choice == '2':
    result = subtract(num1 , num2)
    print("Result: ", result)
elif choice == '3':
    result = multiply(num1 , num2)
    print("Result: ", result)
elif choice == '4':
    result = divide(num1 , num2)
    print("Result: ", result)
else:
    print("Invalid Choice")

