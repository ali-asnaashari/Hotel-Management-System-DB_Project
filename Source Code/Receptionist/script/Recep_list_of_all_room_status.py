from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_recept_list_room_status_window(object):

    def __init__(self):
        self.res = []
        self.status = -1

    def setupUi(self, recept_list_room_status_window):
        recept_list_room_status_window.setObjectName("recept_list_room_status_window")
        recept_list_room_status_window.resize(1108, 782)
        recept_list_room_status_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        recept_list_room_status_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.recept_list_room_status_header_L = QtWidgets.QLabel(recept_list_room_status_window)
        self.recept_list_room_status_header_L.setGeometry(QtCore.QRect(410, 10, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_list_room_status_header_L.setFont(font)
        self.recept_list_room_status_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.recept_list_room_status_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.recept_list_room_status_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recept_list_room_status_header_L.setObjectName("recept_list_room_status_header_L")
        self.recept_list_room_status_TableWidget = QtWidgets.QTableWidget(recept_list_room_status_window)
        self.recept_list_room_status_TableWidget.setGeometry(QtCore.QRect(70, 80, 941, 511))
        self.recept_list_room_status_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_list_room_status_TableWidget.setStyleSheet("background-color: rgb(225, 212, 255);")
        self.recept_list_room_status_TableWidget.setObjectName("recept_list_room_status_TableWidget")
        self.recept_list_room_status_TableWidget.setColumnCount(6)
        self.recept_list_room_status_TableWidget.setRowCount(0)
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
        self.recept_list_room_status_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_list_room_status_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_list_room_status_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_list_room_status_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_list_room_status_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.recept_list_room_status_TableWidget.setHorizontalHeaderItem(5, item)
        self.recept_list_room_status_TableWidget.horizontalHeader().setDefaultSectionSize(155)
        self.recept_list_room_status_Empty_RB = QtWidgets.QRadioButton(recept_list_room_status_window)
        self.recept_list_room_status_Empty_RB.setGeometry(QtCore.QRect(200, 640, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recept_list_room_status_Empty_RB.setFont(font)
        self.recept_list_room_status_Empty_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_list_room_status_Empty_RB.setStyleSheet("background-color: rgb(2, 27, 255);\n"
"color: rgb(255, 255, 255);")
        self.recept_list_room_status_Empty_RB.setObjectName("recept_list_room_status_Empty_RB")
        self.recept_list_room_status_show_PB = QtWidgets.QPushButton(recept_list_room_status_window)
        self.recept_list_room_status_show_PB.setGeometry(QtCore.QRect(760, 650, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recept_list_room_status_show_PB.setFont(font)
        self.recept_list_room_status_show_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_list_room_status_show_PB.setStyleSheet("background-color: rgb(8, 255, 140);")
        self.recept_list_room_status_show_PB.setObjectName("recept_list_room_status_show_PB")
        self.recept_list_room_status_reserved_RB = QtWidgets.QRadioButton(recept_list_room_status_window)
        self.recept_list_room_status_reserved_RB.setGeometry(QtCore.QRect(420, 640, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recept_list_room_status_reserved_RB.setFont(font)
        self.recept_list_room_status_reserved_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_list_room_status_reserved_RB.setStyleSheet("background-color: rgb(2, 27, 255);\n"
"color: rgb(255, 255, 255);")
        self.recept_list_room_status_reserved_RB.setObjectName("recept_list_room_status_reserved_RB")
        self.recept_list_room_status_UnderReconstruction_RB = QtWidgets.QRadioButton(recept_list_room_status_window)
        self.recept_list_room_status_UnderReconstruction_RB.setGeometry(QtCore.QRect(420, 720, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recept_list_room_status_UnderReconstruction_RB.setFont(font)
        self.recept_list_room_status_UnderReconstruction_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_list_room_status_UnderReconstruction_RB.setStyleSheet("background-color: rgb(2, 27, 255);\n"
"color: rgb(255, 255, 255);")
        self.recept_list_room_status_UnderReconstruction_RB.setObjectName("recept_list_room_status_UnderReconstruction_RB")
        self.recept_list_room_status_Full_RB = QtWidgets.QRadioButton(recept_list_room_status_window)
        self.recept_list_room_status_Full_RB.setGeometry(QtCore.QRect(200, 720, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recept_list_room_status_Full_RB.setFont(font)
        self.recept_list_room_status_Full_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recept_list_room_status_Full_RB.setStyleSheet("background-color: rgb(2, 27, 255);\n"
"color: rgb(255, 255, 255);")
        self.recept_list_room_status_Full_RB.setObjectName("recept_list_room_status_Full_RB")

        self.retranslateUi(recept_list_room_status_window)
        QtCore.QMetaObject.connectSlotsByName(recept_list_room_status_window)

        # TODO:show_all_room_status_Automatically
        self.show_all_room_status()

        # TODO:SEE_LIST_OF_ROOM_STATUS_WHEN_SHOW_BUTTON_CLICKED
        self.recept_list_room_status_show_PB.clicked.connect(self.room_status)
        self.show_all_room_status()

    def retranslateUi(self, recept_list_room_status_window):
        _translate = QtCore.QCoreApplication.translate
        recept_list_room_status_window.setWindowTitle(_translate("recept_list_room_status_window", "list of all room status"))
        self.recept_list_room_status_header_L.setText(_translate("recept_list_room_status_window", "List of Rooms"))
        item = self.recept_list_room_status_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("recept_list_room_status_window", "Room No. #"))
        item = self.recept_list_room_status_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("recept_list_room_status_window", "Floor"))
        item = self.recept_list_room_status_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("recept_list_room_status_window", "Price per night"))
        item = self.recept_list_room_status_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("recept_list_room_status_window", "Maximum Capacity"))
        item = self.recept_list_room_status_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("recept_list_room_status_window", "Description"))
        item = self.recept_list_room_status_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("recept_list_room_status_window", "Status"))
        self.recept_list_room_status_Empty_RB.setText(_translate("recept_list_room_status_window", "Empty"))
        self.recept_list_room_status_show_PB.setText(_translate("recept_list_room_status_window", "show"))
        self.recept_list_room_status_reserved_RB.setText(_translate("recept_list_room_status_window", "Reserved"))
        self.recept_list_room_status_UnderReconstruction_RB.setText(_translate("recept_list_room_status_window", "Under Reconstruction"))
        self.recept_list_room_status_Full_RB.setText(_translate("recept_list_room_status_window", "Full"))

    def show_all_room_status(self):

        self.res = exe_query(f""" 
                                SELECT Room_ID,Floor,Price_Per_Night,Maximum_Capacity,description,Room_Status_Name
                                 FROM room JOIN room_status on room_status.Room_Status_ID = room.Room_Status_ID
                                JOIN room_type rt on room.room_type_id = rt.room_type_id
                                ORDER BY Room_ID;
                            """)

        row = 0
        self.recept_list_room_status_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.recept_list_room_status_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.recept_list_room_status_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.recept_list_room_status_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.recept_list_room_status_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.recept_list_room_status_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.recept_list_room_status_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))

            row += 1

    def room_status(self):

        if self.recept_list_room_status_Full_RB.isChecked():
            self.status = 3
        elif self.recept_list_room_status_Empty_RB.isChecked():
            self.status = 1
        elif self.recept_list_room_status_UnderReconstruction_RB.isChecked():
            self.status = 4
        elif self.recept_list_room_status_reserved_RB.isChecked():
            self.status = 2

        self.res = exe_query(f""" 
                                SELECT Room_ID,Floor,Price_Per_Night,Maximum_Capacity,description,Room_Status_Name
                                 FROM room JOIN room_status on room_status.Room_Status_ID = room.Room_Status_ID
                                JOIN room_type rt on room.room_type_id = rt.room_type_id
                                WHERE room_status.Room_Status_ID = '{self.status}' ORDER BY Room_ID;
                            """)

        row = 0
        self.recept_list_room_status_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.recept_list_room_status_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.recept_list_room_status_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.recept_list_room_status_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.recept_list_room_status_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.recept_list_room_status_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.recept_list_room_status_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))

            row += 1


