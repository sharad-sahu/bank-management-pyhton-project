#my sql connection 
import pymysql as sq
mydb=sq.connect(host="localhost", user="root", password="9644626461", database="bank_management")
mycursor=mydb.cursor()

#choice options
lists="""          open new account press --> 1
          deposite amount press  --> 2
          widrawal amount press  --> 3
          check the balance      --> 4
          close or break this    --> 5 """
while True:
    print(lists)
    print("")#for space
    choice=int(input("enter your choice--->"))
    
# for choice 1 open account
    def OpenAccount():
        acno=int(input("enter account number"))
        name=input("enter name")
        address=input("enter Address")
        dob=input("enter dob -> 19-07-2002<--:")
        opning_bal=int(input("enter opening balace"))

        #insert query for information table
        ins="insert into information values(%s,%s,%s,%s)"
        #formatting values
        formated=(acno,name,address,dob)
        mycursor.execute(ins,formated)
        mydb.commit()
        #balance insert into amount table
        bal_ins="insert into amount values(%s,%s)"
        bal_formated=(acno,opning_bal)
        mycursor.execute(bal_ins,bal_formated)
        mydb.commit()  
        print("account open succesfully".upper())
        
#For choice 2 deposite mony 
    def deposite():
        acno=int(input("enter account number"))
        sel="select balance from amount where account_number=%s"
        t=(acno)
        mycursor.execute(sel,t)
        present_amount=mycursor.fetchone()

        #insert amount
        ask_amount=int(input("enter amount:"))
        #new amount
        new_amount=present_amount[0]+ask_amount
        print(new_amount)

        udtq="update amount set balance=%s where account_number=%s"
        x=(new_amount,acno)
        mycursor.execute(udtq,x)
        mydb.commit()
        print("amount deposite sucessfully......".upper())
        
#for choice 3 withdrawals mony
    def witdrawals():
        acno=int(input("enter account number"))
        sel="select balance from amount where account_number=%s"
        t=(acno)
        mycursor.execute(sel,t)
        present_amount=mycursor.fetchone()

        #insert amount
        ask_amount=int(input("enter amount:"))
        #new amount
        if present_amount[0]>=ask_amount:
            new_amount=present_amount[0]-ask_amount
            udtq="update amount set balance=%s where account_number=%s"
            x=(new_amount,acno)
            mycursor.execute(udtq,x)
            mydb.commit()
            print("amount withdrawals sucessfully......".upper()) 
        else:
            print("your balance is less than{}".format(ask_amount))

# for option 4 check the balance
    def check():
        acno=int(input("enter account number"))
        sel="select balance from amount where account_number=%s"
        t=(acno)
        mycursor.execute(sel,t)
        present_amount=mycursor.fetchone()
        print(present_amount[0])

    if choice==1:
        OpenAccount()

    elif choice==2:
        deposite()

    elif choice==3:
        witdrawals()

    elif choice==4:
        check()
        
    elif choice==5:
        print("thankyou".upper())
        break
    else:
        print("plz chose right option")
        
    
