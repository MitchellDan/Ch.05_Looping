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

print("You have just stolen a priceless gem from a band of raiders in the desert.")
print("All was going well until you got spotted on your way out.")
print("You manage to make it 20 miles before the raiders set out after you.")
print("If you can make it 200 miles across the desert to your waiting plane you will assure your safe escape.")
print("Good Luck.")
print()
goahead = input("continue? (press enter)")
print()

while done == ("false"):

    rdist = abs(milesrd)
    seveneleven = random.randint(1,40)

    if thirst >= 6: #death of thirst
        print("You died of thirst!")
        break

    if camel >= 8: #Camel death
        print("Your camel is dead, you will never make it now.")
        break

    if milesrd >= 0: #raiders catching you
        print("The raiders have caught you! ... I hope you are ready for a painful death.")
        break

    if milest >= 200: #win condition
        print("You have made it through the desert, You have won!")
        break

    if seveneleven == 7 or seveneleven == 11: #oasis
        print("You found a random Seven11 is the middle of the desert!?!?!?!")
        print("I guess you and your camel can get a drink? ... yeah sure...")
        print("Your thirst, camel and, canteen have all be reset!")
        print()
        camel = 0
        thirst = 0
        canteen = 3


    print ("A. Drink from your canteen.")  #print options
    print ("B. Ahead moderate speed.")
    print ("C. Ahead full speed.")
    print ("D. Stop for the night.")
    print ("E. Status check.")
    print ("Q. Quit.")
    print()

    if thirst >= 4 and thirst < 6: #thirst notif
        print("You are thirsty")
        print()

    if camel >= 6 and camel <8: #camel notif
        print("Your camel is tired")
        print()

    if rdist <= 15: #raiders notif
        print("The raiders are close!")
        print()

    userinput = input("Select your action ") #ask for user input
    print()

    if userinput.lower() == ("e") or userinput.lower() == ("check"): #code for status check
        print("You have traveled " + str(milest) + " miles.") #print miles traveled
        print("The Raiders are " + str(rdist) + " miles behind you.") #print how far behind the raiders are
        if canteen == 0: #canteen stat
            print("Your canteen is empty, good luck.")
        else:
            print("Your canteen has " + str(canteen) + " drinks left")
        print()
        goahead = input("continue? (press enter)")
        print()

    elif userinput.lower() == ("d") or userinput.lower() == ("stop for the night"): #Stop for night
        camel = 0 #reset camel thirst
        print("The camel is happy but the raiders gain some ground")
        milesrd = milesrd + random.randint(6,13) #the raiders catching up
        print()

    elif userinput.lower() == ("c") or userinput.lower() == ("ahead full speed"): #Full speed ahead
        randforward = random.randrange(10, 20, 1)
        print("You move ahead as fast as you can. You make it "+ str(randforward) + " miles.")
        milest = milest + (randforward) #you moving
        milesrd = milesrd + (random.randrange(-14,4,1)) #raiders moving
        camel = camel + (random.randrange(1,3,1))
        thirst = thirst + 1
        print()

    elif userinput.lower() == ("b") or userinput.lower() == ("ahead moderate speed"): #moderate speed
        randforward = random.randrange(5, 12, 1)
        print("You move ahead at a moderate speed. You make it " + str(randforward) + " miles.")
        milest = milest + randforward #you moving
        milesrd = milesrd + (random.randrange(-5, 9, 1)) #raiders catching up
        thirst = thirst + 1
        camel = camel + 1

    elif userinput.lower() == ("a") or userinput.lower() == ("drink from your canteen"): #drink from canteen
        if canteen > 0:
            canteen = canteen - 1
            thirst = 0
        else:
            print("Your Canteen is empty, good luck.")








