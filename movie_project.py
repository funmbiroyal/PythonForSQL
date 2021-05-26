import mysql.connector
from mysql.connector import Error
conn = None
db_cursor = conn.cursor()

def connect():
    #conn = None
    try:
        conn = mysql.connector.connect(host= "localhost", database = "movie_project",user ="root", password = "Semicolon")
        print("connecting to database")
        if conn.is_connected:
            print("database connected")
           
    except Error as e:
        print("Not connecting due to", e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("database shutdown!")



def insert():
  connect()
  #user_choice = int(input("Enter to insert to movies table"))
  user_query= "insert into movies (title, release_year, genre, collection_in_mil) Values(%s,%s,%s,%s)"
  val  = []
  for i in range(1):
    title = input("Enter title ") 
    release_year = input("Enter release-year ")
    genre = input("Enter genre ")
    collection_in_mil = input("Enter collection_in_mil " )
    user_list = (title, release_year, genre, collection_in_mil)
    val.append(user_list)

    db_cursor.executemany(user_query,val)
    conn.commit()
    print(db_cursor.rowcount,"rows were successfully inserted")
    db_cursor.close

#insert = Operation
insert()

  
