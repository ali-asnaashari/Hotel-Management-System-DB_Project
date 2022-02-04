from PyQt5 import QtCore, QtGui, QtWidgets
from Start.DB_Configuration import read_user_details, exe_query
from User.Script.Guest_Bill_Total_details import Ui_Total_Billing_details_window


class Ui_Total_Billing_window(object):

    def __init__(self):
        self.guest_id = int(read_user_details()[0])
        self.res = []

    def setupUi(self, Total_Billing_window):
        Total_Billing_window.setObjectName("Total_Billing_window")
        Total_Billing_window.setEnabled(True)
        Total_Billing_window.resize(1094, 846)
        Total_Billing_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Total_Billing_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.Total_Billing_L = QtWidgets.QLabel(Total_Billing_window)
        self.Total_Billing_L.setGeometry(QtCore.QRect(360, 40, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Total_Billing_L.setFont(font)
        self.Total_Billing_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Total_Billing_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.Total_Billing_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Total_Billing_L.setObjectName("Total_Billing_L")
        self.Total_Billing_TableWidget = QtWidgets.QTableWidget(Total_Billing_window)
        self.Total_Billing_TableWidget.setGeometry(QtCore.QRect(220, 160, 721, 481))
        self.Total_Billing_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Total_Billing_TableWidget.setObjectName("Total_Billing_TableWidget")
        self.Total_Billing_TableWidget.setColumnCount(5)
        self.Total_Billing_TableWidget.setRowCount(0)
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
        self.Total_Billing_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_TableWidget.setHorizontalHeaderItem(4, item)
        self.Total_Billing_TableWidget.horizontalHeader().setDefaultSectionSize(138)
        self.Total_Billing_Enter_Reservation_LE = QtWidgets.QLineEdit(Total_Billing_window)
        self.Total_Billing_Enter_Reservation_LE.setGeometry(QtCore.QRect(320, 750, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Total_Billing_Enter_Reservation_LE.setFont(font)
        self.Total_Billing_Enter_Reservation_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Total_Billing_Enter_Reservation_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.Total_Billing_Enter_Reservation_LE.setObjectName("Total_Billing_Enter_Reservation_LE")
        self.Total_Billing_Enter_Reservation_PB = QtWidgets.QPushButton(Total_Billing_window)
        self.Total_Billing_Enter_Reservation_PB.setGeometry(QtCore.QRect(780, 740, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Total_Billing_Enter_Reservation_PB.setFont(font)
        self.Total_Billing_Enter_Reservation_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Total_Billing_Enter_Reservation_PB.setStyleSheet("background-color: rgb(90, 255, 2);")
        self.Total_Billing_Enter_Reservation_PB.setObjectName("Total_Billing_Enter_Reservation_PB")
        self.Total_Billing__Reservation_id_L = QtWidgets.QLabel(Total_Billing_window)
        self.Total_Billing__Reservation_id_L.setGeometry(QtCore.QRect(90, 750, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Total_Billing__Reservation_id_L.setFont(font)
        self.Total_Billing__Reservation_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Total_Billing__Reservation_id_L.setStyleSheet("background-color: rgb(228, 255, 47);")
        self.Total_Billing__Reservation_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Total_Billing__Reservation_id_L.setObjectName("Total_Billing__Reservation_id_L")

        self.retranslateUi(Total_Billing_window)
        QtCore.QMetaObject.connectSlotsByName(Total_Billing_window)

        # TODO:SHOW_LIST_OF_TOTAL_BILLING_CLICKED
        self.show_total_amount()

        # TODO:SHOW_LIST_OF_TOTAL_BILLING_Details_CLICKED
        # if (self.Total_Billing_TableWidget.setRowCount(len(self.res)) is not None) and \
        #         (self.Total_Billing_Enter_Reservation_LE.text() != ' '):
        self.Total_Billing_Enter_Reservation_PB.clicked.connect(self.show_details)

    def retranslateUi(self, Total_Billing_window):
        _translate = QtCore.QCoreApplication.translate
        Total_Billing_window.setWindowTitle(_translate("Total_Billing_window", "bill total"))
        self.Total_Billing_L.setText(_translate("Total_Billing_window", "Total Billing"))
        item = self.Total_Billing_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Total_Billing_window", "Reserv. No. #"))
        item = self.Total_Billing_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Total_Billing_window", "Check in"))
        item = self.Total_Billing_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Total_Billing_window", "Check out"))
        item = self.Total_Billing_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Total_Billing_window", "Total Amount"))
        item = self.Total_Billing_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Total_Billing_window", "Status"))
        self.Total_Billing_Enter_Reservation_PB.setText(_translate("Total_Billing_window", "Show Details"))
        self.Total_Billing__Reservation_id_L.setText(_translate("Total_Billing_window", "Reservation Id"))

    def show_total_amount(self):
        self.res = exe_query(f""" 
                         SELECT Reservation_ID,Reservation_CheckIn,Reservation_CheckOut,Reservation_Bill_Total_Amount,
                                Reservation_Bill_Status_Paid_Unpaid
                          FROM Reservation WHERE Guest_ID = '{self.guest_id}';
                       """)

        row = 0
        self.Total_Billing_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.Total_Billing_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.Total_Billing_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.Total_Billing_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.Total_Billing_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            if data[4] == 1:
                self.Total_Billing_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("PAID"))
            else:
                self.Total_Billing_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("UNPAID"))

            row += 1

    def catch_reservation_id(self):
        f = open("../User/Script/File/Total_Billing_reservation_id.txt", "w")
        f.write(self.Total_Billing_Enter_Reservation_LE.text())
        f.close()

    def show_details(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Total_Billing_details_window()
        self.ui.setupUi(self.window)
        self.window.show()
