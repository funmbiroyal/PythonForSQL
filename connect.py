#Connect to mysql database using python and retrieve some data

#import the needed package
import mysql.connector
from mysql.connector import Error

#define the connector function
def connect_fetch():
    ''' function to connect and fetch and fetch rows in a database'''

    #create a variable for the connector object 
    conn = None

    try:
        conn=mysql.connector.connect(host= 'localHost', database = 'cape_codd', 
        user= 'root', password = 'Semicolon')
        print('Connecting to database server')
        if conn.is_connected:
            print('Connected to database server')
            #Select Query
        sql_select_query = "select * from buyer"
        cursor = conn.cursor()
        cursor.execute(sql_select_query)
        records  = cursor.fetchall()
        print('Total number of rows in buyer is: ', cursor.rowcount)
        
        #display the output data
        print('\nPrinting each buyer record')
        for row in records:
            print('Buyer Name', row[0])
            print('Department', row[1])
            print('Position',row [2])
            print('Supervisor:',row[3],'\n')
    
    except Error as e:
        print('Not connecting due to: ', e)

    finally: 
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown')


connect_fetch()            