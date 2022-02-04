from PyQt5 import QtCore, QtGui, QtWidgets
from Start.DB_Configuration import read_user_details, exe_query


class Ui_list_food_window(object):

    def setupUi(self, list_food_window):
        list_food_window.setObjectName("list_food_window")
        list_food_window.resize(1183, 840)
        list_food_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        list_food_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.list_food_L = QtWidgets.QLabel(list_food_window)
        self.list_food_L.setGeometry(QtCore.QRect(360, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_food_L.setFont(font)
        self.list_food_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.list_food_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.list_food_L.setAlignment(QtCore.Qt.AlignCenter)
        self.list_food_L.setObjectName("list_food_L")
        self.list_food_TableWidget = QtWidgets.QTableWidget(list_food_window)
        self.list_food_TableWidget.setGeometry(QtCore.QRect(30, 120, 1081, 511))
        self.list_food_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_food_TableWidget.setObjectName("list_food_TableWidget")
        self.list_food_TableWidget.setColumnCount(7)
        self.list_food_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_food_TableWidget.setHorizontalHeaderItem(0, item)
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
        self.list_food_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_food_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_food_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_food_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_food_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_food_TableWidget.setHorizontalHeaderItem(6, item)
        self.list_food_TableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.list_food_show_PB = QtWidgets.QPushButton(list_food_window)
        self.list_food_show_PB.setGeometry(QtCore.QRect(470, 690, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_food_show_PB.setFont(font)
        self.list_food_show_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_food_show_PB.setStyleSheet("background-color: rgb(8, 255, 140);")
        self.list_food_show_PB.setObjectName("list_food_show_PB")

        self.retranslateUi(list_food_window)
        QtCore.QMetaObject.connectSlotsByName(list_food_window)

        # TODO:LIST_OF_FOOD_ORDER_CLICKED
        self.list_food_show_PB.clicked.connect(self.show_food_order_in_table)

    def retranslateUi(self, list_food_window):
        _translate = QtCore.QCoreApplication.translate
        list_food_window.setWindowTitle(_translate("list_food_window", "List of Food Order"))
        self.list_food_L.setText(_translate("list_food_window", "List of Food Orders"))
        item = self.list_food_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("list_food_window", "Order No. #"))
        item = self.list_food_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("list_food_window", "Restaurant name"))
        item = self.list_food_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("list_food_window", "Food name"))
        item = self.list_food_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("list_food_window", "Food Price"))
        item = self.list_food_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("list_food_window", "Reservation Id"))
        item = self.list_food_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("list_food_window", "Room Id"))
        item = self.list_food_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("list_food_window", "Served in"))
        self.list_food_show_PB.setText(_translate("list_food_window", "Show List"))

    def show_food_order_in_table(self):
        guest_detail = read_user_details()

        guest_id = int(guest_detail[0])

        res = exe_query(f""" 
                        SELECT fo.Food_Order_ID,Restaurant_CoffeeShop_Name,Food_Name,Food_Price,
                                rd.Reservation_ID,Room_ID,Food_Order_Room_Rest
                               FROM food JOIN restaurant_coffeeshop rc on 
                                food.Restaurant_CoffeeShop_ID = rc.Restaurant_CoffeeShop_ID
                               JOIN food_contains fc on food.Food_ID = fc.Food_ID JOIN 
                               food_order fo on fo.Food_Order_ID = fc.Food_Order_ID
                               JOIN reservation_details rd on fo.Reservation_Details_ID = rd.Reservation_Details_ID
                               JOIN reservation r on rd.Reservation_ID = r.Reservation_ID
                               WHERE Guest_ID = '{guest_id}';
                        """)

        row = 0
        self.list_food_TableWidget.setRowCount(len(res))
        for data in res:
            self.list_food_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.list_food_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.list_food_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.list_food_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.list_food_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.list_food_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))
            if data[6] == 1:
                self.list_food_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem("Room"))
            else:
                self.list_food_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem("Restaurant"))

            row += 1

