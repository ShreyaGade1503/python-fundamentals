temp = int(input("Enter Temperature : "))

if temp < 0 :
    print(" Freezing Temperature. ")
elif temp > 0 and temp < 10 :
    print(" Very Cold Weather. ")
elif temp > 10 and temp < 20 :
    print(" Cold Waether. ")
elif temp > 20 and temp < 30 :
    print(" Normal Weather. ")
elif temp > 30 and temp < 40 :
    print(" Hot Weather. ")
else :
    print(" Its very Hot Weather. ")

    