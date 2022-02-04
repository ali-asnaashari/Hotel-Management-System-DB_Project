from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_cleaning_service_reservation_window(object):

    def __init__(self):
        self.res = []

    def setupUi(self, cleaning_service_reservation_window):
        cleaning_service_reservation_window.setObjectName("cleaning_service_reservation_window")
        cleaning_service_reservation_window.resize(1143, 741)
        cleaning_service_reservation_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        cleaning_service_reservation_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.cleaning_service_Header_L = QtWidgets.QLabel(cleaning_service_reservation_window)
        self.cleaning_service_Header_L.setGeometry(QtCore.QRect(400, 30, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_Header_L.setFont(font)
        self.cleaning_service_Header_L.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_Header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.cleaning_service_Header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_service_Header_L.setObjectName("cleaning_service_Header_L")
        self.cleaning_service_reservation_show_PB = QtWidgets.QPushButton(cleaning_service_reservation_window)
        self.cleaning_service_reservation_show_PB.setGeometry(QtCore.QRect(780, 160, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_reservation_show_PB.setFont(font)
        self.cleaning_service_reservation_show_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_reservation_show_PB.setStyleSheet("background-color: rgb(37, 255, 201);")
        self.cleaning_service_reservation_show_PB.setObjectName("cleaning_service_reservation_show_PB")
        self.cleaning_service_reservation_id_L = QtWidgets.QLabel(cleaning_service_reservation_window)
        self.cleaning_service_reservation_id_L.setGeometry(QtCore.QRect(60, 170, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_reservation_id_L.setFont(font)
        self.cleaning_service_reservation_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.cleaning_service_reservation_id_L.setStyleSheet("background-color: rgb(255, 211, 35);")
        self.cleaning_service_reservation_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_service_reservation_id_L.setObjectName("cleaning_service_reservation_id_L")
        self.cleaning_service_reservation_id_LE = QtWidgets.QLineEdit(cleaning_service_reservation_window)
        self.cleaning_service_reservation_id_LE.setGeometry(QtCore.QRect(390, 170, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_reservation_id_LE.setFont(font)
        self.cleaning_service_reservation_id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_reservation_id_LE.setObjectName("cleaning_service_reservation_id_LE")
        self.cleaning_service_reservation_TableWidget = QtWidgets.QTableWidget(cleaning_service_reservation_window)
        self.cleaning_service_reservation_TableWidget.setGeometry(QtCore.QRect(240, 280, 791, 411))
        self.cleaning_service_reservation_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.cleaning_service_reservation_TableWidget.setStyleSheet("background-color: rgb(225, 212, 255);")
        self.cleaning_service_reservation_TableWidget.setObjectName("cleaning_service_reservation_TableWidget")
        self.cleaning_service_reservation_TableWidget.setColumnCount(5)
        self.cleaning_service_reservation_TableWidget.setRowCount(0)
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
        self.cleaning_service_reservation_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cleaning_service_reservation_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cleaning_service_reservation_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cleaning_service_reservation_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cleaning_service_reservation_TableWidget.setHorizontalHeaderItem(4, item)
        self.cleaning_service_reservation_TableWidget.horizontalHeader().setDefaultSectionSize(155)

        self.retranslateUi(cleaning_service_reservation_window)
        QtCore.QMetaObject.connectSlotsByName(cleaning_service_reservation_window)

        # TODO: SHOW_CLEANING_SERVICE_RESERVATION
        self.cleaning_service_reservation_show_PB.clicked.connect(self.cleaning_service_reservation)

    def retranslateUi(self, cleaning_service_reservation_window):
        _translate = QtCore.QCoreApplication.translate
        cleaning_service_reservation_window.setWindowTitle(_translate("cleaning_service_reservation_window", "cleaning_service_reservation"))
        self.cleaning_service_Header_L.setText(_translate("cleaning_service_reservation_window", "List of Cleaning Services"))
        self.cleaning_service_reservation_show_PB.setText(_translate("cleaning_service_reservation_window", "Show"))
        self.cleaning_service_reservation_id_L.setText(_translate("cleaning_service_reservation_window", "Enter Reservation No. #"))
        item = self.cleaning_service_reservation_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("cleaning_service_reservation_window", "Cleaning No. #"))
        item = self.cleaning_service_reservation_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("cleaning_service_reservation_window", "Time"))
        item = self.cleaning_service_reservation_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("cleaning_service_reservation_window", "Date"))
        item = self.cleaning_service_reservation_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("cleaning_service_reservation_window", "Description"))
        item = self.cleaning_service_reservation_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("cleaning_service_reservation_window", "Staff No. #"))

    def cleaning_service_reservation(self):
        self.res = exe_query(f""" 
                           SELECT Cleaning_Service_ID,Cleaning_Service_Time,Cleaning_Service_Date,
                           Cleaning_Service_Description,cleaning_service.Staff_ID
                           FROM reservation_details
                           JOIN reservation       ON reservation_details.Reservation_ID = reservation.Reservation_ID
                           JOIN cleaning_service  ON reservation_details.Reservation_Details_ID = cleaning_service.Reservation_Details_ID
                           JOIN room              ON room.Room_ID = reservation_details.Room_ID
                           WHERE reservation.Reservation_ID = '{int(self.cleaning_service_reservation_id_LE.text())}';
                        """)

        row = 0
        self.cleaning_service_reservation_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.cleaning_service_reservation_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.cleaning_service_reservation_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.cleaning_service_reservation_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.cleaning_service_reservation_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.cleaning_service_reservation_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))

            row += 1
