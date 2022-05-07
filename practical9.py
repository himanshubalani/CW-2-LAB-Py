#Aim: Count uppercase lowercase vowels consonants spaces or newlines
fname = "xyz.txt"
fhor = open(fname,"r")
upcase = lowcase = vow = con = spa = newl = 0
for i in fhor.read():
    if i.isupper():
        upcase += 1
    elif i.islower():
        lowcase += 1
    if i == 'a'or i == 'A' or i == 'e'or i == 'E' or i == 'i'or i == 'I' or i == 'o'or i == 'O' or i == 'u'or i == 'u':
        vow += 1
    elif i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        con += 1
    if i == " ":
        spa += 1
    if i == "\n" :
        newl += 1

print("The no. of uppercase letters are: ", upcase)
print("The no. of lowercase letters are: ", lowcase)
print("The no. of vowels are: ", vow)
print("The no. of consonants are: ", con)
print("The no. of spaces are: ", spa)
print("The no. of newline characters are: ", newl)