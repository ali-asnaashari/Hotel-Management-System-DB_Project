from PyQt5 import QtCore, QtGui, QtWidgets
import csv

from User.Guest_See_Empty_Rooms import Ui_FreeRooms

detail = []


def read_name_family():
    with open("GuestDetails.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            detail.append(row[1])
            detail.append(row[2])
            break

    return detail


class Ui_GuestWelcomePage(object):
    read_name_family()

    def setupUi(self, GuestWelcomePage):
        GuestWelcomePage.setObjectName("GuestWelcomePage")
        GuestWelcomePage.resize(1122, 842)
        self.WelcomePage_TotalBilling_B = QtWidgets.QPushButton(GuestWelcomePage)
        self.WelcomePage_TotalBilling_B.setGeometry(QtCore.QRect(630, 470, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_TotalBilling_B.setFont(font)
        self.WelcomePage_TotalBilling_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_TotalBilling_B.setStyleSheet("background-color: rgb(192, 230, 255);")
        self.WelcomePage_TotalBilling_B.setObjectName("WelcomePage_TotalBilling_B")
        self.WelcomePage_FoodOrders_B = QtWidgets.QPushButton(GuestWelcomePage)
        self.WelcomePage_FoodOrders_B.setGeometry(QtCore.QRect(630, 230, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_FoodOrders_B.setFont(font)
        self.WelcomePage_FoodOrders_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_FoodOrders_B.setStyleSheet("background-color: rgb(192, 230, 255);")
        self.WelcomePage_FoodOrders_B.setObjectName("WelcomePage_FoodOrders_B")
        self.WelcomePage_FreeRoom_B = QtWidgets.QPushButton(GuestWelcomePage)
        self.WelcomePage_FreeRoom_B.setGeometry(QtCore.QRect(300, 230, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_FreeRoom_B.setFont(font)
        self.WelcomePage_FreeRoom_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_FreeRoom_B.setStyleSheet("background-color: rgb(192, 230, 255);")
        self.WelcomePage_FreeRoom_B.setObjectName("WelcomePage_FreeRoom_B")
        self.WelcomePage_SeeRestaurant_B = QtWidgets.QPushButton(GuestWelcomePage)
        self.WelcomePage_SeeRestaurant_B.setGeometry(QtCore.QRect(300, 350, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_SeeRestaurant_B.setFont(font)
        self.WelcomePage_SeeRestaurant_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_SeeRestaurant_B.setStyleSheet("background-color: rgb(192, 230, 255);")
        self.WelcomePage_SeeRestaurant_B.setObjectName("WelcomePage_SeeRestaurant_B")
        self.WelcomePage_ListReservatons_B = QtWidgets.QPushButton(GuestWelcomePage)
        self.WelcomePage_ListReservatons_B.setGeometry(QtCore.QRect(300, 470, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_ListReservatons_B.setFont(font)
        self.WelcomePage_ListReservatons_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_ListReservatons_B.setStyleSheet("background-color: rgb(192, 230, 255);")
        self.WelcomePage_ListReservatons_B.setObjectName("WelcomePage_ListReservatons_B")
        self.WelcomePage_CleaingOrder_B = QtWidgets.QPushButton(GuestWelcomePage)
        self.WelcomePage_CleaingOrder_B.setGeometry(QtCore.QRect(630, 350, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_CleaingOrder_B.setFont(font)
        self.WelcomePage_CleaingOrder_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_CleaingOrder_B.setStyleSheet("background-color: rgb(192, 230, 255);")
        self.WelcomePage_CleaingOrder_B.setObjectName("WelcomePage_CleaingOrder_B")
        self.WelcomePage_Enter_L = QtWidgets.QLabel(GuestWelcomePage)
        self.WelcomePage_Enter_L.setGeometry(QtCore.QRect(350, 70, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Enter_L.setFont(font)
        self.WelcomePage_Enter_L.setStyleSheet("background-color: rgb(201, 204, 255);")
        self.WelcomePage_Enter_L.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomePage_Enter_L.setObjectName("WelcomePage_Enter_L")
        self.WelcomePage_TotalBilling_B_2 = QtWidgets.QPushButton(GuestWelcomePage)
        self.WelcomePage_TotalBilling_B_2.setGeometry(QtCore.QRect(430, 610, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_TotalBilling_B_2.setFont(font)
        self.WelcomePage_TotalBilling_B_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_TotalBilling_B_2.setStyleSheet("background-color: rgb(255, 101, 103);")
        self.WelcomePage_TotalBilling_B_2.setObjectName("WelcomePage_TotalBilling_B_2")

        self.retranslateUi(GuestWelcomePage)
        QtCore.QMetaObject.connectSlotsByName(GuestWelcomePage)

        # See_Empty_Rooms_Clicked
        self.WelcomePage_FreeRoom_B.clicked.connect(self.Guest_See_Empty_Room_Window)

    def retranslateUi(self, GuestWelcomePage):
        _translate = QtCore.QCoreApplication.translate
        GuestWelcomePage.setWindowTitle(_translate("GuestWelcomePage", "Guest Dashboard"))
        self.WelcomePage_TotalBilling_B.setText(_translate("GuestWelcomePage", "Total Billing"))
        self.WelcomePage_FoodOrders_B.setText(_translate("GuestWelcomePage", "List Food Orders"))
        self.WelcomePage_FreeRoom_B.setText(_translate("GuestWelcomePage", "Free Rooms"))
        self.WelcomePage_SeeRestaurant_B.setText(_translate("GuestWelcomePage", "See Restaurants"))
        self.WelcomePage_ListReservatons_B.setText(_translate("GuestWelcomePage", "List Of Reservations"))
        self.WelcomePage_CleaingOrder_B.setText(_translate("GuestWelcomePage", "Make Cleaning Order"))
        self.WelcomePage_Enter_L.setText(_translate("GuestWelcomePage", "Welcome " + detail[0] + " " + detail[1] +
                                                    " to Home Page"))

        self.WelcomePage_TotalBilling_B_2.setText(_translate("GuestWelcomePage", "Exit"))

    def Guest_See_Empty_Room_Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FreeRooms()
        self.ui.setupUi(self.window)
        self.window.show()