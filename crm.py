import mysql.connector
import messfunctions as mf

a=input("Enter your id : ")
b="Select count(tid) from CSE"+a[0]+" where tid='"+a+"';"
mf.mycursor.execute(b)
myres=mf.mycursor.fetchall()
if (myres[0][0]==1):
    c=input("Enter your name :")
    flag=0
    d="Select tname from CSET where tid='"+a+"';"
    mf.mycursor.execute(d)
    myresult=mf.mycursor.fetchall()
    if(myresult[0][0]==c):
        if('T' in a):
            while(flag!=1):
                print("\nYou can perform the following operations - \n1. Take attendance\n2. Update marks\n3. Messages\n4. Apply for Leave\n5. Exit")
                choice=int(input("Enter the choice : "))
                if(choice==1):
                    mf.take_att(a)
                elif(choice==2):
                    mf.update_marks()
                elif(choice==3):
                    mf.message(a)
                elif(choice==4):
                    mf.leave(a)
                elif(choice==5):
                    flag=1
                else:
                    print("Entered wrong choice. Try again")
        elif('A' in a or 'B' in a):
            while(flag!=1):
                print("\nYou can perform the following operations - \n1. View stats\n2. View attendance\n3. Messages\n4. Apply for Leave\n5. Exit")
                choice=int(input("Enter the choice : "))
                if(choice==1):
                    print("View stats\n")
                elif(choice==2):
                    print("View attendance\n")
                elif(choice==3):
                    mf.message(a)
                elif(choice==4):
                    mf.leave(a)
                elif(choice==5):
                    flag=1
                else:
                    print("Entered wrong choice. Try again")
                    
        elif('H' in a):
            mf.message(a)
        else:
            print("No category found.")
    else:
        print("Incorrect name.")
else:
    print("Incorrect id.")
