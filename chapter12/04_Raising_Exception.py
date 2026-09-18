a = int(input("Enter a number: "))
b = int(input("Enter another number: "))


if b == 0:
    raise ZeroDivisionError("Hey Zero is not allowed")
else:
    print(f"the division of a/b is {a/b}")