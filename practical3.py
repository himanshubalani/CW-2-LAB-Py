#Aim: Find if a number is a perfect square using math library
import math

# Taking the input from user
number = int(input("Enter the Number: "))

root = math.sqrt(number)  #Square Root
if int(root + 0.5) ** 2 == number:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")