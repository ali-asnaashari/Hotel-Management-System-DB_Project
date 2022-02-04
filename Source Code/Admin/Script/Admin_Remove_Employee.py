from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_Admin_Remove_Employee_window(object):

    def __init__(self):
        self.res = []
        self.staff_id = -1

    def setupUi(self, Admin_Remove_Employee_window):
        Admin_Remove_Employee_window.setObjectName("Admin_Remove_Employee_window")
        Admin_Remove_Employee_window.resize(1303, 783)
        Admin_Remove_Employee_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Admin_Remove_Employee_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.Remove_Employee_header_L = QtWidgets.QLabel(Admin_Remove_Employee_window)
        self.Remove_Employee_header_L.setGeometry(QtCore.QRect(470, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Remove_Employee_header_L.setFont(font)
        self.Remove_Employee_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Remove_Employee_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.Remove_Employee_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Remove_Employee_header_L.setObjectName("Remove_Employee_header_L")
        self.Remove_Employee_TableWidget = QtWidgets.QTableWidget(Admin_Remove_Employee_window)
        self.Remove_Employee_TableWidget.setGeometry(QtCore.QRect(30, 120, 1231, 461))
        self.Remove_Employee_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Remove_Employee_TableWidget.setObjectName("Remove_Employee_TableWidget")
        self.Remove_Employee_TableWidget.setColumnCount(8)
        self.Remove_Employee_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(0, item)
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
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Remove_Employee_TableWidget.setHorizontalHeaderItem(7, item)
        self.Remove_Employee_TableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.Remove_Employee_remove_PB = QtWidgets.QPushButton(Admin_Remove_Employee_window)
        self.Remove_Employee_remove_PB.setGeometry(QtCore.QRect(960, 630, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Remove_Employee_remove_PB.setFont(font)
        self.Remove_Employee_remove_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Remove_Employee_remove_PB.setAcceptDrops(False)
        self.Remove_Employee_remove_PB.setAutoFillBackground(False)
        self.Remove_Employee_remove_PB.setStyleSheet("background-color: rgb(138, 201, 255);")
        self.Remove_Employee_remove_PB.setObjectName("Remove_Employee_remove_PB")
        self.Remove_Employee_Staff_id_LE = QtWidgets.QLineEdit(Admin_Remove_Employee_window)
        self.Remove_Employee_Staff_id_LE.setGeometry(QtCore.QRect(340, 640, 321, 51))
        self.Remove_Employee_Staff_id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Remove_Employee_Staff_id_LE.setObjectName("Remove_Employee_Staff_id_LE")
        self.Remove_Employee_Staff_id_L = QtWidgets.QLabel(Admin_Remove_Employee_window)
        self.Remove_Employee_Staff_id_L.setGeometry(QtCore.QRect(130, 640, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Remove_Employee_Staff_id_L.setFont(font)
        self.Remove_Employee_Staff_id_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Remove_Employee_Staff_id_L.setStyleSheet("background-color: rgb(255, 201, 5);")
        self.Remove_Employee_Staff_id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Remove_Employee_Staff_id_L.setObjectName("Remove_Employee_Staff_id_L")

        self.retranslateUi(Admin_Remove_Employee_window)
        QtCore.QMetaObject.connectSlotsByName(Admin_Remove_Employee_window)

        # TODO:SHOW_LIST_ALL_EMPLOYEE_CLICKED
        self.show_all_of_employee()

        # TODO:REMOVE_EMPLOYEE_CLICKED
        self.Remove_Employee_remove_PB.clicked.connect(self.remove_staff)

    def retranslateUi(self, Admin_Remove_Employee_window):
        _translate = QtCore.QCoreApplication.translate
        Admin_Remove_Employee_window.setWindowTitle(_translate("Admin_Remove_Employee_window", "Remove A Employee"))
        self.Remove_Employee_header_L.setText(_translate("Admin_Remove_Employee_window", "List of Employee"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Admin_Remove_Employee_window", "Staff No. #"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Admin_Remove_Employee_window", "First name"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Admin_Remove_Employee_window", "Last name"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Admin_Remove_Employee_window", "Email"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Admin_Remove_Employee_window", "National id"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Admin_Remove_Employee_window", "Password"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Admin_Remove_Employee_window", "Salary"))
        item = self.Remove_Employee_TableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Admin_Remove_Employee_window", "Start date"))
        self.Remove_Employee_remove_PB.setText(_translate("Admin_Remove_Employee_window", "Remove"))
        self.Remove_Employee_Staff_id_L.setText(_translate("Admin_Remove_Employee_window", "Staff No.#"))

    def show_all_of_employee(self):
        self.res = exe_query(f""" 
                                SELECT Staff_ID,Staff_Firstname,Staff_Lastname,Staff_Password,Staff_Email,
                                 Staff_National_ID,Staff_Salary,Staff_StartDate,Staff_Role_Recep_Cleaning
                                 FROM staff_information WHERE Staff_ID <> -1;
                            """)

        row = 0
        self.Remove_Employee_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.Remove_Employee_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.Remove_Employee_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.Remove_Employee_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.Remove_Employee_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.Remove_Employee_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.Remove_Employee_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))
            self.Remove_Employee_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data[6])))
            self.Remove_Employee_TableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data[7])))

            row += 1

    def remove_staff(self):

        if self.Remove_Employee_Staff_id_LE.text() != '':
            self.staff_id = int(self.Remove_Employee_Staff_id_LE.text())
            exe_query(f"""
                        UPDATE cleaning_service SET Staff_ID = -1 WHERE Staff_ID = '{self.staff_id}';
                     """)
            exe_query(f"""
                        UPDATE reservation SET Staff_ID = -1 WHERE Staff_ID = '{self.staff_id}';
                     """)
            exe_query(f"""
                        DELETE FROM staff_information WHERE Staff_ID = '{self.staff_id}';
                     """)
