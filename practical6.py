#Aim:Tell a person when they turn 100 years old
import datetime as dt
uname = input("Enter your Name: ")
age = int(input("Enter your Age: "))
cent = 100 - age
yea = (dt.datetime.now()).year + cent
print("You'll turn 100 in",cent,"years, that is in the year",yea)