from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

from Start.DB_Configuration import exe_query


class Ui_cleaning_room(object):

    def setupUi(self, cleaning_room):
        cleaning_room.setObjectName("cleaning_room")
        cleaning_room.resize(1094, 846)
        cleaning_room.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        cleaning_room.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.cleaning_room_Date = QtWidgets.QDateEdit(cleaning_room)
        self.cleaning_room_Date.setGeometry(QtCore.QRect(300, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_Date.setFont(font)
        self.cleaning_room_Date.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_room_Date.setStyleSheet("background-color: rgb(133, 196, 255);")
        self.cleaning_room_Date.setObjectName("cleaning_room_Date")
        self.cleaning_room_Date_L = QtWidgets.QLabel(cleaning_room)
        self.cleaning_room_Date_L.setGeometry(QtCore.QRect(120, 230, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_Date_L.setFont(font)
        self.cleaning_room_Date_L.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cleaning_room_Date_L.setStyleSheet("background-color: rgb(219, 255, 255);")
        self.cleaning_room_Date_L.setFrameShape(QtWidgets.QFrame.Panel)
        self.cleaning_room_Date_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_room_Date_L.setObjectName("cleaning_room_Date_L")
        self.cleaning_room_header_L = QtWidgets.QLabel(cleaning_room)
        self.cleaning_room_header_L.setGeometry(QtCore.QRect(370, 40, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_header_L.setFont(font)
        self.cleaning_room_header_L.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_room_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.cleaning_room_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_room_header_L.setObjectName("cleaning_room_header_L")
        self.cleaning_room_request_PB = QtWidgets.QPushButton(cleaning_room)
        self.cleaning_room_request_PB.setGeometry(QtCore.QRect(360, 700, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_request_PB.setFont(font)
        self.cleaning_room_request_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_room_request_PB.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.cleaning_room_request_PB.setObjectName("cleaning_room_request_PB")
        self.timeEdit = QtWidgets.QTimeEdit(cleaning_room)
        self.timeEdit.setGeometry(QtCore.QRect(777, 230, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.timeEdit.setFont(font)
        self.timeEdit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timeEdit.setStyleSheet("background-color: rgb(133, 196, 255);")
        self.timeEdit.setObjectName("timeEdit")
        self.cleaning_room_Hour_L = QtWidgets.QLabel(cleaning_room)
        self.cleaning_room_Hour_L.setGeometry(QtCore.QRect(600, 230, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_Hour_L.setFont(font)
        self.cleaning_room_Hour_L.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.cleaning_room_Hour_L.setStyleSheet("background-color: rgb(219, 255, 255);")
        self.cleaning_room_Hour_L.setFrameShape(QtWidgets.QFrame.Panel)
        self.cleaning_room_Hour_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_room_Hour_L.setObjectName("cleaning_room_Hour_L")
        self.cleaning_room_id_L = QtWidgets.QLabel(cleaning_room)
        self.cleaning_room_id_L.setGeometry(QtCore.QRect(540, 340, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_id_L.setFont(font)
        self.cleaning_room_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.cleaning_room_id_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.cleaning_room_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_room_id_L.setObjectName("cleaning_room_id_L")
        self.cleaning_room_reservation_Id_LE = QtWidgets.QLineEdit(cleaning_room)
        self.cleaning_room_reservation_Id_LE.setGeometry(QtCore.QRect(270, 410, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_reservation_Id_LE.setFont(font)
        self.cleaning_room_reservation_Id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_room_reservation_Id_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.cleaning_room_reservation_Id_LE.setObjectName("cleaning_room_reservation_Id_LE")
        self.cleaning_room_reservation_Id_L = QtWidgets.QLabel(cleaning_room)
        self.cleaning_room_reservation_Id_L.setGeometry(QtCore.QRect(270, 340, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_reservation_Id_L.setFont(font)
        self.cleaning_room_reservation_Id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.cleaning_room_reservation_Id_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.cleaning_room_reservation_Id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_room_reservation_Id_L.setObjectName("cleaning_room_reservation_Id_L")
        self.cleaning_room_Id_LE = QtWidgets.QLineEdit(cleaning_room)
        self.cleaning_room_Id_LE.setGeometry(QtCore.QRect(540, 410, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_Id_LE.setFont(font)
        self.cleaning_room_Id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_room_Id_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.cleaning_room_Id_LE.setObjectName("cleaning_room_Id_LE")
        self.cleaning_room_Description_L = QtWidgets.QLabel(cleaning_room)
        self.cleaning_room_Description_L.setGeometry(QtCore.QRect(130, 550, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_Description_L.setFont(font)
        self.cleaning_room_Description_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.cleaning_room_Description_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.cleaning_room_Description_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_room_Description_L.setObjectName("cleaning_room_Description_L")
        self.cleaning_room_description_LE = QtWidgets.QLineEdit(cleaning_room)
        self.cleaning_room_description_LE.setGeometry(QtCore.QRect(400, 540, 591, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_room_description_LE.setFont(font)
        self.cleaning_room_description_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_room_description_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.cleaning_room_description_LE.setObjectName("cleaning_room_description_LE")

        self.retranslateUi(cleaning_room)
        QtCore.QMetaObject.connectSlotsByName(cleaning_room)

        # TODO:SEND_REQUEST_CLICKED
        self.cleaning_room_request_PB.clicked.connect(self.send_request)

    def retranslateUi(self, cleaning_room):
        _translate = QtCore.QCoreApplication.translate
        cleaning_room.setWindowTitle(_translate("cleaning_room", "make_cleaning_room"))
        self.cleaning_room_Date_L.setText(_translate("cleaning_room", "Date"))
        self.cleaning_room_header_L.setText(_translate("cleaning_room", "cleanig order"))
        self.cleaning_room_request_PB.setText(_translate("cleaning_room", "Send Request"))
        self.cleaning_room_Hour_L.setText(_translate("cleaning_room", "Hour"))
        self.cleaning_room_id_L.setText(_translate("cleaning_room", "Room Id"))
        self.cleaning_room_reservation_Id_L.setText(_translate("cleaning_room", "Reservation Id"))
        self.cleaning_room_Description_L.setText(_translate("cleaning_room", "Description"))

    def send_request(self):

        if self.catch_booking_status()[0][0] == 2 or self.catch_booking_status()[0][0] == 3:
            reservation_details_id = 0
            if (
                    (self.cleaning_room_reservation_Id_LE.text() != ' ')
                    and
                    (self.cleaning_room_Id_LE.text() != ' ')
            ):
                reservation_details_id = exe_query(f""" 
                                                    SELECT Reservation_Details_ID FROM reservation_details
                                                    WHERE Room_ID = '{int(self.cleaning_room_Id_LE.text())}'
                                                    AND
                                                    Reservation_ID = '{int(self.cleaning_room_reservation_Id_LE.text())}'
                                                  """)

            reservation_details_id = reservation_details_id[0][0]

            year = self.cleaning_room_Date.date().year()
            month = self.cleaning_room_Date.date().month()
            day = self.cleaning_room_Date.date().day()
            date = datetime.datetime(year, month, day).isoformat()

            description = self.cleaning_room_description_LE.text()
            time = self.timeEdit.time().toPyTime()

            exe_query(f"""
                        INSERT INTO cleaning_service 
                                (Cleaning_Service_Time,Cleaning_Service_Date,Cleaning_Service_Description,
                                Staff_ID,Reservation_Details_ID)
                                VALUES
                                 ('{time}','{date}','{description}','{-1}','{reservation_details_id}');
            
                     """)

            # exe_query(f"""
            #             UPDATE reservation SET Reservation_Bill_Total_Amount =
            #             Reservation_Bill_Total_Amount + '10.00'
            #             WHERE Reservation_ID = '{int(self.cleaning_room_reservation_Id_LE.text())}' ;
            #           """)

    def catch_booking_status(self):
        return exe_query(f""" 
                                            SELECT Booking_Status_ID FROM reservation
                                            WHERE
                                            Reservation_ID = '{int(self.cleaning_room_reservation_Id_LE.text())}'
                                          """)
