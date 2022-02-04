import csv

from PyQt5 import QtCore, QtGui, QtWidgets

from Receptionist.script.Recep_WelcomePage import Ui_Recep_WelcomePage
from Start.DB_Configuration import exe_query


class Ui_recep_login_window(object):

    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Recep_WelcomePage()

    def setupUi(self, recep_login_window):
        recep_login_window.setObjectName("recep_login_window")
        recep_login_window.resize(1023, 688)
        recep_login_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        recep_login_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        recep_login_window.setWindowFilePath("")
        self.recep_login_button = QtWidgets.QPushButton(recep_login_window)
        self.recep_login_button.setGeometry(QtCore.QRect(410, 480, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.recep_login_button.setFont(font)
        self.recep_login_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recep_login_button.setAcceptDrops(False)
        self.recep_login_button.setAutoFillBackground(False)
        self.recep_login_button.setStyleSheet("background-color: rgb(161, 255, 103);")
        self.recep_login_button.setObjectName("recep_login_button")
        self.recep_login_email_L = QtWidgets.QLabel(recep_login_window)
        self.recep_login_email_L.setGeometry(QtCore.QRect(250, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recep_login_email_L.setFont(font)
        self.recep_login_email_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(245, 243, 255);")
        self.recep_login_email_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recep_login_email_L.setObjectName("recep_login_email_L")
        self.recep_login_email_LE = QtWidgets.QLineEdit(recep_login_window)
        self.recep_login_email_LE.setGeometry(QtCore.QRect(480, 240, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recep_login_email_LE.setFont(font)
        self.recep_login_email_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recep_login_email_LE.setObjectName("recep_login_email_LE")
        self.recep_login_header_L = QtWidgets.QLabel(recep_login_window)
        self.recep_login_header_L.setGeometry(QtCore.QRect(280, 60, 541, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.recep_login_header_L.setFont(font)
        self.recep_login_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.recep_login_header_L.setStyleSheet("background-color: rgb(255, 102, 104);")
        self.recep_login_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recep_login_header_L.setObjectName("recep_login_header_L")
        self.recep_login_password_L = QtWidgets.QLabel(recep_login_window)
        self.recep_login_password_L.setGeometry(QtCore.QRect(250, 330, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recep_login_password_L.setFont(font)
        self.recep_login_password_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(245, 243, 255);")
        self.recep_login_password_L.setAlignment(QtCore.Qt.AlignCenter)
        self.recep_login_password_L.setObjectName("recep_login_password_L")
        self.recep_login_password_LE = QtWidgets.QLineEdit(recep_login_window)
        self.recep_login_password_LE.setGeometry(QtCore.QRect(480, 330, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recep_login_password_LE.setFont(font)
        self.recep_login_password_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recep_login_password_LE.setObjectName("recep_login_password_LE")

        self.retranslateUi(recep_login_window)
        QtCore.QMetaObject.connectSlotsByName(recep_login_window)

        # TODO: Receptionist_Login_Button_Clicked
        self.recep_login_button.clicked.connect(self.recep_login)

    def retranslateUi(self, recep_login_window):
        _translate = QtCore.QCoreApplication.translate
        recep_login_window.setWindowTitle(_translate("recep_login_window", "Login page"))
        self.recep_login_button.setText(_translate("recep_login_window", "Login"))
        self.recep_login_email_L.setText(_translate("recep_login_window", "Email"))
        self.recep_login_header_L.setText(_translate("recep_login_window", "Welcome To Receptionist Login Page"))
        self.recep_login_password_L.setText(_translate("recep_login_window", "Password"))

    def recep_login(self):

        res = exe_query(f""" 
                     SELECT * FROM staff_information
                        WHERE Staff_Email = '{self.recep_login_email_LE.text()}'  
                        AND 
                        Staff_Password = '{self.recep_login_password_LE.text()}' ; 
                   """)


        if len(res) != 0:
            with open("../Receptionist/script/File/recep_details.csv", "w") as File:
                csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
                writer = csv.writer(File, dialect="custom")
                writer.writerow(res[0])

            self.Recep_Dashboard_Window()

    def Recep_Dashboard_Window(self):
        self.ui.setupUi(self.window)
        self.window.show()
