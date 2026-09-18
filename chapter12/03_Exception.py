try:
    a = int(input("Enter a number: "))  # characters
    print(a)

except Exception as e:
    print("An error occurred:", e)

except ValueError as ve:
    print("ValueError:", ve)