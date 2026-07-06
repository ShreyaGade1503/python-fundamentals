import random

comp = random.randint(1,100)

you = int(input("Enter the Guess number between 1 to 100: "))

while you != comp:
    if you < comp:
        print(" Your Number is lesser than computer's number. Please try again. ")
    else:
        print(" Your Number is greater than computer's number. Please try again. ")
    
    you = int(input("Enter the Guess number between 1 to 100: "))
    

print("Congratulations! You guessed the correct number which is: ", comp)