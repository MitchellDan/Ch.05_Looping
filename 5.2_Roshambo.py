'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random

cont = 1
tie = 0
win = 0
loss = 0

while cont == 1:
    comp = random.randint(1,3)
    print()
    print()
    '''
    1 = rock
    2 = paper
    3 = scissors
    '''

    #Logic for setting the input to 1, 2 or 3. Just to make life easier. Hopefully.
    player = input("1).Rock 2).Paper 3).Scissors? ")
    if str(player).lower() == ("rock") or (player) == ("1"):
        player = 1
        print("Your choice was Rock")
    elif str(player).lower() == ("paper") or (player) == ("2"):
        player = 2
        print("Your choice was Paper")
    elif str(player).lower() == ("scissors") or (player) == ("3"):
        player = 3
        print("Your choice was Scissors")
    else:
        print("Input was not an option, try again.")

    #Prints the random choice
    if comp == 1:
        print("The program chose rock.")
    elif comp == 2:
        print("The program chose paper.")
    else:
        print("The program chose scissors.")

    #logic for deciding who won
    if (player - comp == 0):
        print("The game is a tie!")
        tie = tie + 1
    elif player == 1 and comp == 3:
        print("You won this game!")
        win = win + 1
    elif player == 2 and comp == 1:
        print("You won this game!")
        win = win + 1
    elif player == 3 and comp == 2:
        print("You won this game!")
        win = win + 1
    else:
        print("The program won this game!")
        loss = loss + 1

    #continue and end logic
    continp = input("Continue? y/n ")
    if continp == ("y"):
        print("Next Game!")
    else:
        print("Ending!")
        print("Ties: ", str(tie))
        print("Wins: ", str(win))
        print("Losses: ", str(loss))
        cont = 0










