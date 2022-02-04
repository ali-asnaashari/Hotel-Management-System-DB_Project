from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_Admin_list_of_receptionist_window(object):

    def __init__(self):
        self.res = []

    def setupUi(self, Admin_list_of_receptionist_window):
        Admin_list_of_receptionist_window.setObjectName("Admin_list_of_receptionist_window")
        Admin_list_of_receptionist_window.resize(1278, 715)
        Admin_list_of_receptionist_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Admin_list_of_receptionist_window.setStyleSheet("background-color: rgb(255, 238, 249);")
        self.list_of_receptionist_header_L = QtWidgets.QLabel(Admin_list_of_receptionist_window)
        self.list_of_receptionist_header_L.setGeometry(QtCore.QRect(470, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.list_of_receptionist_header_L.setFont(font)
        self.list_of_receptionist_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.list_of_receptionist_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.list_of_receptionist_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.list_of_receptionist_header_L.setObjectName("list_of_receptionist_header_L")
        self.list_of_receptionist_TableWidget = QtWidgets.QTableWidget(Admin_list_of_receptionist_window)
        self.list_of_receptionist_TableWidget.setGeometry(QtCore.QRect(30, 120, 1231, 511))
        self.list_of_receptionist_TableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.list_of_receptionist_TableWidget.setObjectName("list_of_receptionist_TableWidget")
        self.list_of_receptionist_TableWidget.setColumnCount(8)
        self.list_of_receptionist_TableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(0, item)
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
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.list_of_receptionist_TableWidget.setHorizontalHeaderItem(7, item)
        self.list_of_receptionist_TableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.retranslateUi(Admin_list_of_receptionist_window)
        QtCore.QMetaObject.connectSlotsByName(Admin_list_of_receptionist_window)

        # TODO:SHOW_LIST_RECEPTIONIST_CLICKED
        self.show_receptionist()

    def retranslateUi(self, Admin_list_of_receptionist_window):
        _translate = QtCore.QCoreApplication.translate
        Admin_list_of_receptionist_window.setWindowTitle(_translate("Admin_list_of_receptionist_window", "List of Receptionists"))
        self.list_of_receptionist_header_L.setText(_translate("Admin_list_of_receptionist_window", "List of Receptionists"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Admin_list_of_receptionist_window", "Staff No. #"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Admin_list_of_receptionist_window", "First name"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Admin_list_of_receptionist_window", "Last name"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Admin_list_of_receptionist_window", "Email"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Admin_list_of_receptionist_window", "National id"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Admin_list_of_receptionist_window", "Password"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Admin_list_of_receptionist_window", "Salary"))
        item = self.list_of_receptionist_TableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Admin_list_of_receptionist_window", "Start date"))

    def show_receptionist(self):

        self.res = exe_query(f""" 
                                SELECT Staff_ID,Staff_Firstname,Staff_Lastname,Staff_Password,Staff_Email,
                                 Staff_National_ID,Staff_Salary,Staff_StartDate,Staff_Role_Recep_Cleaning
                                 FROM staff_information WHERE Staff_Role_Recep_Cleaning = 1 AND Staff_ID <> -1;
                            """)

        row = 0
        self.list_of_receptionist_TableWidget.setRowCount(len(self.res))
        for data in self.res:
            self.list_of_receptionist_TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.list_of_receptionist_TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data[1])))
            self.list_of_receptionist_TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))
            self.list_of_receptionist_TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(data[3])))
            self.list_of_receptionist_TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(data[4])))
            self.list_of_receptionist_TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data[5])))
            self.list_of_receptionist_TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data[6])))
            self.list_of_receptionist_TableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data[7])))

            row += 1
