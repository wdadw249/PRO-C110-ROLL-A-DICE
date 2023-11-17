import random;
print("Hi this this a dice")
response = "Y"
while (response == "y" or response == "Y"):
    number = random.randint(1,6)
    if number == 1:
        
        print("     ")
        print("  0  ")
        print("     ")
       
    elif number == 2:
        print("0    ")
        print("     ")
        print("    0")
    elif number == 3:
        print("0    ")
        print("  0  ")
        print("    0")
    elif number == 4:
        print("0   0")
        print("     ")
        print("0   0")
    elif number == 5:
        print("0   0")
        print("  0  ")
        print("0   0")
    elif number == 6:
        print("0   0")
        print("0   0")
        print("0   0")
    response = input("Do you want to roll the dice: Y or N: ")  

print("You exited the program")
response = input("Do you want to roll the dice: Y or N: ") 