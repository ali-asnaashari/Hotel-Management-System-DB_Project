from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_cleaning_service_assign_window(object):

    def __init__(self):
        self.resOne = []
        self.resTwo = []

    def setupUi(self, cleaning_service_assign_window):
        cleaning_service_assign_window.setObjectName("cleaning_service_assign_window")
        cleaning_service_assign_window.resize(1054, 808)
        cleaning_service_assign_window.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        cleaning_service_assign_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.cleaning_service_assign_Header_L = QtWidgets.QLabel(cleaning_service_assign_window)
        self.cleaning_service_assign_Header_L.setGeometry(QtCore.QRect(330, 20, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_assign_Header_L.setFont(font)
        self.cleaning_service_assign_Header_L.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_assign_Header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.cleaning_service_assign_Header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_service_assign_Header_L.setObjectName("cleaning_service_assign_Header_L")
        self.cleaning_service_assign_PB = QtWidgets.QPushButton(cleaning_service_assign_window)
        self.cleaning_service_assign_PB.setGeometry(QtCore.QRect(450, 720, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_assign_PB.setFont(font)
        self.cleaning_service_assign_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_assign_PB.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.cleaning_service_assign_PB.setObjectName("cleaning_service_assign_PB")
        self.cleaning_service_assign_staff_id_LE = QtWidgets.QLineEdit(cleaning_service_assign_window)
        self.cleaning_service_assign_staff_id_LE.setGeometry(QtCore.QRect(220, 650, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_assign_staff_id_LE.setFont(font)
        self.cleaning_service_assign_staff_id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_assign_staff_id_LE.setObjectName("cleaning_service_assign_staff_id_LE")
        self.cleaning_service_assign_staff_id_L = QtWidgets.QLabel(cleaning_service_assign_window)
        self.cleaning_service_assign_staff_id_L.setGeometry(QtCore.QRect(220, 570, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_assign_staff_id_L.setFont(font)
        self.cleaning_service_assign_staff_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.cleaning_service_assign_staff_id_L.setStyleSheet("background-color: rgb(255, 211, 35);")
        self.cleaning_service_assign_staff_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_service_assign_staff_id_L.setObjectName("cleaning_service_assign_staff_id_L")
        self.cleaning_service_assign_cleaning_id_L = QtWidgets.QLabel(cleaning_service_assign_window)
        self.cleaning_service_assign_cleaning_id_L.setGeometry(QtCore.QRect(630, 570, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_assign_cleaning_id_L.setFont(font)
        self.cleaning_service_assign_cleaning_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.cleaning_service_assign_cleaning_id_L.setStyleSheet("background-color: rgb(255, 211, 35);")
        self.cleaning_service_assign_cleaning_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.cleaning_service_assign_cleaning_id_L.setObjectName("cleaning_service_assign_cleaning_id_L")
        self.cleaning_service_assign_cleaning_id_LE = QtWidgets.QLineEdit(cleaning_service_assign_window)
        self.cleaning_service_assign_cleaning_id_LE.setGeometry(QtCore.QRect(630, 650, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cleaning_service_assign_cleaning_id_LE.setFont(font)
        self.cleaning_service_assign_cleaning_id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_assign_cleaning_id_LE.setObjectName("cleaning_service_assign_cleaning_id_LE")
        self.cleaning_service_assign_TableWidget = QtWidgets.QTableWidget(cleaning_service_assign_window)
        self.cleaning_service_assign_TableWidget.setGeometry(QtCore.QRect(280, 130, 651, 411))
        self.cleaning_service_assign_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_assign_TableWidget.setStyleSheet("background-color: rgb(225, 212, 255);")
        self.cleaning_service_assign_TableWidget.setObjectName("cleaning_service_assign_TableWidget")
        self.cleaning_service_assign_TableWidget.setColumnCount(4)
        self.cleaning_service_assign_TableWidget.setRowCount(0)
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
        self.cleaning_service_assign_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cleaning_service_assign_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cleaning_service_assign_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.cleaning_service_assign_TableWidget.setHorizontalHeaderItem(3, item)
        self.cleaning_service_assign_TableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.cleaning_service_assign_TableWidget_2 = QtWidgets.QTableWidget(cleaning_service_assign_window)
        self.cleaning_service_assign_TableWidget_2.setGeometry(QtCore.QRect(40, 130, 151, 411))
        self.cleaning_service_assign_TableWidget_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleaning_service_assign_TableWidget_2.setStyleSheet("background-color: rgb(245, 255, 233);")
        self.cleaning_service_assign_TableWidget_2.setObjectName("cleaning_service_assign_TableWidget_2")
        self.cleaning_service_assign_TableWidget_2.setColumnCount(1)
        self.cleaning_service_assign_TableWidget_2.setRowCount(0)
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
        self.cleaning_service_assign_TableWidget_2.setHorizontalHeaderItem(0, item)
        self.cleaning_service_assign_TableWidget_2.horizontalHeader().setDefaultSectionSize(155)

        self.retranslateUi(cleaning_service_assign_window)
        QtCore.QMetaObject.connectSlotsByName(cleaning_service_assign_window)

        # TODO: SHOW_STAFF_ID_AUTOMATICALLY
        self.show_staff()
        # TODO: SHOW_SERVICE_REQUEST_AUTOMATICALLY
        self.show_cleaning_service_request()
        # TODO: ASSIGN_BUTTON_CLICKED
        self.cleaning_service_assign_PB.clicked.connect(self.assign_staff)

    def retranslateUi(self, cleaning_service_assign_window):
        _translate = QtCore.QCoreApplication.translate
        cleaning_service_assign_window.setWindowTitle(_translate("cleaning_service_assign_window", "Assign Housekeeper"))
        self.cleaning_service_assign_Header_L.setText(_translate("cleaning_service_assign_window", "Assign Staff To Cleaning Order"))
        self.cleaning_service_assign_PB.setText(_translate("cleaning_service_assign_window", "Assign"))
        self.cleaning_service_assign_staff_id_L.setText(_translate("cleaning_service_assign_window", "Enter Staff No. #"))
        self.cleaning_service_assign_cleaning_id_L.setText(_translate("cleaning_service_assign_window", "Enter Cleaning service No. #"))
        item = self.cleaning_service_assign_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("cleaning_service_assign_window", "Cleaning No. #"))
        item = self.cleaning_service_assign_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("cleaning_service_assign_window", "Time"))
        item = self.cleaning_service_assign_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("cleaning_service_assign_window", "Date"))
        item = self.cleaning_service_assign_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("cleaning_service_assign_window", "Description"))
        item = self.cleaning_service_assign_TableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("cleaning_service_assign_window", "Staff No. #"))

    def show_staff(self):
        self.resOne = exe_query(f""" 
                                SELECT Staff_ID FROM staff_information 
                                WHERE Staff_Role_Recep_Cleaning = 0;
                              """)

        row = 0
        self.cleaning_service_assign_TableWidget_2.setRowCount(len(self.resOne))
        for data in self.resOne:
            self.cleaning_service_assign_TableWidget_2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))

            row += 1

    def show_cleaning_service_request(self):
        self.resTwo = exe_query(f""" 
                                    SELECT Cleaning_Service_ID,Cleaning_Service_Time,Cleaning_Service_Date,
                                    Cleaning_Service_Description FROM cleaning_service WHERE Staff_ID = -1;
                              """)

        row = 0
        self.cleaning_service_assign_TableWidget.setRowCount(len(self.resTwo))
        for data in self.resTwo:
            self.cleaning_service_assign_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.cleaning_service_assign_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.cleaning_service_assign_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.cleaning_service_assign_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))

            row += 1

    def assign_staff(self):
        self.resOne = exe_query(f""" 
                                    UPDATE cleaning_service SET 
                                    Staff_ID = '{int(self.cleaning_service_assign_staff_id_LE.text())}'
                                     WHERE 
                                     Cleaning_Service_ID = '{int(self.cleaning_service_assign_cleaning_id_LE.text())}';
                                """)

        reservation_id = exe_query(f""" 
                                        select  r.Reservation_ID from cleaning_service join reservation_details rd on 
                                        rd.Reservation_Details_ID = cleaning_service.Reservation_Details_ID
                                        join reservation r on r.Reservation_ID = rd.Reservation_ID where 
                                        Cleaning_Service_ID  = 
                                        '{int(self.cleaning_service_assign_cleaning_id_LE.text())}';
                                """)
        reservation_id = reservation_id[0][0]
        exe_query(f"""
                    update reservation set Reservation_Bill_Total_Amount =
                     Reservation_Bill_Total_Amount + 10.00 where Reservation_ID = '{reservation_id}';
                    
                    """)
        



