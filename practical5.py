#check palindrome practical 5
'''notes: if the input string is equal to the reverse string then it is a pallindrome '''


s = input("Enter a string: ")
r = s[::-1]

if s == r:
	print("It's a palindrome!")
else:
	print("It's not a palindrome")