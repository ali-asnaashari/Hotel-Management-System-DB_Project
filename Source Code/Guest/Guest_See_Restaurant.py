from PyQt5 import QtCore, QtGui, QtWidgets

from User.DB_Configuration import exe_query
from User.Guest_See_Restaurant_Menu import Ui_See_Rest_Menu_window


class Ui_See_Rest_window(object):

    def setupUi(self, See_Rest_window):
        See_Rest_window.setObjectName("See_Rest_window")
        See_Rest_window.resize(1094, 846)
        See_Rest_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        See_Rest_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.See_Rest_L = QtWidgets.QLabel(See_Rest_window)
        self.See_Rest_L.setGeometry(QtCore.QRect(340, 40, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_L.setFont(font)
        self.See_Rest_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.See_Rest_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_L.setObjectName("See_Rest_L")
        self.See_Rest_B = QtWidgets.QPushButton(See_Rest_window)
        self.See_Rest_B.setGeometry(QtCore.QRect(830, 350, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_B.setFont(font)
        self.See_Rest_B.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_B.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.See_Rest_B.setObjectName("See_Rest_B")
        self.See_Rest_TableWidget = QtWidgets.QTableWidget(See_Rest_window)
        self.See_Rest_TableWidget.setGeometry(QtCore.QRect(350, 160, 411, 481))
        self.See_Rest_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_TableWidget.setObjectName("See_Rest_TableWidget")
        self.See_Rest_TableWidget.setColumnCount(3)
        self.See_Rest_TableWidget.setRowCount(0)
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
        self.See_Rest_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_TableWidget.setHorizontalHeaderItem(2, item)
        self.See_Rest_TableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.See_Rest_Enter_Rest_Id_LE = QtWidgets.QLineEdit(See_Rest_window)
        self.See_Rest_Enter_Rest_Id_LE.setGeometry(QtCore.QRect(390, 770, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Enter_Rest_Id_LE.setFont(font)
        self.See_Rest_Enter_Rest_Id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Enter_Rest_Id_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Enter_Rest_Id_LE.setObjectName("See_Rest_Enter_Rest_Id_LE")
        self.See_Rest__Enter_Id_PB = QtWidgets.QPushButton(See_Rest_window)
        self.See_Rest__Enter_Id_PB.setGeometry(QtCore.QRect(470, 690, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest__Enter_Id_PB.setFont(font)
        self.See_Rest__Enter_Id_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest__Enter_Id_PB.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.See_Rest__Enter_Id_PB.setObjectName("See_Rest__Enter_Id_PB")

        self.retranslateUi(See_Rest_window)
        QtCore.QMetaObject.connectSlotsByName(See_Rest_window)

        # Show_Button_Clicked
        self.See_Rest_B.clicked.connect(self.Show_Restaurant)

        # Enter_Restaurant_Id_Clicked
        self.See_Rest__Enter_Id_PB.clicked.connect(self.Guest_See_Restaurant_Menu_Window)

    def retranslateUi(self, See_Rest_window):
        _translate = QtCore.QCoreApplication.translate
        See_Rest_window.setWindowTitle(_translate("See_Rest_window", "See Restaurant"))
        self.See_Rest_L.setText(_translate("See_Rest_window", "See Restaurant/CoffeeShop"))
        self.See_Rest_B.setText(_translate("See_Rest_window", "Show"))
        item = self.See_Rest_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("See_Rest_window", "Number"))
        item = self.See_Rest_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("See_Rest_window", "Name"))
        item = self.See_Rest_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("See_Rest_window", "Type"))
        self.See_Rest__Enter_Id_PB.setText(_translate("See_Rest_window", "Enter Id"))

    def Show_Restaurant(self):
        res = exe_query(f""" 
                         SELECT Restaurant_CoffeeShop_ID,Restaurant_CoffeeShop_Name,Restaurant_CoffeeShop_Identifier
                          FROM restaurant_coffeeshop
                       """)

        row = 0
        self.See_Rest_TableWidget.setRowCount(len(res))
        for data in res:
            self.See_Rest_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.See_Rest_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            if data[2] == 1:
                self.See_Rest_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem("Cafe"))
            else:
                self.See_Rest_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem("Restaurant"))

            row += 1

    def catch_restaurant_id(self):
        f = open("File/restaurant_id.txt", "w")
        f.write(self.See_Rest_Enter_Rest_Id_LE.text())
        f.close()

    def Guest_See_Restaurant_Menu_Window(self):
        self.catch_restaurant_id()

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_See_Rest_Menu_window()
        self.ui.setupUi(self.window)
        self.window.show()
