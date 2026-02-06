import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='AIRLINES')
if conn.is_connected():
    print("Successfully Connected... \n -WELCOME to AIRLINE MANAGEMENT SYSTEM-")
cur=conn.cursor()
d=1
while(d==1):
    print("__________________________________________________________")
    print("\n=== AIRLINES MENU ===")
    print("1 : Insert Your Flight Information. ")
    print("2 : Delete Your Flight Details. ")
    print("3 : Update Your Flight Details. ")
    print("4 : Search Your Flight Details. ")
    print("5 : Disp1ay Total Flight Details. ")
    print("6 : Display Fare.")
    print("7 : Exit.")
    ch=int(input("Enter Your Choice : "))
    if ch == 1:
        flightNO = input("Enter Flight Number: ")
        flightNAME = input("Enter Flight Name: ")
        Address = input("Enter Current Address: ")
        destination = input("Enter Destination: ")
        fclass = input("Enter Class: ")

        query = "INSERT INTO flight VALUES (%s, %s, %s, %s, %s)"
        values = [flightNO, flightNAME, Address, destination, fclass]

        cur.execute(query,values)
        conn.commit()
        print("Flight Inserted Successfully.")
        
    elif ch == 2:
        flightNo = input("Enter the Flight No to delete: ")
        query = "DELETE FROM flight WHERE flight_No = %s"
        cur.execute(query,(flightNo,))
        conn.commit()
        print(cur.rowcount, "Record(s) Deleted.")

    elif ch == 3:
        print("\nUpdate Options:")
        print("1. Flight Number")
        print("2. Flight Name")
        print("3. Address")
        print("4. Destination")
        print("5. Class")

        option = int(input("Enter your choice: "))

        old_value = input("Enter the value to be modified : ")
        new_value = input("Enter new value: ")

        fields = ["flight_NO", "flight_NAME", "Address", "destination", "class"]
        field = fields[option - 1]
        
        query = "UPDATE flight SET {0} = %s WHERE {0} = %s".format(field)
        cur.execute(query,(new_value,old_value))
        conn.commit()
        print("Successfully updated.")
        
    elif ch == 4:
        flightNAME = input("Enter flight Name to search: ")
        cur.execute("SELECT * FROM flight WHERE flight_NAME = %s",(flightNAME,))
        results = cur.fetchall()
        for row in results:
            print(row)

    elif ch == 5:
        cur.execute("SELECT * FROM flight")
        results = cur.fetchall()
        for row in results:
            print(row)
            
    elif ch == 6:
        print("Class Fare List:")
        print("1. First Class --> ₹6000 per passenger")
        print("2. Business Class --> ₹4000 per passenger")
        print("3. Economy Class --> ₹2000 per passenger")

        choice = int(input("Enter your choice: "))
        n = int(input("Number of passengers: "))

        if choice == 1:
            print("You selected First Class.")
            fare = 6000 * n
        elif choice == 2:
            print("You selected Business Class.")
            fare = 4000 * n
        elif choice == 3:
            print("You selected Economy Class.")
            fare = 2000 * n
        else:
            print("Invalid class selected.")
            fare = 0

        print("Total fare: ₹", fare)
        
    elif ch == 7:
            print("==Thanks for using the Airlines Management System.==")
            break

    else:
            print("Invalid option. Please try again.")

conn.close()
