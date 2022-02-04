from PyQt5 import QtCore, QtGui, QtWidgets
from Start.DB_Configuration import exe_query
from User.Script.Guest_WelcomePage import Ui_GuestWelcomePage
import csv

class Ui_loginPage(object):

    def setupUi(self, loginPage):
        loginPage.setObjectName("loginPage")
        loginPage.resize(1023, 688)
        loginPage.setStyleSheet("\n"
                                "color: rgb(0, 0, 0);\n"
                                "")
        loginPage.setWindowFilePath("")
        self.Login_Button = QtWidgets.QPushButton(loginPage)
        self.Login_Button.setGeometry(QtCore.QRect(390, 480, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Login_Button.setFont(font)
        self.Login_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Login_Button.setAcceptDrops(False)
        self.Login_Button.setAutoFillBackground(False)
        self.Login_Button.setStyleSheet("background-color: rgb(208, 209, 255);\n"
                                        "color: rgb(102, 64, 255);")
        self.Login_Button.setObjectName("Login_Button")
        self.Login_nationalCode_L = QtWidgets.QLabel(loginPage)
        self.Login_nationalCode_L.setGeometry(QtCore.QRect(250, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Login_nationalCode_L.setFont(font)
        self.Login_nationalCode_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                "color: rgb(245, 243, 255);")
        self.Login_nationalCode_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_nationalCode_L.setObjectName("Login_nationalCode_L")
        self.Login_nationalCode_LE = QtWidgets.QLineEdit(loginPage)
        self.Login_nationalCode_LE.setGeometry(QtCore.QRect(480, 240, 311, 41))
        self.Login_nationalCode_LE.setObjectName("Login_nationalCode_LE")
        self.label_2 = QtWidgets.QLabel(loginPage)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.label_2.setStyleSheet("background-color: rgb(255, 102, 104);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Login_password_L = QtWidgets.QLabel(loginPage)
        self.Login_password_L.setGeometry(QtCore.QRect(250, 330, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Login_password_L.setFont(font)
        self.Login_password_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                            "color: rgb(245, 243, 255);")
        self.Login_password_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Login_password_L.setObjectName("Login_password_L")
        self.Login_password_LE = QtWidgets.QLineEdit(loginPage)
        self.Login_password_LE.setGeometry(QtCore.QRect(480, 330, 311, 41))
        self.Login_password_LE.setObjectName("Login_password_LE")

        self.retranslateUi(loginPage)
        QtCore.QMetaObject.connectSlotsByName(loginPage)

        # TODO:Login_Clicked
        self.Login_Button.clicked.connect(self.login)

    def retranslateUi(self, loginPage):
        _translate = QtCore.QCoreApplication.translate
        loginPage.setWindowTitle(_translate("loginPage", "LoginPage"))
        self.Login_Button.setText(_translate("loginPage", "Login"))
        self.Login_nationalCode_L.setText(_translate("loginPage", "Natinal Code"))
        self.label_2.setText(_translate("loginPage", "Welcome To Guest Registeration Page"))
        self.Login_password_L.setText(_translate("loginPage", "Password"))

    def login(self):
        res = exe_query(f""" 
                     SELECT * FROM guest
                        WHERE Guest_National_ID = '{self.Login_nationalCode_LE.text()}'  
                        AND 
                        Guest_Password = '{self.Login_password_LE.text()}' ; 
                   """)

        if len(res) != 0:
            with open("../User/Script/File/guest_details.csv", "w") as File:
                csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
                writer = csv.writer(File, dialect="custom")
                writer.writerow(res[0])

            self.Guest_Dashboard_Window()

    def Guest_Dashboard_Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GuestWelcomePage()
        self.ui.setupUi(self.window)
        self.window.show()
