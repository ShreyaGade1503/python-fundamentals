'''

1 for Rock 
-1 for  Scissors
0 for Paper

'''
import random

randomNo = random.randint(-1, 1)
computer = randomNo

youstr = input("Enter your choice : ")

youDict = { "r" : 1 , "s" : -1 , "p" : 0 }
you = youDict[youstr]


if (computer == -1 and you == 1):
    print("You win ")

elif (computer == -1 and you == 0):
    print(" You lose ")

elif (computer == 0 and you == 1):
    print("You lose ")

elif (computer == 0 and you == -1):
    print("You win ")

elif (computer == 1 and you == -1):
    print("You lose ")

elif (computer == 1 and you == 0):
    print("You win ")

else:
    print("It's a tie ")    
    

print(f" Computer chose : {computer} and You chose : {you} ")