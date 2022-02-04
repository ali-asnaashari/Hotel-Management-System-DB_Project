from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

from Start.DB_Configuration import exe_query


class Ui_Recept_Number_of_reservation_window(object):

    def __init__(self):
        self.count = 0

    def setupUi(self, Recept_Number_of_reservation_window):
        Recept_Number_of_reservation_window.setObjectName("Recept_Number_of_reservation_window")
        Recept_Number_of_reservation_window.resize(1094, 846)
        Recept_Number_of_reservation_window.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        Recept_Number_of_reservation_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.Recept_Number_of_reservation_DateEditOne = QtWidgets.QDateEdit(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_DateEditOne.setGeometry(QtCore.QRect(360, 280, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_DateEditOne.setFont(font)
        self.Recept_Number_of_reservation_DateEditOne.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Recept_Number_of_reservation_DateEditOne.setStyleSheet("background-color: rgb(133, 196, 255);")
        self.Recept_Number_of_reservation_DateEditOne.setObjectName("Recept_Number_of_reservation_DateEditOne")
        self.Recept_Number_of_reservation_DateEditTwo = QtWidgets.QDateEdit(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_DateEditTwo.setGeometry(QtCore.QRect(800, 280, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_DateEditTwo.setFont(font)
        self.Recept_Number_of_reservation_DateEditTwo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Recept_Number_of_reservation_DateEditTwo.setStyleSheet("background-color: rgb(133, 196, 255);")
        self.Recept_Number_of_reservation_DateEditTwo.setObjectName("Recept_Number_of_reservation_DateEditTwo")
        self.Recept_Number_of_reservation_from_L = QtWidgets.QLabel(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_from_L.setGeometry(QtCore.QRect(180, 280, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_from_L.setFont(font)
        self.Recept_Number_of_reservation_from_L.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Recept_Number_of_reservation_from_L.setStyleSheet("background-color: rgb(219, 255, 255);")
        self.Recept_Number_of_reservation_from_L.setFrameShape(QtWidgets.QFrame.Panel)
        self.Recept_Number_of_reservation_from_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Recept_Number_of_reservation_from_L.setObjectName("Recept_Number_of_reservation_from_L")
        self.Recept_Number_of_reservation_to_L = QtWidgets.QLabel(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_to_L.setGeometry(QtCore.QRect(620, 280, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_to_L.setFont(font)
        self.Recept_Number_of_reservation_to_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Recept_Number_of_reservation_to_L.setStyleSheet("background-color: rgb(219, 255, 255);")
        self.Recept_Number_of_reservation_to_L.setFrameShape(QtWidgets.QFrame.Panel)
        self.Recept_Number_of_reservation_to_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Recept_Number_of_reservation_to_L.setObjectName("Recept_Number_of_reservation_to_L")
        self.Recept_Number_of_reservation_header_L = QtWidgets.QLabel(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_header_L.setGeometry(QtCore.QRect(370, 60, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_header_L.setFont(font)
        self.Recept_Number_of_reservation_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Recept_Number_of_reservation_header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.Recept_Number_of_reservation_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Recept_Number_of_reservation_header_L.setObjectName("Recept_Number_of_reservation_header_L")
        self.Recept_Number_of_reservation_enter_PB = QtWidgets.QPushButton(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_enter_PB.setGeometry(QtCore.QRect(440, 470, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_enter_PB.setFont(font)
        self.Recept_Number_of_reservation_enter_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Recept_Number_of_reservation_enter_PB.setStyleSheet("background-color: rgb(24, 255, 78);")
        self.Recept_Number_of_reservation_enter_PB.setObjectName("Recept_Number_of_reservation_enter_PB")
        self.Recept_Number_of_reservation_Count_LE = QtWidgets.QLineEdit(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_Count_LE.setGeometry(QtCore.QRect(580, 680, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_Count_LE.setFont(font)
        self.Recept_Number_of_reservation_Count_LE.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Recept_Number_of_reservation_Count_LE.setObjectName("Recept_Number_of_reservation_Count_LE")
        self.Recept_Number_of_reservation_Count_L = QtWidgets.QLabel(Recept_Number_of_reservation_window)
        self.Recept_Number_of_reservation_Count_L.setGeometry(QtCore.QRect(330, 680, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Recept_Number_of_reservation_Count_L.setFont(font)
        self.Recept_Number_of_reservation_Count_L.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Recept_Number_of_reservation_Count_L.setStyleSheet("background-color: rgb(255, 210, 73);")
        self.Recept_Number_of_reservation_Count_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Recept_Number_of_reservation_Count_L.setObjectName("Recept_Number_of_reservation_Count_L")

        self.retranslateUi(Recept_Number_of_reservation_window)
        QtCore.QMetaObject.connectSlotsByName(Recept_Number_of_reservation_window)

        # TODO: Receptionist_Enter_Clicked
        self.Recept_Number_of_reservation_enter_PB.clicked.connect(self.show_number_of_reservation)

    def retranslateUi(self, Recept_Number_of_reservation_window):
        _translate = QtCore.QCoreApplication.translate
        Recept_Number_of_reservation_window.setWindowTitle(
            _translate("Recept_Number_of_reservation_window", "Number of reservation"))
        self.Recept_Number_of_reservation_from_L.setText(_translate("Recept_Number_of_reservation_window", "from"))
        self.Recept_Number_of_reservation_to_L.setText(_translate("Recept_Number_of_reservation_window", "to"))
        self.Recept_Number_of_reservation_header_L.setText(
            _translate("Recept_Number_of_reservation_window", "Number of Reservations"))
        self.Recept_Number_of_reservation_enter_PB.setText(_translate("Recept_Number_of_reservation_window", "Enter"))
        self.Recept_Number_of_reservation_Count_L.setText(_translate("Recept_Number_of_reservation_window", "Count"))

    def show_number_of_reservation(self):
        year = self.Recept_Number_of_reservation_DateEditOne.date().year()
        month = self.Recept_Number_of_reservation_DateEditOne.date().month()
        day = self.Recept_Number_of_reservation_DateEditOne.date().day()
        Date_From = datetime.datetime(year, month, day).isoformat()

        year1 = self.Recept_Number_of_reservation_DateEditTwo.date().year()
        month1 = self.Recept_Number_of_reservation_DateEditTwo.date().month()
        day1 = self.Recept_Number_of_reservation_DateEditTwo.date().day()
        Date_To = datetime.datetime(year1, month1, day1).isoformat()

        self.count = exe_query(f""" 
                                    SELECT COUNT(Reservation_ID) FROM reservation
                                    JOIN booking_status ON 
                                    reservation.Booking_Status_ID = booking_status.Booking_Status_ID
                                    WHERE reservation.Booking_Status_ID = 2 AND Reservation_Date 
                                    BETWEEN '{Date_From}' AND '{Date_To}';
                            """)

        self.Recept_Number_of_reservation_Count_LE.setText(str(self.count[0][0]))
