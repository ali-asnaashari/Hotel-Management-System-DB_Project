from PyQt5 import QtCore, QtGui, QtWidgets
from Start.DB_Configuration import exe_query, read_rest_cafe_id, read_Food_ids


class Ui_See_Rest_Menu_window(object):

    def __init__(self):
        self.rest_cafe_id = read_rest_cafe_id()

    def setupUi(self, See_Rest_Menu_window):
        See_Rest_Menu_window.setObjectName("See_Rest_Menu_window")
        See_Rest_Menu_window.resize(1119, 863)
        See_Rest_Menu_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        See_Rest_Menu_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.See_Rest_Menu_L = QtWidgets.QLabel(See_Rest_Menu_window)
        self.See_Rest_Menu_L.setGeometry(QtCore.QRect(200, 20, 401, 51))
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
        self.See_Rest_Menu_TableWidget.setGeometry(QtCore.QRect(50, 110, 701, 511))
        self.See_Rest_Menu_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_TableWidget.setObjectName("See_Rest_Menu_TableWidget")
        self.See_Rest_Menu_TableWidget.setColumnCount(5)
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
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_Menu_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_Menu_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.See_Rest_Menu_TableWidget.setHorizontalHeaderItem(4, item)
        self.See_Rest_Menu_TableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.See_Rest_Menu_Enter_Food_LE = QtWidgets.QLineEdit(See_Rest_Menu_window)
        self.See_Rest_Menu_Enter_Food_LE.setGeometry(QtCore.QRect(30, 730, 321, 41))
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
        self.See_Rest_Menu_Search_PB.setGeometry(QtCore.QRect(70, 650, 261, 51))
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
        self.See_Rest_Menu_Room_RB.setGeometry(QtCore.QRect(840, 180, 191, 51))
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
        self.See_Rest_Menu_Rest_RB.setGeometry(QtCore.QRect(840, 250, 191, 51))
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
        self.See_Rest_Menu_where_L.setGeometry(QtCore.QRect(810, 110, 231, 51))
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
        self.See_Rest_Menu_Reservation_Id_L.setGeometry(QtCore.QRect(810, 320, 231, 51))
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
        self.See_Rest_Menu_Room_id_L.setGeometry(QtCore.QRect(810, 480, 231, 51))
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
        self.See_Rest_Menu_Reservation_Id_LE.setGeometry(QtCore.QRect(810, 390, 231, 71))
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
        self.See_Rest_Menu_Room_Id_LE.setGeometry(QtCore.QRect(810, 550, 231, 71))
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
        self.See_Rest_Menu_Submit_PB.setGeometry(QtCore.QRect(480, 790, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Submit_PB.setFont(font)
        self.See_Rest_Menu_Submit_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Submit_PB.setStyleSheet("background-color: rgb(8, 255, 140);")
        self.See_Rest_Menu_Submit_PB.setObjectName("See_Rest_Menu_Submit_PB")
        self.See_Rest_Menu_Search_Price_PB = QtWidgets.QPushButton(See_Rest_Menu_window)
        self.See_Rest_Menu_Search_Price_PB.setGeometry(QtCore.QRect(420, 650, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Search_Price_PB.setFont(font)
        self.See_Rest_Menu_Search_Price_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Search_Price_PB.setStyleSheet("background-color: rgb(208, 209, 255);")
        self.See_Rest_Menu_Search_Price_PB.setObjectName("See_Rest_Menu_Search_Price_PB")
        self.See_Rest_Menu_Enter_Price_LE = QtWidgets.QLineEdit(See_Rest_Menu_window)
        self.See_Rest_Menu_Enter_Price_LE.setGeometry(QtCore.QRect(420, 730, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Enter_Price_LE.setFont(font)
        self.See_Rest_Menu_Enter_Price_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Enter_Price_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Enter_Price_LE.setObjectName("See_Rest_Menu_Enter_Price_LE")
        self.See_Rest_Menu_Food_Ids_LE = QtWidgets.QLineEdit(See_Rest_Menu_window)
        self.See_Rest_Menu_Food_Ids_LE.setGeometry(QtCore.QRect(780, 730, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_Ids_LE.setFont(font)
        self.See_Rest_Menu_Food_Ids_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Food_Ids_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Food_Ids_LE.setObjectName("See_Rest_Menu_Food_Ids_LE")
        self.See_Rest_Menu_Food_Ids_L = QtWidgets.QLabel(See_Rest_Menu_window)
        self.See_Rest_Menu_Food_Ids_L.setGeometry(QtCore.QRect(820, 650, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_Ids_L.setFont(font)
        self.See_Rest_Menu_Food_Ids_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_Food_Ids_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.See_Rest_Menu_Food_Ids_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_Food_Ids_L.setObjectName("See_Rest_Menu_Food_Ids_L")

        self.retranslateUi(See_Rest_Menu_window)
        QtCore.QMetaObject.connectSlotsByName(See_Rest_Menu_window)

        # TODO:SHOW_RESTAURANT_MENU -> RUNS
        self.Show_Restaurant_Menu()

        # TODO:CLICKED_SEARCH_BUTTON_FOR_SHOW_SPECIAL_FOOD -> RUNS
        self.See_Rest_Menu_Search_PB.clicked.connect(self.search_special_food_drink)

        # TODO:CLICKED_SEARCH_BUTTON_FOR_SHOW_SPECIAL_FOOD_BASE_ON_MAXIMUM_PRICE -> RUNS
        self.See_Rest_Menu_Search_Price_PB.clicked.connect(self.search_base_on_maximum_price)

        # TODO:CLICKED_SUBMIT_BUTTON_FOR_SAVE_DATA_IN DATABASE -> RUNS
        self.See_Rest_Menu_Submit_PB.clicked.connect(self.create_new_Food_record)

    def retranslateUi(self, See_Rest_Menu_window):
        _translate = QtCore.QCoreApplication.translate
        See_Rest_Menu_window.setWindowTitle(_translate("See_Rest_Menu_window", "Food Order"))
        self.See_Rest_Menu_L.setText(_translate("See_Rest_Menu_window", "See Restaurant/CoffeeShop Menu"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("See_Rest_Menu_window", "Food Id"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("See_Rest_Menu_window", "Food name"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("See_Rest_Menu_window", "Food Price"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("See_Rest_Menu_window", "Ingredients"))
        item = self.See_Rest_Menu_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("See_Rest_Menu_window", "Type"))
        self.See_Rest_Menu_Search_PB.setText(_translate("See_Rest_Menu_window", "Search Base on name"))
        self.See_Rest_Menu_Room_RB.setText(_translate("See_Rest_Menu_window", "Room"))
        self.See_Rest_Menu_Rest_RB.setText(_translate("See_Rest_Menu_window", "Restaurant/Coffee"))
        self.See_Rest_Menu_where_L.setText(_translate("See_Rest_Menu_window", "Where Do You Eat ?"))
        self.See_Rest_Menu_Reservation_Id_L.setText(_translate("See_Rest_Menu_window", "Reservation Id"))
        self.See_Rest_Menu_Room_id_L.setText(_translate("See_Rest_Menu_window", "Room Id"))
        self.See_Rest_Menu_Submit_PB.setText(_translate("See_Rest_Menu_window", "Submit"))
        self.See_Rest_Menu_Search_Price_PB.setText(_translate("See_Rest_Menu_window", "Search Base on Mximum Price"))
        self.See_Rest_Menu_Food_Ids_L.setText(_translate("See_Rest_Menu_window", "Food Ids"))

    def Show_Restaurant_Menu(self):

        res = exe_query(f""" 
                               SELECT Food_ID,Food_Name,Food_Price,Food_Ingredients,Food_Drink_Identifier
                               FROM food WHERE Restaurant_CoffeeShop_ID = '{self.rest_cafe_id}';
                             """)

        row = 0
        self.See_Rest_Menu_TableWidget.setRowCount(len(res))
        for data in res:
            self.See_Rest_Menu_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.See_Rest_Menu_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.See_Rest_Menu_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.See_Rest_Menu_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            if data[4] == 1:
                self.See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Drink"))
            else:
                self.See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Food"))

            row += 1

    def search_special_food_drink(self):

        search_box = '%' + self.See_Rest_Menu_Enter_Food_LE.text() + '%'

        res = exe_query(f""" 
                               SELECT Food_ID,Food_Name,Food_Price,Food_Ingredients,Food_Drink_Identifier
                                FROM food where Restaurant_CoffeeShop_ID = '{self.rest_cafe_id}' AND 
                                Food_Name LIKE '{search_box}';
                             """)

        row = 0
        self.See_Rest_Menu_TableWidget.setRowCount(len(res))
        for data in res:
            self.See_Rest_Menu_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.See_Rest_Menu_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.See_Rest_Menu_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.See_Rest_Menu_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            if data[4] == 1:
                self.See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Drink"))
            else:
                self.See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Food"))

            row += 1

    def search_base_on_maximum_price(self):

        search_box = self.See_Rest_Menu_Enter_Price_LE.text()

        res = exe_query(f""" 
                                  SELECT Food_ID,Food_Name,Food_Price,Food_Ingredients,Food_Drink_Identifier
                                   FROM food where Restaurant_CoffeeShop_ID = '{self.rest_cafe_id}' AND 
                                    Food_Price <= '{float(search_box)}' ;
                                """)

        row = 0
        self.See_Rest_Menu_TableWidget.setRowCount(len(res))
        for data in res:
            self.See_Rest_Menu_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.See_Rest_Menu_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.See_Rest_Menu_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.See_Rest_Menu_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            if data[4] == 1:
                self.See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Drink"))
            else:
                self.See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Food"))

            row += 1

    def catch_Food_ids(self):
        room_ids = self.See_Rest_Menu_Food_Ids_LE.text().split(' ')
        f = open("../User/Script/File/Food_ids.txt", "w")
        for i in range(len(room_ids)):
            f.write(room_ids[i] + ' ')
        f.close()

    def create_new_Food_record(self):

        if self.catch_booking_status()[0][0] == 2 or self.catch_booking_status()[0][0] == 3:

            room_rest = False
            if self.See_Rest_Menu_Room_RB.isChecked():
                room_rest = True

            reservation_details_id = 0
            if (
                    (self.See_Rest_Menu_Reservation_Id_LE.text() != ' ')
                    and
                    (self.See_Rest_Menu_Room_Id_LE.text() != ' ')
            ):
                reservation_details_id = exe_query(f""" 
                                                    SELECT Reservation_Details_ID FROM reservation_details
                                                    WHERE Room_ID = '{int(self.See_Rest_Menu_Room_Id_LE.text())}'
                                                    AND
                                                    Reservation_ID = '{int(self.See_Rest_Menu_Reservation_Id_LE.text())}'
                                                  """)

            reservation_details_id = reservation_details_id[0][0]

            exe_query(f""" 
                      INSERT INTO food_order
                      (Food_Order_Room_Rest,Reservation_Details_ID)
                                        VALUES
                    ({room_rest},'{reservation_details_id}'); 
                    """)

            Food_Order_ID = exe_query(f""" 
                        SELECT Food_Order_ID FROM food_order WHERE 
                        Reservation_Details_ID = '{reservation_details_id}'; 
                       """)

            last_record_of_Food_order_id_with_this_reservation_details_id = Food_Order_ID[len(Food_Order_ID) - 1][0]

            self.catch_Food_ids()
            food_ids = read_Food_ids()

            for row in range(len(food_ids)):
                exe_query(f""" 
                                  INSERT INTO food_contains
                                  (Food_ID,Food_Order_ID)
                                                    VALUES
                                ('{food_ids[row]}','{last_record_of_Food_order_id_with_this_reservation_details_id}'); 
                                """)

            food_prices = []

            for row in range(len(food_ids)):
                food_prices.append(exe_query(f""" 
                            SELECT Food_Price FROM food WHERE 
                            Food_ID = '{food_ids[row]}'; 
                           """))

            for row in range(len(food_prices)):
                exe_query(f"""
                            UPDATE reservation SET Reservation_Bill_Total_Amount = 
                            Reservation_Bill_Total_Amount + '{food_prices[row][0][0]}'
                            WHERE Reservation_ID = '{int(self.See_Rest_Menu_Reservation_Id_LE.text())}' ;
                          """)

    def catch_booking_status(self):
        return exe_query(f""" 
                                            SELECT Booking_Status_ID FROM reservation
                                            WHERE
                                            Reservation_ID = '{int(self.See_Rest_Menu_Reservation_Id_LE.text())}'
                                          """)
