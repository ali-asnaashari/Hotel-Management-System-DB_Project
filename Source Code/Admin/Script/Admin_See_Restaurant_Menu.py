from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import admin_read_rest_cafe_id, exe_query


class Ui_Admin_See_Rest_Menu_window(object):

    def __init__(self):
        self.rest_cafe_id = admin_read_rest_cafe_id()
        self.food_id = -1

    def setupUi(self, Admin_See_Rest_Menu_window):
        Admin_See_Rest_Menu_window.setObjectName("Admin_See_Rest_Menu_window")
        Admin_See_Rest_Menu_window.resize(1119, 863)
        Admin_See_Rest_Menu_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Admin_See_Rest_Menu_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.Admin_See_Rest_Menu_L = QtWidgets.QLabel(Admin_See_Rest_Menu_window)
        self.Admin_See_Rest_Menu_L.setGeometry(QtCore.QRect(200, 20, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Rest_Menu_L.setFont(font)
        self.Admin_See_Rest_Menu_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Admin_See_Rest_Menu_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.Admin_See_Rest_Menu_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Admin_See_Rest_Menu_L.setObjectName("Admin_See_Rest_Menu_L")
        self.Admin_See_Rest_Menu_TableWidget = QtWidgets.QTableWidget(Admin_See_Rest_Menu_window)
        self.Admin_See_Rest_Menu_TableWidget.setGeometry(QtCore.QRect(50, 110, 701, 291))
        self.Admin_See_Rest_Menu_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin_See_Rest_Menu_TableWidget.setObjectName("Admin_See_Rest_Menu_TableWidget")
        self.Admin_See_Rest_Menu_TableWidget.setColumnCount(5)
        self.Admin_See_Rest_Menu_TableWidget.setRowCount(0)
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
        self.Admin_See_Rest_Menu_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Rest_Menu_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Rest_Menu_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Rest_Menu_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Rest_Menu_TableWidget.setHorizontalHeaderItem(4, item)
        self.Admin_See_Rest_Menu_TableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.See_Rest_Menu_Submit_PB = QtWidgets.QPushButton(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Submit_PB.setGeometry(QtCore.QRect(480, 740, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Submit_PB.setFont(font)
        self.See_Rest_Menu_Submit_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Submit_PB.setStyleSheet("background-color: rgb(8, 255, 140);")
        self.See_Rest_Menu_Submit_PB.setObjectName("See_Rest_Menu_Submit_PB")
        self.See_Rest_Menu_Food_Ids_LE = QtWidgets.QLineEdit(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_Ids_LE.setGeometry(QtCore.QRect(780, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_Ids_LE.setFont(font)
        self.See_Rest_Menu_Food_Ids_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Food_Ids_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Food_Ids_LE.setObjectName("See_Rest_Menu_Food_Ids_LE")
        self.Admin_See_Rest_Menu_Food_Ids_L = QtWidgets.QLabel(Admin_See_Rest_Menu_window)
        self.Admin_See_Rest_Menu_Food_Ids_L.setGeometry(QtCore.QRect(820, 120, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Rest_Menu_Food_Ids_L.setFont(font)
        self.Admin_See_Rest_Menu_Food_Ids_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Admin_See_Rest_Menu_Food_Ids_L.setStyleSheet("background-color: rgb(157, 224, 255);")
        self.Admin_See_Rest_Menu_Food_Ids_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Admin_See_Rest_Menu_Food_Ids_L.setObjectName("Admin_See_Rest_Menu_Food_Ids_L")
        self.See_Rest_Menu_Food_name_L = QtWidgets.QLabel(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_name_L.setGeometry(QtCore.QRect(80, 470, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_name_L.setFont(font)
        self.See_Rest_Menu_Food_name_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_Food_name_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.See_Rest_Menu_Food_name_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_Food_name_L.setObjectName("See_Rest_Menu_Food_name_L")
        self.See_Rest_Menu_Food_name_LE = QtWidgets.QLineEdit(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_name_LE.setGeometry(QtCore.QRect(40, 540, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_name_LE.setFont(font)
        self.See_Rest_Menu_Food_name_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Food_name_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Food_name_LE.setObjectName("See_Rest_Menu_Food_name_LE")
        self.See_Rest_Menu_Food_Ingredients_L = QtWidgets.QLabel(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_Ingredients_L.setGeometry(QtCore.QRect(780, 470, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_Ingredients_L.setFont(font)
        self.See_Rest_Menu_Food_Ingredients_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_Food_Ingredients_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.See_Rest_Menu_Food_Ingredients_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_Food_Ingredients_L.setObjectName("See_Rest_Menu_Food_Ingredients_L")
        self.See_Rest_Menu_Food_Ingredients_LE = QtWidgets.QLineEdit(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_Ingredients_LE.setGeometry(QtCore.QRect(740, 540, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_Ingredients_LE.setFont(font)
        self.See_Rest_Menu_Food_Ingredients_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Food_Ingredients_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Food_Ingredients_LE.setObjectName("See_Rest_Menu_Food_Ingredients_LE")
        self.See_Rest_Menu_Food_Price_L = QtWidgets.QLabel(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_Price_L.setGeometry(QtCore.QRect(440, 470, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_Price_L.setFont(font)
        self.See_Rest_Menu_Food_Price_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.See_Rest_Menu_Food_Price_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.See_Rest_Menu_Food_Price_L.setAlignment(QtCore.Qt.AlignCenter)
        self.See_Rest_Menu_Food_Price_L.setObjectName("See_Rest_Menu_Food_Price_L")
        self.See_Rest_Menu_Food_Price_LE = QtWidgets.QLineEdit(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_Price_LE.setGeometry(QtCore.QRect(400, 540, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_Price_LE.setFont(font)
        self.See_Rest_Menu_Food_Price_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Food_Price_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.See_Rest_Menu_Food_Price_LE.setObjectName("See_Rest_Menu_Food_Price_LE")
        self.See_Rest_Menu_Food_RB = QtWidgets.QRadioButton(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Food_RB.setGeometry(QtCore.QRect(330, 620, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Food_RB.setFont(font)
        self.See_Rest_Menu_Food_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Food_RB.setStyleSheet("background-color: rgb(151, 215, 255);")
        self.See_Rest_Menu_Food_RB.setObjectName("See_Rest_Menu_Food_RB")
        self.See_Rest_Menu_Drink_RB = QtWidgets.QRadioButton(Admin_See_Rest_Menu_window)
        self.See_Rest_Menu_Drink_RB.setGeometry(QtCore.QRect(560, 620, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.See_Rest_Menu_Drink_RB.setFont(font)
        self.See_Rest_Menu_Drink_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.See_Rest_Menu_Drink_RB.setStyleSheet("background-color: rgb(151, 215, 255);")
        self.See_Rest_Menu_Drink_RB.setObjectName("See_Rest_Menu_Drink_RB")
        self.Type_L = QtWidgets.QLabel(Admin_See_Rest_Menu_window)
        self.Type_L.setGeometry(QtCore.QRect(50, 620, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Type_L.setFont(font)
        self.Type_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Type_L.setStyleSheet("background-color: rgb(255, 222, 156);")
        self.Type_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Type_L.setObjectName("Type_L")

        self.retranslateUi(Admin_See_Rest_Menu_window)
        QtCore.QMetaObject.connectSlotsByName(Admin_See_Rest_Menu_window)

        # TODO:SHOW_RESTAURANT_MENU
        self.Show_Restaurant_Menu()

        # TODO:CHANGE_RESTAURANT_MENU
        self.See_Rest_Menu_Submit_PB.clicked.connect(self.change_menu_restaurant)

    def retranslateUi(self, Admin_See_Rest_Menu_window):
        _translate = QtCore.QCoreApplication.translate
        Admin_See_Rest_Menu_window.setWindowTitle(_translate("Admin_See_Rest_Menu_window", "Change Menu"))
        self.Admin_See_Rest_Menu_L.setText(_translate("Admin_See_Rest_Menu_window", "See Restaurant/CoffeeShop Menu"))
        item = self.Admin_See_Rest_Menu_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Admin_See_Rest_Menu_window", "Food Id"))
        item = self.Admin_See_Rest_Menu_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Admin_See_Rest_Menu_window", "Food name"))
        item = self.Admin_See_Rest_Menu_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Admin_See_Rest_Menu_window", "Food Price"))
        item = self.Admin_See_Rest_Menu_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Admin_See_Rest_Menu_window", "Ingredients"))
        item = self.Admin_See_Rest_Menu_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Admin_See_Rest_Menu_window", "Type"))
        self.See_Rest_Menu_Submit_PB.setText(_translate("Admin_See_Rest_Menu_window", "Submit"))
        self.Admin_See_Rest_Menu_Food_Ids_L.setText(_translate("Admin_See_Rest_Menu_window", "Food Ids"))
        self.See_Rest_Menu_Food_name_L.setText(_translate("Admin_See_Rest_Menu_window", "Food Name"))
        self.See_Rest_Menu_Food_Ingredients_L.setText(_translate("Admin_See_Rest_Menu_window", "Food Ingredients"))
        self.See_Rest_Menu_Food_Price_L.setText(_translate("Admin_See_Rest_Menu_window", "Food Price"))
        self.See_Rest_Menu_Food_RB.setText(_translate("Admin_See_Rest_Menu_window", "Food"))
        self.See_Rest_Menu_Drink_RB.setText(_translate("Admin_See_Rest_Menu_window", "Drink"))
        self.Type_L.setText(_translate("Admin_See_Rest_Menu_window", "Type"))

    def Show_Restaurant_Menu(self):

        res = exe_query(f""" 
                               SELECT Food_ID,Food_Name,Food_Price,Food_Ingredients,Food_Drink_Identifier
                               FROM food WHERE Restaurant_CoffeeShop_ID = '{self.rest_cafe_id}';
                             """)

        row = 0
        self.Admin_See_Rest_Menu_TableWidget.setRowCount(len(res))
        for data in res:
            self.Admin_See_Rest_Menu_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.Admin_See_Rest_Menu_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.Admin_See_Rest_Menu_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.Admin_See_Rest_Menu_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            if data[4] == 1:
                self.Admin_See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Food"))
            else:
                self.Admin_See_Rest_Menu_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("Drink"))

            row += 1

    def change_menu_restaurant(self):

        if self.See_Rest_Menu_Food_Ids_LE.text() != '':
            self.food_id = int(self.See_Rest_Menu_Food_Ids_LE.text())

            if self.See_Rest_Menu_Food_name_LE.text() != '':
                exe_query(f"""
                            UPDATE food SET
                            Food_Name =  '{self.See_Rest_Menu_Food_name_LE.text()}' 
                           WHERE Food_ID = '{self.food_id}'
                          """)

            if self.See_Rest_Menu_Food_Price_LE.text() != '':
                exe_query(f"""
                            UPDATE food SET
                            Food_Price =  '{self.See_Rest_Menu_Food_Price_LE.text()}' 
                           WHERE Food_ID = '{self.food_id}'
                          """)

            if self.See_Rest_Menu_Food_Ingredients_LE.text() != '':
                exe_query(f"""
                            UPDATE food SET
                            Food_Ingredients =  '{self.See_Rest_Menu_Food_Ingredients_LE.text()}' 
                           WHERE Food_ID = '{self.food_id}'
                          """)

            if self.See_Rest_Menu_Food_RB.isChecked():
                role = 1
                exe_query(f"""
                            UPDATE food SET
                            Food_Drink_Identifier =  {role}
                           WHERE Food_ID = '{self.food_id}'
                          """)
            elif  self.See_Rest_Menu_Drink_RB.isChecked():
                role = 0
                exe_query(f"""
                            UPDATE food SET
                            Food_Drink_Identifier =  {role}
                           WHERE Food_ID = '{self.food_id}'
                          """)



