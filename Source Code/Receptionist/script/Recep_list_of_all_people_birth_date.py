import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_recep_list_of_all_people_birth_date_window(object):

    def __init__(self):
        self.res = []

    def setupUi(self, recep_list_of_all_people_birth_date_window):
        recep_list_of_all_people_birth_date_window.setObjectName("recep_list_of_all_people_birth_date_window")
        recep_list_of_all_people_birth_date_window.resize(1132, 697)
        recep_list_of_all_people_birth_date_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        recep_list_of_all_people_birth_date_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.recep_list_of_all_people_birth_date_header_L = QtWidgets.QLabel(recep_list_of_all_people_birth_date_window)
        self.recep_list_of_all_people_birth_date_header_L.setGeometry(QtCore.QRect(430, 50, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recep_list_of_all_people_birth_date_header_L.setFont(font)
        self.recep_list_of_all_people_birth_date_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.recep_list_of_all_people_birth_date_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.recep_list_of_all_people_birth_date_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recep_list_of_all_people_birth_date_header_L.setObjectName("recep_list_of_all_people_birth_date_header_L")
        self.recep_list_of_all_people_birth_date_TableWidget = QtWidgets.QTableWidget(recep_list_of_all_people_birth_date_window)
        self.recep_list_of_all_people_birth_date_TableWidget.setGeometry(QtCore.QRect(230, 150, 701, 451))
        self.recep_list_of_all_people_birth_date_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recep_list_of_all_people_birth_date_TableWidget.setStyleSheet("background-color: rgb(225, 212, 255);")
        self.recep_list_of_all_people_birth_date_TableWidget.setObjectName("recep_list_of_all_people_birth_date_TableWidget")
        self.recep_list_of_all_people_birth_date_TableWidget.setColumnCount(5)
        self.recep_list_of_all_people_birth_date_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recep_list_of_all_people_birth_date_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recep_list_of_all_people_birth_date_TableWidget.setHorizontalHeaderItem(1, item)
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
        self.recep_list_of_all_people_birth_date_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recep_list_of_all_people_birth_date_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recep_list_of_all_people_birth_date_TableWidget.setHorizontalHeaderItem(4, item)
        self.recep_list_of_all_people_birth_date_TableWidget.horizontalHeader().setDefaultSectionSize(135)

        self.retranslateUi(recep_list_of_all_people_birth_date_window)
        QtCore.QMetaObject.connectSlotsByName(recep_list_of_all_people_birth_date_window)

        # TODO:SHOW_LIST_OF_ALL_PEOPLE_BIRTHDATE
        self.list_of_all_people()

    def retranslateUi(self, recep_list_of_all_people_birth_date_window):
        _translate = QtCore.QCoreApplication.translate
        recep_list_of_all_people_birth_date_window.setWindowTitle(_translate("recep_list_of_all_people_birth_date_window", "list of people _ birth"))
        self.recep_list_of_all_people_birth_date_header_L.setText(_translate("recep_list_of_all_people_birth_date_window", "List of people"))
        item = self.recep_list_of_all_people_birth_date_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("recep_list_of_all_people_birth_date_window", "First name"))
        item = self.recep_list_of_all_people_birth_date_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("recep_list_of_all_people_birth_date_window", "Last name"))
        item = self.recep_list_of_all_people_birth_date_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("recep_list_of_all_people_birth_date_window", "National ID"))
        item = self.recep_list_of_all_people_birth_date_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("recep_list_of_all_people_birth_date_window", "Gender"))
        item = self.recep_list_of_all_people_birth_date_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("recep_list_of_all_people_birth_date_window", "Birth date"))

    def list_of_all_people(self):

        self.res = exe_query(f""" 
                                SELECT Guest_Firstname,Guest_Lastname,Guest_National_ID,Guest_Gender,Guest_BirthDate
                                FROM reservation JOIN guest ON reservation.Guest_ID = guest.Guest_ID
                                WHERE MONTH(Guest_BirthDate) BETWEEN MONTH (Reservation_CheckIn) AND 
                                MONTH(Reservation_CheckOut) AND
                                DAY(Guest_BirthDate) BETWEEN DAY(Reservation_CheckIn)
                                AND DAY(Reservation_CheckOut)
                                AND Reservation_CheckOut < '{datetime.date.today()}';
                            """)

        print(self.res)

        row = 0
        self.recep_list_of_all_people_birth_date_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.recep_list_of_all_people_birth_date_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.recep_list_of_all_people_birth_date_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.recep_list_of_all_people_birth_date_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            if data[3] == 1:
                self.recep_list_of_all_people_birth_date_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("Men"))
            else:
                self.recep_list_of_all_people_birth_date_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("Female"))
            self.recep_list_of_all_people_birth_date_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))

            row += 1

