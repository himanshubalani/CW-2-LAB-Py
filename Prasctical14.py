import pickle
def  writebin(sroll,sname):
    with open ('studentrecord.dat','ab') as myfile:
        srecord={"SROLL":sroll,"SNAME":sname}        
        pickle.dump(srecord,myfile)
       
def readbin():
    with open ('studentrecord.dat','rb') as myfile:
        print("\n-------DISPALY STUDENTS DETAILS--------")
        print("\nRoll No.",' ','Name','\t',end='')
        print()
        while True:
           try:
               rec=pickle.load(myfile)
               print(' ',rec['SROLL'],'\t  ' ,rec['SNAME'])
           except EOFError:
                break

def SearchRecord(roll):
    with open ('studentrecord.dat','rb') as myfile:
       while True:
          try:
               rec=pickle.load(myfile)
               if rec['SROLL']==roll:
                   print("Roll NO:",rec['SROLL'])
                   print("Name:",rec['SNAME'])
                   break

          except EOFError:
               print("Record not find..............")
               print("Try Again..............")
               break

def main():
   
    while True:
        print('\nYour Choices are: ')
        print('0.Exit (Enter 0 to exit)')
        print('1.Dispaly Records') 
        print('2.Search Records (By Roll No)')
        
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            readbin()
        elif ch==2:
            r=int(input("Enter a Rollno to be Search: "))
            SearchRecord(r)
        else:
            break
main()