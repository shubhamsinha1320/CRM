import mysql.connector

global mydb,mycursor

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="crm"
)
mycursor = mydb.cursor()


def read_all(tid):
    cc="Select tid,message,subject from "+tid+"_all order by sno desc;"
    mycursor.execute(cc)
    myre=mycursor.fetchall()
    aa=mycursor.rowcount
    if(aa!=0):
        for z in range(0,aa):
            print("\nSent by teacher id : "+myre[z][0]+"\nSubject : "+myre[z][2]+"\nMessage :\n"+myre[z][1]+"\n")

def take_att(tid):
    h=input("Enter section(A/B) : ")
    e="desc CSE"+h+"att"+tid+";"
    mycursor.execute(e)
    myresult=mycursor.fetchall()
    b=len(myresult)
    for x in range(0,b):
        if(x==0):
            f=input("Enter date(dd/mm/yy) : ")
            g="Insert into CSE"+h+"att"+tid+"(date) values ('"+f+"');"
            mycursor.execute(g)
            mydb.commit()
        else:
            g="Select sname from CSE"+h+" where sid='"+myresult[x][0]+"';"
            mycursor.execute(g)
            myresul=mycursor.fetchall()
            j="Select date from CSE"+h+"att"+tid+";"
            mycursor.execute(j)
            myresu=mycursor.fetchall()
            k=len(myresu)-1
            f=input("Enter attendance of "+myresul[0][0]+" : ")
            i="Update CSE"+h+"att"+tid+" set "+myresult[x][0]+"='"+f+"' where date='"+myresu[k][0]+"';"
            mycursor.execute(i)
            mydb.commit()
            if(f=='P'):
                l="Select totalatt from CSE"+h+" where sid='"+myresult[x][0]+"';"
                mycursor.execute(l)
                myres=mycursor.fetchall()
                n=myres[0][0]+1
                m="Update CSE"+h+" set totalatt="+str(n)+" where sid='"+myresult[x][0]+"';"
                mycursor.execute(m)
                mydb.commit()
    print("Attendance taken")

def update_marks():
    f="Select subject from CSET;"
    mycursor.execute(f)
    myresul=mycursor.fetchall()
    h=input("Enter section(A/B) : ")
    e="Select sid,sname from CSE"+h+";"
    mycursor.execute(e)
    myresult=mycursor.fetchall()
    b=len(myresult)
    for x in range(0,b):
        f=int(input("Enter marks of"+myresult[x][1]+"("+myresult[x][0]+") : "))
        g="Insert into CSE"+h+"("+myresul[0][0]+") values ("+f+");"
        mycursor.execute(g)
    print("Marks updated.")

def message(tid):
        print("Enter the choice value -\n\t1. Send Message\n\t2. Read Unread Messages\n\t3. Read All Messages")
        choice=int(input("Enter your choice : "))
        if(choice==1):
            tir=input("Enter id of recepient : ")
            send_me(tid,tir)
        elif(choice==2):
            unread(tid)
        elif(choice==3):
            read_all(tid)            
        else:
            print("Wrong choice entered.")

def leave(tid):
    a="Select leaveid from CSE"+tid[0]+"where tid='"+tid+"';"
    mycursor.execute(a)
    r=mycursor.fetchall()
    tir=r[0][0]
    f=input("Enter your message :\n")
    n="Select count(tid) from "+tir+";"
    mycursor.execute(n)
    r=mycursor.fetchall()
    sno=r[0][0]+1
    h="Insert into "+tir+" values('"+tid+"','"+f+"',"+str(sno)+",'Leave');"
    mycursor.execute(h)
    mydb.commit()
    print("\nMessage sent.")

def send_me(tid,tir):
    g="Select count(tid) from CSET where tid='"+tir+"';"
    mycursor.execute(g)
    myr=mycursor.fetchall()
    if (myr[0][0]==1):
        f=input("Enter your message :\n")
        n="Select count(tid) from "+tir+";"
        mycursor.execute(n)
        r=mycursor.fetchall()
        sno=r[0][0]+1
        h="Insert into "+tir+" values('"+tid+"','"+f+"',"+str(sno)+",'Message');"
        mycursor.execute(h)
        mydb.commit()
        print("\nMessage sent.")
    else:
        print("Enter valid recepient id")

def unread(tid):
    cc="Select tid,message from "+tid+" order by sno desc;"
    mycursor.execute(cc)
    myre=mycursor.fetchall()
    aa=mycursor.rowcount
    if(aa!=0):
        for z in range(0,aa):
            print("\nSent by teacher id : "+myre[z][0]+"\nSubject : "+myre[z][2]+"\nMessage :\n"+myre[z][1]+"\n")
        ee="Select count(tid) from "+tid+"_all;"
        mycursor.execute(ee)
        m=mycursor.fetchall()
        dd="INSERT INTO "+tid+"_all (tid,message,sno,subject) SELECT tid,message,sno+"+str(m[0][0])+",subject FROM "+tid+";"
        mycursor.execute(dd)
        mydb.commit()
        ff="Delete from "+tid+";"
        mycursor.execute(ff)
        mydb.commit()
    else:
        print("No unread messages to show")
