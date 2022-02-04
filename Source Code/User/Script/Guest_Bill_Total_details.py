from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query, read_user_details


class Ui_Total_Billing_details_window(object):

    def __init__(self):
        self.guest_id = int(read_user_details()[0])

    def setupUi(self, Total_Billing_details_window):
        Total_Billing_details_window.setObjectName("Total_Billing_details_window")
        Total_Billing_details_window.setEnabled(True)
        Total_Billing_details_window.resize(1429, 846)
        Total_Billing_details_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Total_Billing_details_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.Total_Billing_details_L = QtWidgets.QLabel(Total_Billing_details_window)
        self.Total_Billing_details_L.setGeometry(QtCore.QRect(540, 50, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Total_Billing_details_L.setFont(font)
        self.Total_Billing_details_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Total_Billing_details_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.Total_Billing_details_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Total_Billing_details_L.setObjectName("Total_Billing_details_L")
        self.Total_Billing_details_TableWidget = QtWidgets.QTableWidget(Total_Billing_details_window)
        self.Total_Billing_details_TableWidget.setGeometry(QtCore.QRect(100, 160, 1271, 481))
        self.Total_Billing_details_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Total_Billing_details_TableWidget.setObjectName("Total_Billing_details_TableWidget")
        self.Total_Billing_details_TableWidget.setColumnCount(9)
        self.Total_Billing_details_TableWidget.setRowCount(0)
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
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Total_Billing_details_TableWidget.setHorizontalHeaderItem(8, item)
        self.Total_Billing_details_TableWidget.horizontalHeader().setDefaultSectionSize(138)

        self.retranslateUi(Total_Billing_details_window)
        QtCore.QMetaObject.connectSlotsByName(Total_Billing_details_window)

        # TODO:SHOW_LIST_OF_TOTAL_BILLING_Details
        self.show_total_amount_details()

    def retranslateUi(self, Total_Billing_details_window):
        _translate = QtCore.QCoreApplication.translate
        Total_Billing_details_window.setWindowTitle(_translate("Total_Billing_details_window", "bill total details"))
        self.Total_Billing_details_L.setText(_translate("Total_Billing_details_window", "Total Billing Details"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Total_Billing_details_window", "Room No. #"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Total_Billing_details_window", "Room Price"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Total_Billing_details_window", "Extra Facilities"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Total_Billing_details_window", "Rest Name"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Total_Billing_details_window", "Food name"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Total_Billing_details_window", "Food price"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Total_Billing_details_window", "Cleaning No."))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Total_Billing_details_window", "Cleaning Date"))
        item = self.Total_Billing_details_TableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Total_Billing_details_window", "Cleaning price"))

    def show_total_amount_details(self):

        res = exe_query(f""" 
                          SELECT r.Room_ID,Price_Per_Night,Reservation_Details_Extra_Facilities,
                          Restaurant_CoffeeShop_Name,Food_Name,Food_Price,Cleaning_Service_ID,Cleaning_Service_Date
                          FROM reservation JOIN reservation_details rd on reservation.Reservation_ID = rd.Reservation_ID
                          JOIN room r on r.Room_ID = rd.Room_ID
                          LEFT OUTER JOIN food_order fo on rd.Reservation_Details_ID = fo.Reservation_Details_ID
                          JOIN food_contains fc on fo.Food_Order_ID = fc.Food_Order_ID
                          JOIN food f on f.Food_ID = fc.Food_ID
                          JOIN restaurant_coffeeshop rc on f.Restaurant_CoffeeShop_ID = rc.Restaurant_CoffeeShop_ID
                          LEFT OUTER JOIN cleaning_service cs on rd.Reservation_Details_ID = cs.Reservation_Details_ID
                          WHERE Guest_ID = '{self.guest_id}';
                       """)

        print(res)

        row = 0
        self.Total_Billing_details_TableWidget.setRowCount(len(res))
        for data in res:
            self.Total_Billing_details_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.Total_Billing_details_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.Total_Billing_details_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.Total_Billing_details_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.Total_Billing_details_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.Total_Billing_details_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))
            self.Total_Billing_details_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data[6])))
            self.Total_Billing_details_TableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data[7])))
            if data[6] != None:
                self.Total_Billing_details_TableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem("10000"))
            else:
                self.Total_Billing_details_TableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem("-"))

            row += 1
