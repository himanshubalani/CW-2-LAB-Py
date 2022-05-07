#Aim: Find a string using regex
#Extract all emails present in mbox-short.txt
import re

fhand = open("mbox-short.txt","r")
lines = fhand.readlines()
for line in lines:
	ema = re.findall("[a-zA-Z0-9]\S*@\S*[a-zA-Z]", line)
	if len(ema) > 0:
		print(ema)
	else: continue