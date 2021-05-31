import mysql.connector
from mysql.connector import Error

def connect_fetch():
    conn = None
    try:
        conn = mysql.connector.connect(host="localhost", database='exercise', user='root', password='Semicolon')
        print("connecting to database server")
        if conn.is_connected:
            print('connected to database server')
            #Query
            sql_select_query = 'select * from Human'
            cursor = conn.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Total number of rows in human is :" ,cursor.rowcount)
            #print
            print("\n, printing each row in human records")
            for row in records:
                print('HumanId',row[0])
                print('Name',row[1])
                print('Color',row[2])
                print('Gender',row[3])
                print('Bloodgroup',row[4],"\n")

    except Error as e:
        print('Not connecting due to: ', e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database Shutdown')

connect_fetch()
