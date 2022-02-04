from PyQt5 import QtCore, QtGui, QtWidgets

from Admin.Script.Admin_Create_new_Staff import Ui_Admin_create_new_staff
from Admin.Script.Admin_List_Of_Housekeeper import Ui_Admin_list_of_Housekeeper_window
from Admin.Script.Admin_List_Of_Receptionist import Ui_Admin_list_of_receptionist_window
from Admin.Script.Admin_Remove_Employee import Ui_Admin_Remove_Employee_window
from Admin.Script.Admin_see_reataurant import Ui_Admin_See_Rest_window
from Admin.Script.Admin_see_room import Ui_Admin_See_Room_window


class Ui_Admin_WelcomePage(object):

    def setupUi(self, Admin_WelcomePage):
        Admin_WelcomePage.setObjectName("Admin_WelcomePage")
        Admin_WelcomePage.resize(1122, 842)
        Admin_WelcomePage.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Admin_WelcomePage.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.WelcomePage_Change_Menu_PB = QtWidgets.QPushButton(Admin_WelcomePage)
        self.WelcomePage_Change_Menu_PB.setGeometry(QtCore.QRect(610, 340, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Change_Menu_PB.setFont(font)
        self.WelcomePage_Change_Menu_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Change_Menu_PB.setStyleSheet("background-color: rgb(255, 232, 174);")
        self.WelcomePage_Change_Menu_PB.setObjectName("WelcomePage_Change_Menu_PB")
        self.WelcomePage_Add_new_employee_PB = QtWidgets.QPushButton(Admin_WelcomePage)
        self.WelcomePage_Add_new_employee_PB.setGeometry(QtCore.QRect(150, 230, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Add_new_employee_PB.setFont(font)
        self.WelcomePage_Add_new_employee_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Add_new_employee_PB.setStyleSheet("background-color: rgb(180, 255, 204);")
        self.WelcomePage_Add_new_employee_PB.setObjectName("WelcomePage_Add_new_employee_PB")
        self.WelcomePage_list_of_all_receptionist_PB = QtWidgets.QPushButton(Admin_WelcomePage)
        self.WelcomePage_list_of_all_receptionist_PB.setGeometry(QtCore.QRect(150, 340, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_list_of_all_receptionist_PB.setFont(font)
        self.WelcomePage_list_of_all_receptionist_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_list_of_all_receptionist_PB.setStyleSheet("background-color: rgb(255, 134, 12);")
        self.WelcomePage_list_of_all_receptionist_PB.setObjectName("WelcomePage_list_of_all_receptionist_PB")
        self.WelcomePage_List_cleaning_staff_PB = QtWidgets.QPushButton(Admin_WelcomePage)
        self.WelcomePage_List_cleaning_staff_PB.setGeometry(QtCore.QRect(140, 470, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_List_cleaning_staff_PB.setFont(font)
        self.WelcomePage_List_cleaning_staff_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_List_cleaning_staff_PB.setStyleSheet("background-color: rgb(255, 151, 196);")
        self.WelcomePage_List_cleaning_staff_PB.setObjectName("WelcomePage_List_cleaning_staff_PB")
        self.WelcomePage_Remove_Employee_PB = QtWidgets.QPushButton(Admin_WelcomePage)
        self.WelcomePage_Remove_Employee_PB.setGeometry(QtCore.QRect(610, 230, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Remove_Employee_PB.setFont(font)
        self.WelcomePage_Remove_Employee_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Remove_Employee_PB.setStyleSheet("background-color: rgb(152, 154, 255);")
        self.WelcomePage_Remove_Employee_PB.setObjectName("WelcomePage_Remove_Employee_PB")
        self.WelcomePage_header_L = QtWidgets.QLabel(Admin_WelcomePage)
        self.WelcomePage_header_L.setGeometry(QtCore.QRect(350, 60, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_header_L.setFont(font)
        self.WelcomePage_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.WelcomePage_header_L.setStyleSheet("background-color: rgb(201, 204, 255);")
        self.WelcomePage_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomePage_header_L.setObjectName("WelcomePage_header_L")
        self.WelcomePage_Change_type_of_room_PB = QtWidgets.QPushButton(Admin_WelcomePage)
        self.WelcomePage_Change_type_of_room_PB.setGeometry(QtCore.QRect(610, 470, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Change_type_of_room_PB.setFont(font)
        self.WelcomePage_Change_type_of_room_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Change_type_of_room_PB.setStyleSheet("background-color: rgb(232, 212, 255);")
        self.WelcomePage_Change_type_of_room_PB.setObjectName("WelcomePage_Change_type_of_room_PB")

        self.retranslateUi(Admin_WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(Admin_WelcomePage)

        # TODO:create_new_staff_Clicked
        self.WelcomePage_Add_new_employee_PB.clicked.connect(self.create_new_staff_window)

        # TODO:LIST_OF_ALL_RECEPTIONIST_Clicked
        self.WelcomePage_list_of_all_receptionist_PB.clicked.connect(self.list_of_receptionist_window)

        # TODO:LIST_CLEANING_STAFF_Clicked
        self.WelcomePage_List_cleaning_staff_PB.clicked.connect(self.list_of_House_Keeper_window)

        # TODO:REMOVE_EMPLOYEE_Clicked
        self.WelcomePage_Remove_Employee_PB.clicked.connect(self.remove_employee_window)

        # TODO:CHANGE_MENU_RESTAURANT_Clicked
        self.WelcomePage_Change_Menu_PB.clicked.connect(self.change_menu_restaurant_window)

        # TODO:CHANGE_THE_TYPE_OF_THE_ROOM_Clicked
        self.WelcomePage_Change_type_of_room_PB.clicked.connect(self.change_the_type_of_the_room_window)

    def retranslateUi(self, Admin_WelcomePage):
        _translate = QtCore.QCoreApplication.translate
        Admin_WelcomePage.setWindowTitle(_translate("Admin_WelcomePage", "Receptionist Welcome Page"))
        self.WelcomePage_Change_Menu_PB.setText(_translate("Admin_WelcomePage", "Change a Menu Restaurant"))
        self.WelcomePage_Add_new_employee_PB.setText(_translate("Admin_WelcomePage", "Add a new employee"))
        self.WelcomePage_list_of_all_receptionist_PB.setText(_translate("Admin_WelcomePage", "List of All Receptionist"))
        self.WelcomePage_List_cleaning_staff_PB.setText(_translate("Admin_WelcomePage", "List of all cleaning staff"))
        self.WelcomePage_Remove_Employee_PB.setText(_translate("Admin_WelcomePage", "Remove Employee"))
        self.WelcomePage_header_L.setText(_translate("Admin_WelcomePage", "WELCOME TO ADMIN HOME PAGE"))
        self.WelcomePage_Change_type_of_room_PB.setText(_translate("Admin_WelcomePage", "Change the type of a room"))

    def create_new_staff_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_create_new_staff()
        self.ui.setupUi(self.window)
        self.window.show()

    def list_of_receptionist_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_list_of_receptionist_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def list_of_House_Keeper_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_list_of_Housekeeper_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def remove_employee_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_Remove_Employee_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def change_menu_restaurant_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_See_Rest_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def change_the_type_of_the_room_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_See_Room_window()
        self.ui.setupUi(self.window)
        self.window.show()

