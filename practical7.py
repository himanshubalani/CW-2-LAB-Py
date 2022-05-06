#Aim: random number generator (Between 1 to 6)
import time
import random as rd

print("Rolling Dice...")
time.sleep(0.5)
print("You got",str(rd.randint(1,6))+"!")

list1 = [1,2,3,4,5,6]
print("In a list of numbers from 1 to 6, you get:",rd.choice(list1))

string1 = "umbrella"
print("Random letter from word 'umbrella':",rd.choice(string1))