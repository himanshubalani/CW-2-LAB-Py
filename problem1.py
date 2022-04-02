#Create a Stack that shows four options
# 1.Push
# 2.Pop
# 3.Print
# 4.Exit

import os
from stack import Stack

def exit():
    print("Goodbye!")
    os._exit(0)

#flow

stack1 = []
print('''Hello! What Stack Operation should we perform today?
Press 1 to Push an element
Press 2 to Pop the last element
Press 3 to Print current Stack 
Press 4 to Exit''')

while True: 
    inp = int(input("Enter new option here: "))
    if inp == 1:
        ele = input("Please enter the value to insert: ")
        stack1.append(ele)
        print(ele, "pushed successfully")

    elif inp == 2:
        ele = stack1.pop()
        print(ele,"got deleted!")

    elif inp == 3:
        print(stack1)

    elif inp == 4:
        exit()

    else: print("Enter a valid number (1-4)")
