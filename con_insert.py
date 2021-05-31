import mysql.connector
from mysql.connector import Error

def connect_insert():
    '''Function to connect and fetch from the database'''

    #create a connection variable
    conn = None
    try:
        conn = mysql.connector.connect(host="localhost", database = "exercise", user="root", password= "Semicolon")
        print("Connecting to database server")
        if conn.is_connected:
            print("Connected to database server")
        db_cursor = conn.cursor()

        #create a variqble to contain  the sql query to be executed
        sql= "insert into Human (HumanId,name,color,gender,bloodgroup) Values(%s,%s,%s,%s,%s)"

     #prompt user to input values
        val = []
        for i in range(2):
            HumanId= int(input("Enter your HumanId"))
            name = input("Enter your name")
            color = input("Enter your color")
            gender = input("Enter your gender")
            bloodgroup = input("Your blood group please..")
            mylist = (HumanId, name, color, gender, bloodgroup)
            val.append(mylist)

        #create a list variable to contain all the values we want to insert into the human table from user prompt
        #val=(HumanId,name, color,gender,bloodgroup),
            # ('1014','Micheal', 'Brown','Male','o'),
            # ('1015','Sandy', 'Black', 'Female','OO')
        

        #create the query using executemany function
        db_cursor.executemany(sql,val)

        #commit to the database
        conn.commit()

        #print a success message
        print(db_cursor.rowcount, "rows were inserted")

        #close the cursor function
        db_cursor.close

    except Error as e:
        print("Not connecting due to : ",e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("database shutdown")

connect_insert()

