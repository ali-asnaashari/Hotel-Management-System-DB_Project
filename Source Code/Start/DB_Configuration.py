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


def read_user_details() -> list:
    detail = []
    with open("../User/Script/File/guest_details.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            detail.append(row[0])
            detail.append(row[1])
            detail.append(row[2])
            break

    return detail


def read_room_ids() -> list:
    f = open("../User/Script/File/room_ids.txt", "r")
    room_id = f.readline()
    lst = room_id.split(" ")

    room_ids_set = set()
    for i in range(len(lst) - 1):
        room_ids_set.add(lst[i])

    room_ids = list(room_ids_set)

    return room_ids


def read_rest_cafe_id() -> int:
    f = open("../User/Script/File/restaurant_id.txt", "r")
    restaurant_id = f.readline()
    return int(restaurant_id)


def admin_read_rest_cafe_id() -> int:
    f = open("../Admin/Script/File/restaurant_id.txt", "r")
    restaurant_id = f.readline()
    return int(restaurant_id)


def read_Food_ids() -> list:
    f = open("../User/Script/File/Food_ids.txt", "r")
    Food_id = f.readline()
    lst = Food_id.split(" ")

    food_ids = []

    for i in range(len(lst) - 1):
        food_ids.append(int(lst[i]))

    return food_ids


def read_reservation_id() -> int:
    f = open("../User/Script/File/Total_Billing_reservation_id.txt", "r")
    reservation_id = f.readline().split(" ")

    return int(reservation_id[0])


def read_recep_details() -> list:
    detail = []
    with open("../Receptionist/script/File/recep_details.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            detail.append(row[0])
            detail.append(row[1])
            detail.append(row[2])
            break

    return detail
