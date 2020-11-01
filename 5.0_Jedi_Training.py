  #Sign your name:Daniel Mitchell
import random
'''
 1. Make the following program work.
   '''

'''
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
 i = input("Enter a number: ")
 total = total + int(i)
print("The total is:", str(total))
  '''


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
'''
num = 1
for i in range(100):
    num = num +1
    if int(num) % 2 == 0:
        print (str(num))
'''


'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

'''
countstart = 10
while (countstart >= 0):
    print (str(countstart))
    countstart = countstart - 1
print("Blast Off!!")
'''




'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

'''
number = random.randint(1,10)
print(str(number))
'''


'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
totalnm = 0
numzero = 0
numposi = 0
numnegt = 0

for num in range(7):
    num = input("Give any number: ")
    totalnm = totalnm + int(num)
    if int(num) == 0:
        numzero = numzero + 1
    elif int(num) > 0:
        numposi = numposi + 1
    else:
        numnegt = numnegt + 1

print("Number of zeros: ", str(numzero))
print("Number of positives: ", str(numposi))
print("Number of negatives: ", str(numnegt))
print("Total: ", str(totalnm))