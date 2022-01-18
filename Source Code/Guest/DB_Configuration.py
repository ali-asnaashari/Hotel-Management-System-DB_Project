import csv
import mysql.connector


def exe_query(query):
    Hotel_DB = mysql.connector.connect(host="localhost", user="root", password="alishiraz127?", database="main")
    cursor = Hotel_DB.cursor()
    cursor.execute(query)
    res = cursor.fetchall()
    Hotel_DB.commit()
    Hotel_DB.close()
    return res


def read_user_details():
    detail = []
    with open("GuestDetails.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            detail.append(row[0])
            detail.append(row[1])
            detail.append(row[2])
            break

    return detail
