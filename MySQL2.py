import mysql.connector  
from tkinter import messagebox

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R): 
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="aditya4sql10#")
        mycursor = mydb.cursor()
        print("Connection established!")

    except mysql.connector.Error as err:
        messagebox.showerror("Connection Error", f"Database connection not established: {err}")

    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS Heart_Data")
        mycursor.execute("USE Heart_Data")
        mycursor.execute("""CREATE TABLE IF NOT EXISTS data (
                            user INT AUTO_INCREMENT PRIMARY KEY,
                            Name VARCHAR(50),
                            Date VARCHAR(100),
                            DOB VARCHAR(100),
                            age VARCHAR(100),
                            sex VARCHAR(100),
                            Cp VARCHAR(100),
                            trestbps VARCHAR(100),
                            chol VARCHAR(100),
                            fbs VARCHAR(100),
                            restecg VARCHAR(100),
                            thalach VARCHAR(100),
                            exang VARCHAR(100),
                            oldpeak VARCHAR(100),
                            slope VARCHAR(100),
                            ca VARCHAR(100),
                            thal VARCHAR(100),
                            Result VARCHAR(100))""")
        
        command = """INSERT INTO data(Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, 
                                      exang, oldpeak, slope, ca, thal, Result)  
                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                     
        mycursor.execute(command, (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Register", "New user added successfully!!!!")
        
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error inserting data into database: {err}")
