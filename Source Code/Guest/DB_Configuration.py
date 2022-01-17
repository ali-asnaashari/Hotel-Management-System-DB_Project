import mysql.connector


def exe_query(query):
    Hotel_DB = mysql.connector.connect(host="localhost", user="root", password="alishiraz127?", database="main")
    cursor = Hotel_DB.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    Hotel_DB.commit()
    Hotel_DB.close()
    return res
