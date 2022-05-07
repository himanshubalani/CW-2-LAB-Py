fhand = open("xyz.txt","r")
words = fhand.readlines()
print("Before:")
for word in words:
	print(word)
print("After:")
for spa in words:
	print(spa.replace(" ","#"))