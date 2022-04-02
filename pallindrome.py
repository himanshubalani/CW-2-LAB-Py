#check if a number is a pallindrome or not
inp = input("Enter a number")
li = []
rev = []
for i in inp:
    li.append(i)
for i in li :
    rev.append(li.pop(-1))
rev.append(li[0])
if li == rev
print("This is a pallindrome")
print("This is not a pallindrome")
