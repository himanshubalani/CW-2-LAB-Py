#Aim: Create a result analysis system
fname = (input("Enter your Full Name: ")).title()
email = input("Enter your Uni registerd Email ID: ")
print('''Choose your branch by it's number
1. C.S.E (Computer Science and Engineering)
2. E.T.C (Electronics and Tele-Communication)
3. E.E (Electrical Engineering)
4. M.E (Mechanical Engineering)
5. Other (PLease Specify)
Example: If my branch is C.S.E then i'll press 1''')
brn = int(input("Enter Here: "))  # branch input
if brn == 1:
    brn = "C.S.E"
elif brn == 2:
    brn = "E.T.C"
elif brn == 3:
    brn = "E.E"
elif brn == 4:
    brn = "M.E"
elif brn == 5:
    brn = (input("Enter your branch name: ")).title()
print("Enter only the number for roll No. and Semester")
roll = int(input("What's your Roll no? "))
sem = input("What Semester are you in? ")

print('''Let's check your marks
(Enter marks out of 70)''')
while True:
    aem = int(input("Enter your Apllied Physics (AP) Marks: "))
    ac = int(input("Enter your Applied Chemistry (AC) Marks: "))
    mth = int(input("Enter your Maths Marks: "))
    if roll >= 1 and roll <= 20:
        ele = int(input("Enter your 'Programming in C' Marks: "))
        sub = "Programming in C"
        break
    elif roll >= 21 and roll <= 40:
        ele = int(input("Enter your Electronics Marks: "))
        sub = "Electronics"
        break
    elif roll >= 41 and roll <= 60:
        ele = int(input("Enter your Physical Education Marks: "))
        sub = "Physical Education"
        break

#Total Marks
tol = str(aem + ac + mth + ele) + "/280"

#percentage calculation
peraem = (aem*100)//70
perac = (ac*100)//70
permth = (mth*100)//70
perele = (ele*100)//70
percent = (peraem + perac + permth + perele)//4

#Grade Calculation
if percent >= 80 :
    grd = "AA"
    sta = "PASS"
if percent >= 70 and percent < 80:
    grd = "AB"
    sta = "PASS"
if percent >= 60 and percent < 70:
    grd = "BB"
    sta = "PASS"
if percent >= 55 and percent < 60:
    grd = "BC"
    sta = "PASS"
if percent >= 50 and percent < 55:
    grd = "CC"
    sta = "PASS"
if percent >= 45 and percent < 50:
    grd = "CD"
    sta = "PASS"
if percent >= 40 and percent < 45:
    grd = "DD"
    sta = "PASS"
if percent >= 0 and percent < 40:
    grd = "FF"
    sta = "FAIL"



#MarkSheet 
print("\nCreating your MarkSheet...")
print("Name:", fname, "\t\t\tRoll No.", roll)
print("Email:", email, "\t\t\tSemester: ", sem)
print("Subject\t\t\tMarks\t\t\tPercentage")
print("AEM\t\t\t", aem, "\t\t\t", peraem )
print("AC\t\t\t", ac, "\t\t\t",perac)
print("Maths\t\t\t", mth, "\t\t\t", permth)
print(sub,"\t",ele,"\t\t",perele)
print("Percentage: ",percent,"\t\t\tTotal Marks:",tol)
print("Grade: ",grd,"\t\t\tStatus: ",sta)