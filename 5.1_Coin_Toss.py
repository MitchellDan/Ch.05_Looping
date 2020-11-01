'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random

numheads = 0
numtails = 0

for flip in range(50):
    flip = random.randint(0,1)
    if (flip == 0):
        print("Heads")
        numheads = numheads + 1
    else:
        print("Tails")
        numtails = numtails + 1

print("Number of heads: ", str(numheads))
print("Number of tails", str(numtails))









