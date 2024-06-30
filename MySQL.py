import mysql.connector  # Import library to connect to MySQL databases
from tkinter import messagebox
# Import messagebox for pop-up messages
# 

def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):  # Function to save data to MySQL database
   
    try:
        # Connect to the MySQL database
        mydb = mysql.connector.connect(host="localhost",user="root",password="aditya4sql10#")
        mycursor = mydb.cursor()
        # Print a message if connection is successful (currently commented out)
        print("Connection stablished!")

    except:
        # Handle connection errors
        messagebox.showerror("Connection", "Database connection not stablished!!")

    
    try:
        command="create database Heart_Data"
        mycursor.execute(command)
        
        command="use Heart_Data"
        mycursor.execute(command)
        
        command="create table data(user int auto_increment key not null, Name varchar(50),Date varchar(100),DOB varchar(100),age varchar(100),sex varchar(100),Cp varchar(100),trestbps varchar(100),chol varchar(100),fbs varchar(100),restecg varchar(100),thalach varchar(100),exang varchar(100),oldpeak varchar(100),slope varchar(100),ca varchar(100),thal varchar(100),result varchar(100))"
        mycursor.execute(command)
        
        command="insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result)  values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register","New user added sucessfully!!!!")
        
        
    except:
        mycursor.execute("use Heart_Data")
        mydb=mysql.connector.connect(host="localhost",user="root",password="aditya4sql10#",database="Heart_Data")
        mycursor=mydb.cursor()
         
        command="insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register","New user added sucessfully!!!!")
    
    
    
    
    
    
    
#Save_Data_MySql("mr unknown","08/08/2023","1979","44","1","1","233","233","1","1","233","1","233.0","0","2","1","0")
