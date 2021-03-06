from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_recept_reservation_list_window(object):

    def __init__(self):
        self.res = []

    def setupUi(self, recept_reservation_list_window):
        recept_reservation_list_window.setObjectName("recept_reservation_list_window")
        recept_reservation_list_window.resize(1838, 863)
        recept_reservation_list_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        recept_reservation_list_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.recept_reservation_list_header_L = QtWidgets.QLabel(recept_reservation_list_window)
        self.recept_reservation_list_header_L.setGeometry(QtCore.QRect(730, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_reservation_list_header_L.setFont(font)
        self.recept_reservation_list_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.recept_reservation_list_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.recept_reservation_list_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recept_reservation_list_header_L.setObjectName("recept_reservation_list_header_L")
        self.recept_reservation_list_TableWidget = QtWidgets.QTableWidget(recept_reservation_list_window)
        self.recept_reservation_list_TableWidget.setGeometry(QtCore.QRect(120, 110, 1641, 511))
        self.recept_reservation_list_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_reservation_list_TableWidget.setStyleSheet("background-color: rgb(225, 212, 255);")
        self.recept_reservation_list_TableWidget.setObjectName("recept_reservation_list_TableWidget")
        self.recept_reservation_list_TableWidget.setColumnCount(12)
        self.recept_reservation_list_TableWidget.setRowCount(0)
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
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_reservation_list_TableWidget.setHorizontalHeaderItem(11, item)
        self.recept_reservation_list_TableWidget.horizontalHeader().setDefaultSectionSize(135)

        self.retranslateUi(recept_reservation_list_window)
        QtCore.QMetaObject.connectSlotsByName(recept_reservation_list_window)

        # TODO: Fill_Table_Reservation_Automatically_Clicked
        self.fill_table_reservation()

    def retranslateUi(self, recept_reservation_list_window):
        _translate = QtCore.QCoreApplication.translate
        recept_reservation_list_window.setWindowTitle(_translate("recept_reservation_list_window", "list_of_all_reservations"))
        self.recept_reservation_list_header_L.setText(_translate("recept_reservation_list_window", "List of All Reservations"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("recept_reservation_list_window", "Reserv No. #"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("recept_reservation_list_window", "Date"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("recept_reservation_list_window", "No nights"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("recept_reservation_list_window", "Check in"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("recept_reservation_list_window", "Check out"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("recept_reservation_list_window", "First name"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("recept_reservation_list_window", "Last name"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(7)
        item.setText(_translate("recept_reservation_list_window", "National Id"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(8)
        item.setText(_translate("recept_reservation_list_window", "Phone number"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(9)
        item.setText(_translate("recept_reservation_list_window", "Address"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(10)
        item.setText(_translate("recept_reservation_list_window", "Birth date"))
        item = self.recept_reservation_list_TableWidget.horizontalHeaderItem(11)
        item.setText(_translate("recept_reservation_list_window", "Gender"))

    def fill_table_reservation(self):

        self.res = exe_query(f""" 
                                SELECT Reservation_ID,Reservation_Date,Reservation_no_night,Reservation_CheckIn,
                                Reservation_CheckOut,Guest_Firstname,Guest_Lastname,Guest_National_ID,Guest_PhoneNumber,
                                Guest_Address,Guest_BirthDate,Guest_Gender  FROM
                                guest JOIN reservation  ON guest.Guest_ID = reservation.Guest_ID;
                        """)

        row = 0
        self.recept_reservation_list_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.recept_reservation_list_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.recept_reservation_list_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.recept_reservation_list_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.recept_reservation_list_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.recept_reservation_list_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.recept_reservation_list_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))
            self.recept_reservation_list_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data[6])))
            self.recept_reservation_list_TableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data[7])))
            self.recept_reservation_list_TableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data[8])))
            self.recept_reservation_list_TableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(data[9])))
            self.recept_reservation_list_TableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(data[10])))
            if data[11] == 1:
                self.recept_reservation_list_TableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem("Men"))
            else:
                self.recept_reservation_list_TableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem("Female"))

            row += 1


