from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query, read_user_details


class Ui_list_of_reservation_window(object):

    def setupUi(self, list_of_reservation_window):
        list_of_reservation_window.setObjectName("list_of_reservation_window")
        list_of_reservation_window.resize(1651, 831)
        list_of_reservation_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        list_of_reservation_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.list_of_reservations_L = QtWidgets.QLabel(list_of_reservation_window)
        self.list_of_reservations_L.setGeometry(QtCore.QRect(630, 50, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_of_reservations_L.setFont(font)
        self.list_of_reservations_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.list_of_reservations_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.list_of_reservations_L.setAlignment(QtCore.Qt.AlignCenter)
        self.list_of_reservations_L.setObjectName("list_of_reservations_L")
        self.list_of_reservations_TableWidget = QtWidgets.QTableWidget(list_of_reservation_window)
        self.list_of_reservations_TableWidget.setGeometry(QtCore.QRect(30, 170, 1591, 471))
        self.list_of_reservations_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_of_reservations_TableWidget.setObjectName("list_of_reservations_TableWidget")
        self.list_of_reservations_TableWidget.setColumnCount(10)
        self.list_of_reservations_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(2, item)
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
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_reservations_TableWidget.setHorizontalHeaderItem(9, item)
        self.list_of_reservations_TableWidget.horizontalHeader().setDefaultSectionSize(157)
        self.list_of_reservations_show_PB = QtWidgets.QPushButton(list_of_reservation_window)
        self.list_of_reservations_show_PB.setGeometry(QtCore.QRect(720, 700, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_of_reservations_show_PB.setFont(font)
        self.list_of_reservations_show_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_of_reservations_show_PB.setStyleSheet("background-color: rgb(8, 255, 140);")
        self.list_of_reservations_show_PB.setObjectName("list_of_reservations_show_PB")

        self.retranslateUi(list_of_reservation_window)
        QtCore.QMetaObject.connectSlotsByName(list_of_reservation_window)

        # TODO:LIST_OF_FOOD_ORDER_CLICKED
        self.list_of_reservations_show_PB.clicked.connect(self.show_reservation_in_table)

    def retranslateUi(self, list_of_reservation_window):
        _translate = QtCore.QCoreApplication.translate
        list_of_reservation_window.setWindowTitle(_translate("list_of_reservation_window", "list_of_reservations"))
        self.list_of_reservations_L.setText(_translate("list_of_reservation_window", "List of reservations"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("list_of_reservation_window", " Reservation No. #"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("list_of_reservation_window", "Room No. #"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("list_of_reservation_window", "Price Per Night"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("list_of_reservation_window", "Reservation Date"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("list_of_reservation_window", "CheckIn"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("list_of_reservation_window", "CheckOut"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("list_of_reservation_window", "No. nights"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(7)
        item.setText(_translate("list_of_reservation_window", "Status"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(8)
        item.setText(_translate("list_of_reservation_window", "Total Amount"))
        item = self.list_of_reservations_TableWidget.horizontalHeaderItem(9)
        item.setText(_translate("list_of_reservation_window", "Bill Status"))
        self.list_of_reservations_show_PB.setText(_translate("list_of_reservation_window", "Show List"))

    def show_reservation_in_table(self):
        guest_detail = read_user_details()

        guest_id = int(guest_detail[0])

        res = exe_query(f""" 
                            SELECT rd.Reservation_ID,r.Room_ID,Price_Per_Night,Reservation_Date,Reservation_CheckIn,
                            Reservation_CheckOut,Reservation_no_night,Booking_Status_name,Reservation_Bill_Total_Amount,
                            Reservation_Bill_Status_Paid_Unpaid
                            FROM reservation JOIN reservation_details rd 
                            on reservation.Reservation_ID = rd.Reservation_ID
                            JOIN booking_status bs on bs.Booking_Status_ID = reservation.Booking_Status_ID
                            JOIN room r on r.Room_ID = rd.Room_ID
                            WHERE Guest_ID = '{guest_id}';
                        """)

        row = 0
        self.list_of_reservations_TableWidget.setRowCount(len(res))
        for data in res:
            self.list_of_reservations_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.list_of_reservations_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.list_of_reservations_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.list_of_reservations_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.list_of_reservations_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.list_of_reservations_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))
            self.list_of_reservations_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data[6])))
            self.list_of_reservations_TableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data[7])))
            self.list_of_reservations_TableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data[8])))
            if data[6] == 1:
                self.list_of_reservations_TableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem("PAID"))
            else:
                self.list_of_reservations_TableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem("UNPAID"))

            row += 1
