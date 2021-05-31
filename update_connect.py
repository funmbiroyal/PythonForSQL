import mysql.connector
from mysql.connector import Error, connect

def connect_update():
    conn = None
    try:
        conn = mysql.connector.connect(host = "localhost", user = "root", database = "movie_project", password = "Semicolon")
        print("Connecting to the database")
        if conn.is_connected:
            print ("database connected")
            db_cursor = conn.cursor()

        count = int(input("How many rows do you want you update "))
        
        val = []
        for i in range(count):
            movie_id = input("Enter movie id ")
            title = input("Enter title ")
            release_year = input("Enter release-year ")
            genre = input("Enter genre ")
            collection_in_mil = input("Enter collection_in_mil ")

            sql_update_query1 = "update movies set title = \'" + title + "\' where id = \'" + movie_id + "\'"
            db_cursor.execute(sql_update_query1)
            conn. commit()

            sql_update_query2 = "update movies set release_year = \'" + release_year + "\' where id = \'" + movie_id + "\'"
            db_cursor.execute(sql_update_query2)
            conn. commit()

            sql_update_query3 = "update movies set genre = \'" + genre + "\' where id = \'" + movie_id + "\'"
            db_cursor.execute(sql_update_query3)
            conn. commit()

            sql_update_query4 = "update movies set collection_in_mil = \'" + collection_in_mil + "\' where id = \'" + movie_id + "\'"
            db_cursor.execute(sql_update_query4)
            conn. commit()
            #user_list = (title,release_year,genre,collection_in_mil)
            #val.append(user_list)

            
            print (db_cursor.rowcount, "row(s) were successfully inserted ")
            db_cursor.close
    except Error as e:
        print("Not connecting due to",e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close
            print("Database shutdown")
connect_update()