'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random

#set up variables for later
done = ("false")
milest = 0
milesrd = -20
thirst = 0
canteen = 3
camel = 0
rdist = abs(milesrd)

while done == ("false"): #print instructions

    if thirst >= 6:
        print("You died of thirst!")
        break

    print ("A. Drink from your canteen.")
    print ("B. Ahead moderate speed.")
    print ("C. Ahead full speed.")
    print ("D. Stop for the night.")
    print ("E. Status check.")
    print ("Q. Quit.")
    print()

    if thirst >= 4 and thirst < 6:
        print("You are thirsty")
        print()

    userinput = input("Select your action ") #ask for user input
    print()

    if userinput.lower() == ("e") or userinput.lower() == ("check"): #code for status check
        print("You have traveled " + str(milest) + " miles.") #print miles traveled
        print("The Raiders are " + str(rdist) + " miles behind you.") #print how far behind the raiders are
        print("Your camel is ") #camel thirst
        if canteen == 0:
            print("Your canteen is empty, good luck.")
        else:
            print("Your canteen has " + str(canteen) + " drinks left")
        print()

    elif userinput.lower() == ("d") or userinput.lower() == ("stop for the night"): #Stop for night
        camel = 0 #reset camel thirst
        print("The camel is happy but the raiders gain some ground")
        milesrd = milesrd + random.randint(6,13) #the raiders catching up
        print()

    elif userinput.lower() == ("c") or userinput.lower() == ("ahead full speed"): #Full speed ahead
        randforward = random.randrange(10, 20, 1)
        print("You move ahead as fast as you can. You make it "+ str(randforward) + " miles.")
        milest = milest + (randforward)
        milesrd = milesrd + (random.randrange(-14,4,1))
        camel = camel + (random.randrange(1,3,1))
        thirst = thirst + 1

    elif userinput.lower() == ("b") or userinput.lower() == ("ahead moderate speed"): #moderate speed
        randforward = random.randrange(5, 12, 1)
        print("You move ahead at a moderate speed. You make it " + str(randforward) + " miles.")
        milest = milest + randforward
        milesrd = milesrd + (random.randrange(-5, 9, 1))
        thirst = thirst + 1
        camel = camel + 1








