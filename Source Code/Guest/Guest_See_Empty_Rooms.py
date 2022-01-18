from PyQt5 import QtCore, QtGui, QtWidgets

from User.DB_Configuration import exe_query, read_user_details
import datetime

from User.Guest_ReservedRoom import Ui_ReservedRoom


class Ui_FreeRooms(object):

    def setupUi(self, FreeRooms):
        FreeRooms.setObjectName("FreeRooms")
        FreeRooms.resize(1094, 846)
        FreeRooms.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        FreeRooms.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.FreeRooms_DateEditOne = QtWidgets.QDateEdit(FreeRooms)
        self.FreeRooms_DateEditOne.setGeometry(QtCore.QRect(240, 120, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_DateEditOne.setFont(font)
        self.FreeRooms_DateEditOne.setStyleSheet("background-color: rgb(133, 196, 255);")
        self.FreeRooms_DateEditOne.setObjectName("FreeRooms_DateEditOne")
        self.FreeRooms_DateEditTwo = QtWidgets.QDateEdit(FreeRooms)
        self.FreeRooms_DateEditTwo.setGeometry(QtCore.QRect(680, 120, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_DateEditTwo.setFont(font)
        self.FreeRooms_DateEditTwo.setStyleSheet("background-color: rgb(133, 196, 255);")
        self.FreeRooms_DateEditTwo.setObjectName("FreeRooms_DateEditTwo")
        self.FreeRooms_From = QtWidgets.QLabel(FreeRooms)
        self.FreeRooms_From.setGeometry(QtCore.QRect(60, 120, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_From.setFont(font)
        self.FreeRooms_From.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.FreeRooms_From.setStyleSheet("background-color: rgb(219, 255, 255);")
        self.FreeRooms_From.setFrameShape(QtWidgets.QFrame.Panel)
        self.FreeRooms_From.setAlignment(QtCore.Qt.AlignCenter)
        self.FreeRooms_From.setObjectName("FreeRooms_From")
        self.FreeRooms_To = QtWidgets.QLabel(FreeRooms)
        self.FreeRooms_To.setGeometry(QtCore.QRect(500, 120, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_To.setFont(font)
        self.FreeRooms_To.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.FreeRooms_To.setStyleSheet("background-color: rgb(219, 255, 255);")
        self.FreeRooms_To.setFrameShape(QtWidgets.QFrame.Panel)
        self.FreeRooms_To.setAlignment(QtCore.Qt.AlignCenter)
        self.FreeRooms_To.setObjectName("FreeRooms_To")
        self.SeeFreeRooms_L = QtWidgets.QLabel(FreeRooms)
        self.SeeFreeRooms_L.setGeometry(QtCore.QRect(290, 30, 541, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SeeFreeRooms_L.setFont(font)
        self.SeeFreeRooms_L.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SeeFreeRooms_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.SeeFreeRooms_L.setAlignment(QtCore.Qt.AlignCenter)
        self.SeeFreeRooms_L.setObjectName("SeeFreeRooms_L")
        self.SeeFreeRooms_B = QtWidgets.QPushButton(FreeRooms)
        self.SeeFreeRooms_B.setGeometry(QtCore.QRect(870, 310, 151, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SeeFreeRooms_B.setFont(font)
        self.SeeFreeRooms_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SeeFreeRooms_B.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.SeeFreeRooms_B.setObjectName("SeeFreeRooms_B")
        self.FreeRooms_TableWidget = QtWidgets.QTableWidget(FreeRooms)
        self.FreeRooms_TableWidget.setGeometry(QtCore.QRect(60, 200, 761, 451))
        self.FreeRooms_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.FreeRooms_TableWidget.setObjectName("FreeRooms_TableWidget")
        self.FreeRooms_TableWidget.setColumnCount(6)
        self.FreeRooms_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(120, 105, 110))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.FreeRooms_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FreeRooms_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FreeRooms_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FreeRooms_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FreeRooms_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.FreeRooms_TableWidget.setHorizontalHeaderItem(5, item)
        self.FreeRooms_TableWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FreeRooms_Search_LE = QtWidgets.QLineEdit(FreeRooms)
        self.FreeRooms_Search_LE.setGeometry(QtCore.QRect(90, 770, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_Search_LE.setFont(font)
        self.FreeRooms_Search_LE.setObjectName("FreeRooms_Search_LE")
        self.FreeRooms_Filter_PB = QtWidgets.QPushButton(FreeRooms)
        self.FreeRooms_Filter_PB.setGeometry(QtCore.QRect(120, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_Filter_PB.setFont(font)
        self.FreeRooms_Filter_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FreeRooms_Filter_PB.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.FreeRooms_Filter_PB.setObjectName("FreeRooms_Filter_PB")
        self.FreeRooms_Enter_RoomID_LE = QtWidgets.QLineEdit(FreeRooms)
        self.FreeRooms_Enter_RoomID_LE.setGeometry(QtCore.QRect(820, 770, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_Enter_RoomID_LE.setFont(font)
        self.FreeRooms_Enter_RoomID_LE.setObjectName("FreeRooms_Enter_RoomID_LE")
        self.FreeRooms_Reserved_PB = QtWidgets.QPushButton(FreeRooms)
        self.FreeRooms_Reserved_PB.setGeometry(QtCore.QRect(860, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_Reserved_PB.setFont(font)
        self.FreeRooms_Reserved_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FreeRooms_Reserved_PB.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.FreeRooms_Reserved_PB.setObjectName("FreeRooms_Reserved_PB")
        self.FreeRooms_Enter_NumberOfNight_LE = QtWidgets.QLineEdit(FreeRooms)
        self.FreeRooms_Enter_NumberOfNight_LE.setGeometry(QtCore.QRect(530, 770, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FreeRooms_Enter_NumberOfNight_LE.setFont(font)
        self.FreeRooms_Enter_NumberOfNight_LE.setObjectName("FreeRooms_Enter_NumberOfNight_LE")
        self.SeeFreeRooms_NumberOfNight_L = QtWidgets.QLabel(FreeRooms)
        self.SeeFreeRooms_NumberOfNight_L.setGeometry(QtCore.QRect(520, 690, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SeeFreeRooms_NumberOfNight_L.setFont(font)
        self.SeeFreeRooms_NumberOfNight_L.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.SeeFreeRooms_NumberOfNight_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.SeeFreeRooms_NumberOfNight_L.setAlignment(QtCore.Qt.AlignCenter)
        self.SeeFreeRooms_NumberOfNight_L.setObjectName("SeeFreeRooms_NumberOfNight_L")

        self.retranslateUi(FreeRooms)
        QtCore.QMetaObject.connectSlotsByName(FreeRooms)

        self.FreeRooms_TableWidget.setColumnWidth(0, 80)
        self.FreeRooms_TableWidget.setColumnWidth(1, 80)
        self.FreeRooms_TableWidget.setColumnWidth(2, 180)
        self.FreeRooms_TableWidget.setColumnWidth(3, 120)
        self.FreeRooms_TableWidget.setColumnWidth(4, 180)
        self.FreeRooms_TableWidget.setColumnWidth(5, 120)

        # TODO:Clicked_Enter_Button_For_Show_Rooms -> RUNS
        self.SeeFreeRooms_B.clicked.connect(self.load_data)

        # TODO:Clicked_Rooms_Id_Button -> RUNS
        self.FreeRooms_Reserved_PB.clicked.connect(self.create_new_reservation_record)

        # TODO:Clicked_Filter_Button_For_Show_Rooms -> RUNS
        self.FreeRooms_Filter_PB.clicked.connect(self.show_room_detailed_filtered)

    def retranslateUi(self, FreeRooms):
        _translate = QtCore.QCoreApplication.translate
        FreeRooms.setWindowTitle(_translate("FreeRooms", "Free Rooms"))
        self.FreeRooms_From.setText(_translate("FreeRooms", "CheckIn Date"))
        self.FreeRooms_To.setText(_translate("FreeRooms", "CheckOut Date"))
        self.SeeFreeRooms_L.setText(_translate("FreeRooms", "See Empty Rooms Between Given Dates"))
        self.SeeFreeRooms_B.setText(_translate("FreeRooms", "Show Room"))
        item = self.FreeRooms_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("FreeRooms", "Room ID"))
        item = self.FreeRooms_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("FreeRooms", "Floor"))
        item = self.FreeRooms_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("FreeRooms", "Price Per Night"))
        item = self.FreeRooms_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("FreeRooms", "Beds Number"))
        item = self.FreeRooms_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("FreeRooms", "Description"))
        item = self.FreeRooms_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("FreeRooms", "Max Capacity"))
        self.FreeRooms_Filter_PB.setText(_translate("FreeRooms", "Filter"))
        self.FreeRooms_Reserved_PB.setText(_translate("FreeRooms", "Enter Room IDs"))
        self.SeeFreeRooms_NumberOfNight_L.setText(_translate("FreeRooms", "Number Of Nights"))

    def load_data(self):
        year = self.FreeRooms_DateEditOne.date().year()
        month = self.FreeRooms_DateEditOne.date().month()
        day = self.FreeRooms_DateEditOne.date().day()
        Date_From = datetime.datetime(year, month, day).isoformat()

        year1 = self.FreeRooms_DateEditTwo.date().year()
        month1 = self.FreeRooms_DateEditTwo.date().month()
        day1 = self.FreeRooms_DateEditTwo.date().day()
        Date_To = datetime.datetime(year1, month1, day1).isoformat()

        res = exe_query(f""" 
                         SELECT Room_ID,Floor, Price_Per_Night,no_beds,description,Maximum_Capacity FROM room
                         JOIN room_type rt on rt.room_type_id = room.room_type_id
                         WHERE Room_ID NOT IN
                         (SELECT room.Room_ID FROM room JOIN reservation_details rd on room.Room_ID = rd.Room_ID
                         JOIN reservation r on r.Reservation_ID = rd.Reservation_ID WHERE
                         Reservation_CheckIn >= '{Date_From}'  AND   Reservation_CheckOut <= '{Date_To}' )
                         AND (Room_Status_ID = 1 OR Room_Status_ID = 2 OR Room_Status_ID = 3) ORDER BY Room_ID;
                       """)

        row = 0
        self.FreeRooms_TableWidget.setRowCount(len(res))
        for data in res:
            self.FreeRooms_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.FreeRooms_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.FreeRooms_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.FreeRooms_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.FreeRooms_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.FreeRooms_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))

            row += 1

    def create_new_reservation_record(self):

        user_detail = read_user_details()

        year = self.FreeRooms_DateEditOne.date().year()
        month = self.FreeRooms_DateEditOne.date().month()
        day = self.FreeRooms_DateEditOne.date().day()
        Date_From = datetime.datetime(year, month, day).isoformat()

        year1 = self.FreeRooms_DateEditTwo.date().year()
        month1 = self.FreeRooms_DateEditTwo.date().month()
        day1 = self.FreeRooms_DateEditTwo.date().day()
        Date_To = datetime.datetime(year1, month1, day1).isoformat()

        today = datetime.date.today()

        if (
                (self.FreeRooms_Enter_NumberOfNight_LE.text() != ' ')
                and
                (self.FreeRooms_Enter_NumberOfNight_LE.text() != ' ')
        ):
            exe_query(f""" 
                          INSERT INTO reservation 
                          (Reservation_Date,Reservation_no_night,Reservation_CheckIn,Reservation_CheckOut,
                           Reservation_Bill_Total_Amount,Reservation_Bill_Status_Paid_Unpaid,Staff_ID,Booking_Status_ID
                           ,Guest_ID) 
                                              VALUES
                          ('{today}','{self.FreeRooms_Enter_NumberOfNight_LE.text()}','{Date_From}',
                           '{Date_To}','{0.00}' ,
                           FALSE, '{-1}','{1}','{user_detail[0]}'); 
                       """)

            print("Reservation Successful")
            self.catch_room_ids()

            self.Guest_Reserved_Room_Window()

    def show_room_detailed_filtered(self):
        year = self.FreeRooms_DateEditOne.date().year()
        month = self.FreeRooms_DateEditOne.date().month()
        day = self.FreeRooms_DateEditOne.date().day()
        Date_From = datetime.datetime(year, month, day).isoformat()

        year1 = self.FreeRooms_DateEditTwo.date().year()
        month1 = self.FreeRooms_DateEditTwo.date().month()
        day1 = self.FreeRooms_DateEditTwo.date().day()
        Date_To = datetime.datetime(year1, month1, day1).isoformat()

        Search_filter = '%' + self.FreeRooms_Search_LE.text() + '%'

        res = exe_query(f""" 
                         SELECT Room_ID,Floor, Price_Per_Night,no_beds,description,Maximum_Capacity FROM room
                         JOIN room_type rt on rt.room_type_id = room.room_type_id
                         WHERE Room_ID NOT IN
                         (SELECT room.Room_ID FROM room JOIN reservation_details rd on room.Room_ID = rd.Room_ID
                         JOIN reservation r on r.Reservation_ID = rd.Reservation_ID WHERE
                         Reservation_CheckIn >= '{Date_From}'  AND   Reservation_CheckOut <= '{Date_To}' )
                         AND (Room_Status_ID = 1 OR Room_Status_ID = 2 OR Room_Status_ID = 3)
                         AND  (rt.description LIKE '{Search_filter}') ORDER BY Room_ID;
                       """)

        row = 0
        self.FreeRooms_TableWidget.setRowCount(len(res))
        for data in res:
            self.FreeRooms_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.FreeRooms_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.FreeRooms_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.FreeRooms_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.FreeRooms_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.FreeRooms_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))

            row += 1

    def catch_room_ids(self):
        room_ids = self.FreeRooms_Enter_RoomID_LE.text().split(' ')
        f = open("File/room_ids.txt", "w")
        for i in range(len(room_ids)):
            f.write(room_ids[i] + ' ')
        f.close()

    def Guest_Reserved_Room_Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReservedRoom()
        self.ui.setupUi(self.window)
        self.window.show()
