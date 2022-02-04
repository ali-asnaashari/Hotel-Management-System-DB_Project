from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_Admin_See_Room_window(object):

    def setupUi(self, Admin_See_Room_window):
        Admin_See_Room_window.setObjectName("Admin_See_Room_window")
        Admin_See_Room_window.resize(1288, 814)
        Admin_See_Room_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Admin_See_Room_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.Admin_See_Room_header_L = QtWidgets.QLabel(Admin_See_Room_window)
        self.Admin_See_Room_header_L.setGeometry(QtCore.QRect(590, 40, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_header_L.setFont(font)
        self.Admin_See_Room_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Admin_See_Room_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.Admin_See_Room_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Admin_See_Room_header_L.setObjectName("Admin_See_Room_header_L")
        self.Admin_See_Room_show_PB = QtWidgets.QPushButton(Admin_See_Room_window)
        self.Admin_See_Room_show_PB.setGeometry(QtCore.QRect(880, 590, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_show_PB.setFont(font)
        self.Admin_See_Room_show_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin_See_Room_show_PB.setStyleSheet("background-color: rgb(7, 255, 152);")
        self.Admin_See_Room_show_PB.setObjectName("Admin_See_Room_show_PB")
        self.Admin_See_Room_TableWidget = QtWidgets.QTableWidget(Admin_See_Room_window)
        self.Admin_See_Room_TableWidget.setGeometry(QtCore.QRect(390, 120, 721, 361))
        self.Admin_See_Room_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin_See_Room_TableWidget.setObjectName("Admin_See_Room_TableWidget")
        self.Admin_See_Room_TableWidget.setColumnCount(5)
        self.Admin_See_Room_TableWidget.setRowCount(0)
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
        self.Admin_See_Room_TableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Room_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Room_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Room_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Admin_See_Room_TableWidget.setHorizontalHeaderItem(4, item)
        self.Admin_See_Room_TableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.Admin_See_Room_Room_id_LE = QtWidgets.QLineEdit(Admin_See_Room_window)
        self.Admin_See_Room_Room_id_LE.setGeometry(QtCore.QRect(610, 530, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_Room_id_LE.setFont(font)
        self.Admin_See_Room_Room_id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin_See_Room_Room_id_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.Admin_See_Room_Room_id_LE.setObjectName("Admin_See_Room_Room_id_LE")
        self.Admin_See_Room_No_beds_LE = QtWidgets.QLineEdit(Admin_See_Room_window)
        self.Admin_See_Room_No_beds_LE.setGeometry(QtCore.QRect(610, 610, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_No_beds_LE.setFont(font)
        self.Admin_See_Room_No_beds_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin_See_Room_No_beds_LE.setStyleSheet("background-color: rgb(244, 233, 255);")
        self.Admin_See_Room_No_beds_LE.setObjectName("Admin_See_Room_No_beds_LE")
        self.Admin_See_Room_Room_id_L = QtWidgets.QLabel(Admin_See_Room_window)
        self.Admin_See_Room_Room_id_L.setGeometry(QtCore.QRect(400, 520, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_Room_id_L.setFont(font)
        self.Admin_See_Room_Room_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Admin_See_Room_Room_id_L.setStyleSheet("background-color: rgb(255, 231, 90);")
        self.Admin_See_Room_Room_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Admin_See_Room_Room_id_L.setObjectName("Admin_See_Room_Room_id_L")
        self.Admin_See_Room_No_beds_L = QtWidgets.QLabel(Admin_See_Room_window)
        self.Admin_See_Room_No_beds_L.setGeometry(QtCore.QRect(400, 600, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_No_beds_L.setFont(font)
        self.Admin_See_Room_No_beds_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Admin_See_Room_No_beds_L.setStyleSheet("background-color: rgb(255, 231, 90);")
        self.Admin_See_Room_No_beds_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Admin_See_Room_No_beds_L.setObjectName("Admin_See_Room_No_beds_L")
        self.Admin_See_Room_under_reconstruction_L = QtWidgets.QLabel(Admin_See_Room_window)
        self.Admin_See_Room_under_reconstruction_L.setGeometry(QtCore.QRect(400, 690, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_under_reconstruction_L.setFont(font)
        self.Admin_See_Room_under_reconstruction_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Admin_See_Room_under_reconstruction_L.setStyleSheet("background-color: rgb(255, 231, 90);")
        self.Admin_See_Room_under_reconstruction_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Admin_See_Room_under_reconstruction_L.setObjectName("Admin_See_Room_under_reconstruction_L")
        self.Admin_See_Room_Apply_RD = QtWidgets.QRadioButton(Admin_See_Room_window)
        self.Admin_See_Room_Apply_RD.setGeometry(QtCore.QRect(690, 700, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Admin_See_Room_Apply_RD.setFont(font)
        self.Admin_See_Room_Apply_RD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Admin_See_Room_Apply_RD.setStyleSheet("background-color: rgb(198, 196, 255);")
        self.Admin_See_Room_Apply_RD.setCheckable(True)
        self.Admin_See_Room_Apply_RD.setObjectName("Admin_See_Room_Apply_RD")

        self.retranslateUi(Admin_See_Room_window)
        QtCore.QMetaObject.connectSlotsByName(Admin_See_Room_window)

        # TODO:SHOW_ROOM
        self.Show_All_Room()

        # TODO:CHANGE_RESTAURANT_MENU
        self.Admin_See_Room_show_PB.clicked.connect(self.change_room_details)

    def retranslateUi(self, Admin_See_Room_window):
        _translate = QtCore.QCoreApplication.translate
        Admin_See_Room_window.setWindowTitle(_translate("Admin_See_Room_window", "Change room type"))
        self.Admin_See_Room_header_L.setText(_translate("Admin_See_Room_window", "See Room"))
        self.Admin_See_Room_show_PB.setText(_translate("Admin_See_Room_window", "Apply Changes"))
        item = self.Admin_See_Room_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Admin_See_Room_window", "Room No. #"))
        item = self.Admin_See_Room_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Admin_See_Room_window", "Floor"))
        item = self.Admin_See_Room_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Admin_See_Room_window", "No beds"))
        item = self.Admin_See_Room_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Admin_See_Room_window", "Description"))
        item = self.Admin_See_Room_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Admin_See_Room_window", "Status"))
        self.Admin_See_Room_Room_id_L.setText(_translate("Admin_See_Room_window", "Room Id"))
        self.Admin_See_Room_No_beds_L.setText(_translate("Admin_See_Room_window", "No beds"))
        self.Admin_See_Room_under_reconstruction_L.setText(_translate("Admin_See_Room_window", "Under Reconstruction"))
        self.Admin_See_Room_Apply_RD.setText(_translate("Admin_See_Room_window", "Apply"))

    def Show_All_Room(self):

        res = exe_query(f""" 
                                SELECT Room_ID,Floor,no_beds,description,Room_Status_Name FROM room 
                                JOIN room_type rt on room.room_type_id = rt.room_type_id
                                JOIN room_status rs on rs.Room_Status_ID = room.Room_Status_ID order by Room_ID;
                             """)

        row = 0
        self.Admin_See_Room_TableWidget.setRowCount(len(res))
        for data in res:
            self.Admin_See_Room_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.Admin_See_Room_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.Admin_See_Room_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.Admin_See_Room_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.Admin_See_Room_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))

            row += 1

    def change_room_details(self):

        if self.Admin_See_Room_Room_id_LE.text() != '':
            room_id = int(self.Admin_See_Room_Room_id_LE.text())

            if self.Admin_See_Room_No_beds_LE.text() != '':
                exe_query(f"""
                            UPDATE room set room_type_id = '{int(self.Admin_See_Room_No_beds_LE.text())}' 
                            WHERE Room_ID = '{room_id}';
                          """)

            if self.Admin_See_Room_Apply_RD.isChecked():
                exe_query(f"""
                        UPDATE room set Room_Status_ID = 4 WHERE Room_ID = '{room_id}';
                          """)




