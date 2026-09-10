mark = int(input("Enter Mark : "))

if ( mark < 100 and mark >= 85 ):
    print("A grade")
elif ( mark < 85 and mark >= 70 ):
    print("B grade")
elif( mark < 70 and mark >= 60 ):
    print("C grade")
elif( mark < 60 and mark >= 40 ):
    print("Pass")
else:
    print("You are Fail! ")