from PyQt5 import QtCore, QtGui, QtWidgets

from User.DB_Configuration import exe_query, read_user_details


class Ui_ReservedRoom(object):

    def setupUi(self, ReservedRoom):
        ReservedRoom.setObjectName("ReservedRoom")
        ReservedRoom.resize(1100, 840)
        ReservedRoom.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        ReservedRoom.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.tableWidget = QtWidgets.QTableWidget(ReservedRoom)
        self.tableWidget.setGeometry(QtCore.QRect(230, 160, 521, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.Reserved_Room_Append_PB = QtWidgets.QPushButton(ReservedRoom)
        self.Reserved_Room_Append_PB.setGeometry(QtCore.QRect(780, 160, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Reserved_Room_Append_PB.setFont(font)
        self.Reserved_Room_Append_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reserved_Room_Append_PB.setStyleSheet("background-color: rgb(28, 218, 255);")
        self.Reserved_Room_Append_PB.setObjectName("Reserved_Room_Append_PB")
        self.Reserved_Room_Remove_PB = QtWidgets.QPushButton(ReservedRoom)
        self.Reserved_Room_Remove_PB.setGeometry(QtCore.QRect(780, 250, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Reserved_Room_Remove_PB.setFont(font)
        self.Reserved_Room_Remove_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reserved_Room_Remove_PB.setStyleSheet("background-color: rgb(255, 98, 101);")
        self.Reserved_Room_Remove_PB.setObjectName("Reserved_Room_Remove_PB")
        self.Reserved_Room_Save_PB = QtWidgets.QPushButton(ReservedRoom)
        self.Reserved_Room_Save_PB.setGeometry(QtCore.QRect(780, 350, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Reserved_Room_Save_PB.setFont(font)
        self.Reserved_Room_Save_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reserved_Room_Save_PB.setStyleSheet("background-color: rgb(26, 255, 133);")
        self.Reserved_Room_Save_PB.setObjectName("Reserved_Room_Save_PB")
        self.Reserved_Room_Header_L = QtWidgets.QLabel(ReservedRoom)
        self.Reserved_Room_Header_L.setGeometry(QtCore.QRect(300, 60, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Reserved_Room_Header_L.setFont(font)
        self.Reserved_Room_Header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Reserved_Room_Header_L.setStyleSheet("background-color: rgb(243, 207, 255);")
        self.Reserved_Room_Header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Reserved_Room_Header_L.setObjectName("Reserved_Room_Header_L")

        self.retranslateUi(ReservedRoom)
        QtCore.QMetaObject.connectSlotsByName(ReservedRoom)

        # Append_Button
        self.Reserved_Room_Append_PB.clicked.connect(self.append_row)

        # Remove_Button
        self.Reserved_Room_Remove_PB.clicked.connect(self.remove_row)

        # Insert_Button
        self.Reserved_Room_Save_PB.clicked.connect(self.insert_data)

    def retranslateUi(self, ReservedRoom):
        _translate = QtCore.QCoreApplication.translate
        ReservedRoom.setWindowTitle(_translate("ReservedRoom", "Reserved Room"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ReservedRoom", "National ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ReservedRoom", "Firstname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ReservedRoom", "Lastname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ReservedRoom", "Gender(M-F)"))
        self.Reserved_Room_Append_PB.setText(_translate("ReservedRoom", "Append"))
        self.Reserved_Room_Remove_PB.setText(_translate("ReservedRoom", "Remove"))
        self.Reserved_Room_Save_PB.setText(_translate("ReservedRoom", "Save"))
        self.Reserved_Room_Header_L.setText(_translate("ReservedRoom", "Please Enter Your Companion Information"))

    def append_row(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)

    def remove_row(self):
        if self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount() - 1)

    def catch_data_from_table(self) -> list:
        All_data = []
        data = []
        for item in range(self.tableWidget.rowCount()):
            data.append(int(self.tableWidget.item(item, 0).text()))
            data.append(self.tableWidget.item(item, 1).text())
            data.append(self.tableWidget.item(item, 2).text())
            data.append(self.tableWidget.item(item, 3).text())
            All_data.append(data)
            data = []

        return All_data

    def insert_data(self):

        # TODO:Catch GUEST ID -> RUNS
        user_detail = read_user_details()

        # TODO:Catch Data From Table & Men -> 1 Female -> 0 -> RUNS
        all_data_in_table = self.catch_data_from_table()

        for i in range(len(all_data_in_table)):
            if all_data_in_table[i][3] == 'M' or all_data_in_table[i][3] == 'm':
                all_data_in_table[i][3] = True
            else:
                all_data_in_table[i][3] = False

        # TODO:Catch Reservation_ID WITH THIS GUEST ID -> RUNS
        reservation_id = exe_query(f""" 
                    SELECT Reservation_ID FROM reservation WHERE reservation.Guest_ID = {user_detail[0]}; 
                   """)

        last_record_of_reservation_with_this_user_id = reservation_id[len(reservation_id) - 1][0]

        # TODO:INSERT ROOM_IDS  INTO Reservation_Details's Table -> RUNS

        room_ids = read_room_ids()

        for row in range(len(room_ids)):
            nothing = "nothing"
            exe_query(f"""
                          INSERT INTO reservation_details
                          (Reservation_Details_Rate,Reservation_Details_Extra_Facilities,Room_ID,Reservation_ID)
                                              VALUES
                          ('{0}','{nothing}', '{room_ids[row]}','{last_record_of_reservation_with_this_user_id}');
                       """)

        # TODO:INSERT DATA INTO People's Table -> RUNS

        for row in range(self.tableWidget.rowCount()):
            exe_query(f"""
                          INSERT INTO people
                          (People_National_ID,People_Firstname,People_Lastname,People_Gender,Reservation_ID)
                                              VALUES
                          ('{all_data_in_table[row][0]}','{all_data_in_table[row][1]}','{all_data_in_table[row][2]}'
                           , {all_data_in_table[row][3]},'{last_record_of_reservation_with_this_user_id}');
                       """)

        print("all Function works Successfully")


def read_room_ids() -> list:
    f = open("room_ids.txt", "r")
    room_id = f.readline()
    lst = room_id.split(" ")

    room_ids_set = set()
    for i in range(len(lst) - 1):
        room_ids_set.add(lst[i])

    room_ids = list(room_ids_set)

    return room_ids
