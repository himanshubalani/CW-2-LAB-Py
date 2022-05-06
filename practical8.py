#Aim: exception Handling

def divide():
	a = int(input("Enter your number: "))
	b = 4/a 
	return b

def conquer():
	try:
		print(divide())
	except ZeroDivisionError:
		print("Number is not divisible")

conquer()