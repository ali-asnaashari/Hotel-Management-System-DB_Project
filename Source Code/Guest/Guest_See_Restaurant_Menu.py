from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_See_Rest_Menu_window(object):
    def setupUi(self, See_Rest_Menu_window):
        See_Rest_Menu_window.setObjectName("See_Rest_Menu_window")
        See_Rest_Menu_window.resize(1094, 846)
        See_Rest_Menu_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        See_Rest_Menu_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.See_Rest_Menu_L = QtWidgets.QLabel(See_Rest_Menu_window)
        self.See_Rest_Menu_L.setGeometry(QtCore.QRect(200, 40, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_L.setFont(font)
        self.See_Rest_Menu_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.See_Rest_Menu_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_L.setObjectName("See_Rest_Menu_L")
        self.See_Rest_Menu_TableWidget = QtWidgets.QTableWidget(See_Rest_Menu_window)
        self.See_Rest_Menu_TableWidget.setGeometry(QtCore.QRect(130, 140, 511, 511))
        self.See_Rest_Menu_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_TableWidget.setObjectName("See_Rest_Menu_TableWidget")
        self.See_Rest_Menu_TableWidget.setColumnCount(4)
        self.See_Rest_Menu_TableWidget.setRowCount(0)
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
        self.See_Rest_Menu_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_Menu_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_Menu_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_Menu_TableWidget.setHorizontalHeaderItem(3, item)
        self.See_Rest_Menu_Enter_Food_LE = QtWidgets.QLineEdit(See_Rest_Menu_window)
        self.See_Rest_Menu_Enter_Food_LE.setGeometry(QtCore.QRect(210, 760, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Enter_Food_LE.setFont(font)
        self.See_Rest_Menu_Enter_Food_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Enter_Food_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Enter_Food_LE.setObjectName("See_Rest_Menu_Enter_Food_LE")
        self.See_Rest_Menu_Search_PB = QtWidgets.QPushButton(See_Rest_Menu_window)
        self.See_Rest_Menu_Search_PB.setGeometry(QtCore.QRect(260, 680, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Search_PB.setFont(font)
        self.See_Rest_Menu_Search_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Search_PB.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.See_Rest_Menu_Search_PB.setObjectName("See_Rest_Menu_Search_PB")
        self.See_Rest_Menu_Room_RB = QtWidgets.QRadioButton(See_Rest_Menu_window)
        self.See_Rest_Menu_Room_RB.setGeometry(QtCore.QRect(830, 210, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Room_RB.setFont(font)
        self.See_Rest_Menu_Room_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Room_RB.setStyleSheet("background-color: rgb(151, 215, 255);")
        self.See_Rest_Menu_Room_RB.setObjectName("See_Rest_Menu_Room_RB")
        self.See_Rest_Menu_Rest_RB = QtWidgets.QRadioButton(See_Rest_Menu_window)
        self.See_Rest_Menu_Rest_RB.setGeometry(QtCore.QRect(830, 280, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Rest_RB.setFont(font)
        self.See_Rest_Menu_Rest_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Rest_RB.setStyleSheet("background-color: rgb(151, 215, 255);")
        self.See_Rest_Menu_Rest_RB.setObjectName("See_Rest_Menu_Rest_RB")
        self.See_Rest_Menu_where_L = QtWidgets.QLabel(See_Rest_Menu_window)
        self.See_Rest_Menu_where_L.setGeometry(QtCore.QRect(800, 140, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_where_L.setFont(font)
        self.See_Rest_Menu_where_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_where_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.See_Rest_Menu_where_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_where_L.setObjectName("See_Rest_Menu_where_L")
        self.See_Rest_Menu_Reservation_Id_L = QtWidgets.QLabel(See_Rest_Menu_window)
        self.See_Rest_Menu_Reservation_Id_L.setGeometry(QtCore.QRect(800, 380, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Reservation_Id_L.setFont(font)
        self.See_Rest_Menu_Reservation_Id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_Reservation_Id_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.See_Rest_Menu_Reservation_Id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_Reservation_Id_L.setObjectName("See_Rest_Menu_Reservation_Id_L")
        self.See_Rest_Menu_Room_id_L = QtWidgets.QLabel(See_Rest_Menu_window)
        self.See_Rest_Menu_Room_id_L.setGeometry(QtCore.QRect(800, 570, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Room_id_L.setFont(font)
        self.See_Rest_Menu_Room_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_Room_id_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.See_Rest_Menu_Room_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_Room_id_L.setObjectName("See_Rest_Menu_Room_id_L")
        self.See_Rest_Menu_Reservation_Id_LE = QtWidgets.QLineEdit(See_Rest_Menu_window)
        self.See_Rest_Menu_Reservation_Id_LE.setGeometry(QtCore.QRect(800, 450, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Reservation_Id_LE.setFont(font)
        self.See_Rest_Menu_Reservation_Id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Reservation_Id_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Reservation_Id_LE.setObjectName("See_Rest_Menu_Reservation_Id_LE")
        self.See_Rest_Menu_Room_Id_LE = QtWidgets.QLineEdit(See_Rest_Menu_window)
        self.See_Rest_Menu_Room_Id_LE.setGeometry(QtCore.QRect(800, 640, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Room_Id_LE.setFont(font)
        self.See_Rest_Menu_Room_Id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Room_Id_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Room_Id_LE.setObjectName("See_Rest_Menu_Room_Id_LE")
        self.See_Rest_Menu_Submit_PB = QtWidgets.QPushButton(See_Rest_Menu_window)
        self.See_Rest_Menu_Submit_PB.setGeometry(QtCore.QRect(810, 750, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Submit_PB.setFont(font)
        self.See_Rest_Menu_Submit_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Submit_PB.setStyleSheet("background-color: rgb(8, 255, 140);")
        self.See_Rest_Menu_Submit_PB.setObjectName("See_Rest_Menu_Submit_PB")

        self.retranslateUi(See_Rest_Menu_window)
        QtCore.QMetaObject.connectSlotsByName(See_Rest_Menu_window)

    def retranslateUi(self, See_Rest_Menu_window):
        _translate = QtCore.QCoreApplication.translate
        See_Rest_Menu_window.setWindowTitle(_translate("See_Rest_Menu_window", "Free Rooms"))
        self.See_Rest_Menu_L.setText(_translate("See_Rest_Menu_window", "See Restaurant/CoffeeShop Menu"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("See_Rest_Menu_window", "Food Id"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("See_Rest_Menu_window", "Food name"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("See_Rest_Menu_window", "Ingredients"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("See_Rest_Menu_window", "Type"))
        self.See_Rest_Menu_Search_PB.setText(_translate("See_Rest_Menu_window", "Search Food/Drink"))
        self.See_Rest_Menu_Room_RB.setText(_translate("See_Rest_Menu_window", "Room"))
        self.See_Rest_Menu_Rest_RB.setText(_translate("See_Rest_Menu_window", "Restaurant/Coffee"))
        self.See_Rest_Menu_where_L.setText(_translate("See_Rest_Menu_window", "Where Do You Eat ?"))
        self.See_Rest_Menu_Reservation_Id_L.setText(_translate("See_Rest_Menu_window", "Reservation Id"))
        self.See_Rest_Menu_Room_id_L.setText(_translate("See_Rest_Menu_window", "Room Id"))
        self.See_Rest_Menu_Submit_PB.setText(_translate("See_Rest_Menu_window", "Submit"))
