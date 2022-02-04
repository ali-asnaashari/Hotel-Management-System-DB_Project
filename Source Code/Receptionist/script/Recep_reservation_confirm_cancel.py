from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query, read_recep_details


class Ui_recept_reservation_CC_window(object):

    def __init__(self):
        self.res = []
        self.confirm_cancel = 1
        self.recep_details = read_recep_details()

    def setupUi(self, recept_reservation_CC_window):
        recept_reservation_CC_window.setObjectName("recept_reservation_CC_window")
        recept_reservation_CC_window.resize(1119, 863)
        recept_reservation_CC_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        recept_reservation_CC_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.recept_reservation_CC_header_L = QtWidgets.QLabel(recept_reservation_CC_window)
        self.recept_reservation_CC_header_L.setGeometry(QtCore.QRect(430, 30, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_header_L.setFont(font)
        self.recept_reservation_CC_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.recept_reservation_CC_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.recept_reservation_CC_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recept_reservation_CC_header_L.setObjectName("recept_reservation_CC_header_L")
        self.recept_reservation_CC_TableWidget = QtWidgets.QTableWidget(recept_reservation_CC_window)
        self.recept_reservation_CC_TableWidget.setGeometry(QtCore.QRect(180, 110, 831, 511))
        self.recept_reservation_CC_TableWidget.viewport().setProperty("cursor",
                                                                      QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_CC_TableWidget.setStyleSheet("background-color: rgb(225, 212, 255);")
        self.recept_reservation_CC_TableWidget.setObjectName("recept_reservation_CC_TableWidget")
        self.recept_reservation_CC_TableWidget.setColumnCount(6)
        self.recept_reservation_CC_TableWidget.setRowCount(0)
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
        self.recept_reservation_CC_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_CC_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_CC_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_CC_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_CC_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_CC_TableWidget.setHorizontalHeaderItem(5, item)
        self.recept_reservation_CC_TableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.recept_reservation_CC_Submit_PB = QtWidgets.QPushButton(recept_reservation_CC_window)
        self.recept_reservation_CC_Submit_PB.setGeometry(QtCore.QRect(740, 790, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_Submit_PB.setFont(font)
        self.recept_reservation_CC_Submit_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_CC_Submit_PB.setStyleSheet("background-color: rgb(8, 255, 140);")
        self.recept_reservation_CC_Submit_PB.setObjectName("recept_reservation_CC_Submit_PB")
        self.recept_reservation_CC_Reservation_LE = QtWidgets.QLineEdit(recept_reservation_CC_window)
        self.recept_reservation_CC_Reservation_LE.setGeometry(QtCore.QRect(360, 760, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_Reservation_LE.setFont(font)
        self.recept_reservation_CC_Reservation_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_CC_Reservation_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.recept_reservation_CC_Reservation_LE.setObjectName("recept_reservation_CC_Reservation_LE")
        self.recept_reservation_CC_Reservation_L = QtWidgets.QLabel(recept_reservation_CC_window)
        self.recept_reservation_CC_Reservation_L.setGeometry(QtCore.QRect(70, 760, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_Reservation_L.setFont(font)
        self.recept_reservation_CC_Reservation_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.recept_reservation_CC_Reservation_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.recept_reservation_CC_Reservation_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recept_reservation_CC_Reservation_L.setObjectName("recept_reservation_CC_Reservation_L")
        self.recept_reservation_CC_confirm_RB = QtWidgets.QRadioButton(recept_reservation_CC_window)
        self.recept_reservation_CC_confirm_RB.setGeometry(QtCore.QRect(820, 650, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_confirm_RB.setFont(font)
        self.recept_reservation_CC_confirm_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_CC_confirm_RB.setStyleSheet("background-color: rgb(2, 27, 255);\n"
                                                            "color: rgb(255, 255, 255);")
        self.recept_reservation_CC_confirm_RB.setObjectName("recept_reservation_CC_confirm_RB")
        self.recept_reservation_CC_cancel_RB = QtWidgets.QRadioButton(recept_reservation_CC_window)
        self.recept_reservation_CC_cancel_RB.setGeometry(QtCore.QRect(820, 720, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_cancel_RB.setFont(font)
        self.recept_reservation_CC_cancel_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_CC_cancel_RB.setStyleSheet("background-color: rgb(2, 27, 255);\n"
                                                           "color: rgb(255, 255, 255);")
        self.recept_reservation_CC_cancel_RB.setObjectName("recept_reservation_CC_cancel_RB")
        self.recept_reservation_CC_serach_guest_id_LE = QtWidgets.QLineEdit(recept_reservation_CC_window)
        self.recept_reservation_CC_serach_guest_id_LE.setGeometry(QtCore.QRect(360, 680, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_serach_guest_id_LE.setFont(font)
        self.recept_reservation_CC_serach_guest_id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_CC_serach_guest_id_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.recept_reservation_CC_serach_guest_id_LE.setObjectName("recept_reservation_CC_serach_guest_id_LE")
        self.recept_reservation_CC_Search_Guest_id_PB = QtWidgets.QPushButton(recept_reservation_CC_window)
        self.recept_reservation_CC_Search_Guest_id_PB.setGeometry(QtCore.QRect(70, 680, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_CC_Search_Guest_id_PB.setFont(font)
        self.recept_reservation_CC_Search_Guest_id_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_CC_Search_Guest_id_PB.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.recept_reservation_CC_Search_Guest_id_PB.setObjectName("recept_reservation_CC_Search_Guest_id_PB")

        self.retranslateUi(recept_reservation_CC_window)
        QtCore.QMetaObject.connectSlotsByName(recept_reservation_CC_window)

        # TODO: Get_Waiting_Reservations
        self.get_waiting_reservations()

        # TODO: SEARCH_BASE_ON_GUEST_ID
        self.recept_reservation_CC_Search_Guest_id_PB.clicked.connect(self.search_base_on_guest_id)

        # TODO: CONFIRM_CANCEL_RESERVATIONS
        self.recept_reservation_CC_Submit_PB.clicked.connect(self.confirm_cancel_reservation)

    def retranslateUi(self, recept_reservation_CC_window):
        _translate = QtCore.QCoreApplication.translate
        recept_reservation_CC_window.setWindowTitle(_translate("recept_reservation_CC_window", "Affirm_Reservations"))
        self.recept_reservation_CC_header_L.setText(_translate("recept_reservation_CC_window", "Affirm  Reservations"))
        item = self.recept_reservation_CC_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("recept_reservation_CC_window", "Reserv No. #"))
        item = self.recept_reservation_CC_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("recept_reservation_CC_window", "Date"))
        item = self.recept_reservation_CC_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("recept_reservation_CC_window", "No nights"))
        item = self.recept_reservation_CC_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("recept_reservation_CC_window", "Check in"))
        item = self.recept_reservation_CC_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("recept_reservation_CC_window", "Check out"))
        item = self.recept_reservation_CC_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("recept_reservation_CC_window", "Guest No."))
        self.recept_reservation_CC_Submit_PB.setText(_translate("recept_reservation_CC_window", "Submit"))
        self.recept_reservation_CC_Reservation_L.setText(
            _translate("recept_reservation_CC_window", "Reservation Number"))
        self.recept_reservation_CC_confirm_RB.setText(_translate("recept_reservation_CC_window", "Confirm"))
        self.recept_reservation_CC_cancel_RB.setText(_translate("recept_reservation_CC_window", "Cancel"))
        self.recept_reservation_CC_Search_Guest_id_PB.setText(
            _translate("recept_reservation_CC_window", "Search Base on Guest Id"))

    def get_waiting_reservations(self):
        self.res = exe_query(f""" 
                            SELECT Reservation_ID,Reservation_Date,Reservation_no_night,
                            Reservation_CheckIn,Reservation_CheckOut,Guest_ID FROM reservation
                            WHERE Booking_Status_ID = '{1}' ORDER BY Reservation_Date;
                        """)

        row = 0
        self.recept_reservation_CC_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.recept_reservation_CC_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.recept_reservation_CC_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.recept_reservation_CC_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.recept_reservation_CC_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.recept_reservation_CC_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.recept_reservation_CC_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))

            row += 1

    def search_base_on_guest_id(self):
        self.res = exe_query(f""" 
                            SELECT Reservation_ID,Reservation_Date,Reservation_no_night,
                            Reservation_CheckIn,Reservation_CheckOut,Guest_ID FROM reservation
                            WHERE Booking_Status_ID = '{1}' AND 
                            Guest_ID = '{self.recept_reservation_CC_serach_guest_id_LE.text()}'
                             ORDER BY Reservation_Date;
                        """)

        row = 0
        self.recept_reservation_CC_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.recept_reservation_CC_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.recept_reservation_CC_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.recept_reservation_CC_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.recept_reservation_CC_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.recept_reservation_CC_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.recept_reservation_CC_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))

            row += 1

    def confirm_cancel_reservation(self):

        if self.recept_reservation_CC_confirm_RB.isChecked():
            self.confirm_cancel = 2

        elif self.recept_reservation_CC_cancel_RB.isChecked():
            self.confirm_cancel = 5

        self.res = exe_query(f""" 
                                UPDATE reservation SET 
                                Booking_Status_ID = '{self.confirm_cancel}',
                                Staff_ID = '{int(self.recep_details[0])}'
                                WHERE Reservation_ID = '{int(self.recept_reservation_CC_Reservation_LE.text())}';
                        """)

        if self.confirm_cancel == 2:
            self.res = exe_query(f""" 
                                    UPDATE reservation JOIN reservation_details rd on reservation.Reservation_ID = rd.Reservation_ID
                                    JOIN room r on r.Room_ID = rd.Room_ID SET
                                    Reservation.Reservation_Bill_Total_Amount = Reservation_Bill_Total_Amount + 
                                    Reservation_no_night * Price_Per_Night
                                    where reservation.Reservation_ID = 
                                    '{int(self.recept_reservation_CC_Reservation_LE.text())}';
                            """)


