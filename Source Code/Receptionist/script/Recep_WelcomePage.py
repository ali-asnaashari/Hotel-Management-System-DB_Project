from PyQt5 import QtCore, QtGui, QtWidgets

from Receptionist.script.Recep_Assign_employee_to_customer_service_request import Ui_cleaning_service_assign_window
from Receptionist.script.Recep_Number_of_reservation import Ui_Recept_Number_of_reservation_window
from Receptionist.script.Recep_cleaning_service_reservation import Ui_cleaning_service_reservation_window
from Receptionist.script.Recep_customer_booking import Ui_customer_booking_window
from Receptionist.script.Recep_list_of_all_people_bill_account import Ui_recep_list_of_all_people_bill_account_window
from Receptionist.script.Recep_list_of_all_people_birth_date import Ui_recep_list_of_all_people_birth_date_window
from Receptionist.script.Recep_list_of_all_reservations import Ui_recept_reservation_list_window
from Receptionist.script.Recep_list_of_all_room_status import Ui_recept_list_room_status_window
from Receptionist.script.Recep_reservation_confirm_cancel import Ui_recept_reservation_CC_window
from Start.DB_Configuration import read_recep_details


class Ui_Recep_WelcomePage(object):


    def setupUi(self, Recep_WelcomePage):
        Recep_WelcomePage.setObjectName("Recep_WelcomePage")
        Recep_WelcomePage.resize(1122, 842)
        Recep_WelcomePage.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        Recep_WelcomePage.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.WelcomePage_Guest_Room_Reserved_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_Guest_Room_Reserved_PB.setGeometry(QtCore.QRect(610, 340, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Guest_Room_Reserved_PB.setFont(font)
        self.WelcomePage_Guest_Room_Reserved_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Guest_Room_Reserved_PB.setStyleSheet("background-color: rgb(255, 232, 174);")
        self.WelcomePage_Guest_Room_Reserved_PB.setObjectName("WelcomePage_Guest_Room_Reserved_PB")
        self.WelcomePage_Guest_Birthday_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_Guest_Birthday_PB.setGeometry(QtCore.QRect(320, 720, 531, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Guest_Birthday_PB.setFont(font)
        self.WelcomePage_Guest_Birthday_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Guest_Birthday_PB.setStyleSheet("background-color: rgb(24, 255, 178);")
        self.WelcomePage_Guest_Birthday_PB.setObjectName("WelcomePage_Guest_Birthday_PB")
        self.WelcomePage_Waiting_Reservations_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_Waiting_Reservations_PB.setGeometry(QtCore.QRect(150, 230, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Waiting_Reservations_PB.setFont(font)
        self.WelcomePage_Waiting_Reservations_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Waiting_Reservations_PB.setStyleSheet("background-color: rgb(180, 255, 204);")
        self.WelcomePage_Waiting_Reservations_PB.setObjectName("WelcomePage_Waiting_Reservations_PB")
        self.WelcomePage_list_of_all_reservations_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_list_of_all_reservations_PB.setGeometry(QtCore.QRect(150, 340, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_list_of_all_reservations_PB.setFont(font)
        self.WelcomePage_list_of_all_reservations_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_list_of_all_reservations_PB.setStyleSheet("background-color: rgb(255, 134, 12);")
        self.WelcomePage_list_of_all_reservations_PB.setObjectName("WelcomePage_list_of_all_reservations_PB")
        self.WelcomePage_List_room_status_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_List_room_status_PB.setGeometry(QtCore.QRect(140, 470, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_List_room_status_PB.setFont(font)
        self.WelcomePage_List_room_status_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_List_room_status_PB.setStyleSheet("background-color: rgb(255, 151, 196);")
        self.WelcomePage_List_room_status_PB.setObjectName("WelcomePage_List_room_status_PB")
        self.WelcomePage_Guest_Bill_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_Guest_Bill_PB.setGeometry(QtCore.QRect(610, 230, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Guest_Bill_PB.setFont(font)
        self.WelcomePage_Guest_Bill_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Guest_Bill_PB.setStyleSheet("background-color: rgb(152, 154, 255);")
        self.WelcomePage_Guest_Bill_PB.setObjectName("WelcomePage_Guest_Bill_PB")
        self.WelcomePage_header_L = QtWidgets.QLabel(Recep_WelcomePage)
        self.WelcomePage_header_L.setGeometry(QtCore.QRect(350, 70, 481, 61))
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
        self.WelcomePage_Cleaning_order_reservation_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_Cleaning_order_reservation_PB.setGeometry(QtCore.QRect(610, 470, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Cleaning_order_reservation_PB.setFont(font)
        self.WelcomePage_Cleaning_order_reservation_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Cleaning_order_reservation_PB.setStyleSheet("background-color: rgb(232, 212, 255);")
        self.WelcomePage_Cleaning_order_reservation_PB.setObjectName("WelcomePage_Cleaning_order_reservation_PB")
        self.WelcomePage_Number_Confirmed_Reservation_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_Number_Confirmed_Reservation_PB.setGeometry(QtCore.QRect(130, 590, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Number_Confirmed_Reservation_PB.setFont(font)
        self.WelcomePage_Number_Confirmed_Reservation_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Number_Confirmed_Reservation_PB.setStyleSheet("background-color: rgb(232, 212, 255);")
        self.WelcomePage_Number_Confirmed_Reservation_PB.setObjectName("WelcomePage_Number_Confirmed_Reservation_PB")
        self.WelcomePage_Assign_Staff_PB = QtWidgets.QPushButton(Recep_WelcomePage)
        self.WelcomePage_Assign_Staff_PB.setGeometry(QtCore.QRect(610, 590, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WelcomePage_Assign_Staff_PB.setFont(font)
        self.WelcomePage_Assign_Staff_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.WelcomePage_Assign_Staff_PB.setStyleSheet("background-color: rgb(232, 212, 255);")
        self.WelcomePage_Assign_Staff_PB.setObjectName("WelcomePage_Assign_Staff_PB")

        self.retranslateUi(Recep_WelcomePage)
        QtCore.QMetaObject.connectSlotsByName(Recep_WelcomePage)

        # TODO: Receptionist_Login_Button_Clicked
        self.WelcomePage_Waiting_Reservations_PB.clicked.connect(self.Waiting_Reservations_window)
        # TODO: Receptionist_List_of_All_Reservation_Button_Clicked
        self.WelcomePage_list_of_all_reservations_PB.clicked.connect(self.list_of_all_reservation_window)
        # TODO: Receptionist_List_of_Rooms_By_Their_Status_Button_Clicked
        self.WelcomePage_List_room_status_PB.clicked.connect(self.list_of_rooms_by_their_status_window)
        # TODO: Receptionist_List_of_Rooms_By_Their_Status_Button_Clicked
        self.WelcomePage_Number_Confirmed_Reservation_PB.clicked.connect(self.Number_Confirmed_Reservation_window)
        # TODO: Receptionist_List_of_People_Birth_Button_Clicked
        self.WelcomePage_Guest_Birthday_PB.clicked.connect(self.list_of_people_birthdate_window)
        # TODO: Receptionist_List_of_People_Total_Amount_Button_Clicked
        self.WelcomePage_Guest_Bill_PB.clicked.connect(self.list_of_people_total_amount_window)
        # TODO: Receptionist_CUSTOMER_BOOKING_Button_Clicked
        self.WelcomePage_Guest_Room_Reserved_PB.clicked.connect(self.customer_booking_window)
        # TODO: Receptionist_CLEANING_ORDER_RESERVATION_Button_Clicked
        self.WelcomePage_Cleaning_order_reservation_PB.clicked.connect(self.cleaning_order_reservation_window)
        # TODO: Receptionist_ASSIGN_HOUSEKEEPER_Button_Clicked
        self.WelcomePage_Assign_Staff_PB.clicked.connect(self.assign_housekeeper_window)

    def retranslateUi(self, Recep_WelcomePage):
        staff_detail = read_recep_details()

        _translate = QtCore.QCoreApplication.translate
        Recep_WelcomePage.setWindowTitle(_translate("Recep_WelcomePage", "Receptionist Welcome Page"))
        self.WelcomePage_Guest_Room_Reserved_PB.setText(
            _translate("Recep_WelcomePage", "See All Rooms a Guest Has Reserved"))
        self.WelcomePage_Guest_Birthday_PB.setText(
            _translate("Recep_WelcomePage", "See Guests who Resided in Hotel on Their Birthday"))
        self.WelcomePage_Waiting_Reservations_PB.setText(
            _translate("Recep_WelcomePage", "List of Waiting Reservations"))
        self.WelcomePage_list_of_all_reservations_PB.setText(
            _translate("Recep_WelcomePage", "List of All Reservations"))
        self.WelcomePage_List_room_status_PB.setText(_translate("Recep_WelcomePage", "List of Rooms By Their Status"))
        self.WelcomePage_Guest_Bill_PB.setText(_translate("Recep_WelcomePage", "See Guests with Bills over 1,000,000"))
        self.WelcomePage_header_L.setText(_translate("Recep_WelcomePage", "WELCOME " + staff_detail[1] + " " +
                                                     staff_detail[2] + " TO HOME PAGE"))
        self.WelcomePage_Cleaning_order_reservation_PB.setText(
            _translate("Recep_WelcomePage", "Cleaning Orders of a Reservation"))
        self.WelcomePage_Number_Confirmed_Reservation_PB.setText(
            _translate("Recep_WelcomePage", "Number of Confirmed Reservations"))
        self.WelcomePage_Assign_Staff_PB.setText(_translate("Recep_WelcomePage", "Assign Staff to Cleaning Order"))

    def Waiting_Reservations_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recept_reservation_CC_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def list_of_all_reservation_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recept_reservation_list_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def list_of_rooms_by_their_status_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recept_list_room_status_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def list_of_people_birthdate_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recep_list_of_all_people_birth_date_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def list_of_people_total_amount_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recep_list_of_all_people_bill_account_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def Number_Confirmed_Reservation_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Recept_Number_of_reservation_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def customer_booking_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_customer_booking_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def cleaning_order_reservation_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_cleaning_service_reservation_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def assign_housekeeper_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_cleaning_service_assign_window()
        self.ui.setupUi(self.window)
        self.window.show()

