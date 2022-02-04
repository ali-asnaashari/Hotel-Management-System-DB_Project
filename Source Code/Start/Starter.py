from PyQt5 import QtCore, QtGui, QtWidgets

from Admin.Script.Admin_WelcomePage import Ui_Admin_WelcomePage
from Receptionist.script.Recep_LoginPage import Ui_recep_login_window
from User.Script.Guest_SignUpPage import Ui_Guest_signup_page


class Ui_starter_window(object):

    def setupUi(self, starter_window):
        starter_window.setObjectName("starter_window")
        starter_window.resize(1069, 666)
        starter_window.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        starter_window.setStyleSheet("background-color: rgb(197, 223, 255);")
        self.starter_Header_L = QtWidgets.QLabel(starter_window)
        self.starter_Header_L.setGeometry(QtCore.QRect(350, 80, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.starter_Header_L.setFont(font)
        self.starter_Header_L.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.starter_Header_L.setStyleSheet("background-color: rgb(255, 97, 100);")
        self.starter_Header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.starter_Header_L.setObjectName("starter_Header_L")
        self.starter_Recep_PB = QtWidgets.QPushButton(starter_window)
        self.starter_Recep_PB.setGeometry(QtCore.QRect(410, 380, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.starter_Recep_PB.setFont(font)
        self.starter_Recep_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.starter_Recep_PB.setStyleSheet("background-color: rgb(255, 148, 200);")
        self.starter_Recep_PB.setObjectName("starter_Recep_PB")
        self.starter_Guest_PB = QtWidgets.QPushButton(starter_window)
        self.starter_Guest_PB.setGeometry(QtCore.QRect(410, 530, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.starter_Guest_PB.setFont(font)
        self.starter_Guest_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.starter_Guest_PB.setStyleSheet("background-color: rgb(179, 25, 255);\n"
                                            "color: rgb(255, 255, 255);")
        self.starter_Guest_PB.setObjectName("starter_Guest_PB")
        self.starter_Admin_PB = QtWidgets.QPushButton(starter_window)
        self.starter_Admin_PB.setGeometry(QtCore.QRect(410, 230, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.starter_Admin_PB.setFont(font)
        self.starter_Admin_PB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.starter_Admin_PB.setStyleSheet("background-color: rgb(16, 52, 255);\n"
                                            "color: rgb(255, 255, 255);")
        self.starter_Admin_PB.setObjectName("starter_Admin_PB")

        self.retranslateUi(starter_window)
        QtCore.QMetaObject.connectSlotsByName(starter_window)

        # TODO:Receptionist Login Page
        self.starter_Recep_PB.clicked.connect(self.show_receptionist_login_page)

        # TODO:Guest Signup Page
        self.starter_Guest_PB.clicked.connect(self.show_guest_signup_page)

        # TODO:Admin Signup Page
        self.starter_Admin_PB.clicked.connect(self.show_admin_welcome_page_page)

    def retranslateUi(self, starter_window):
        _translate = QtCore.QCoreApplication.translate
        starter_window.setWindowTitle(_translate("starter_window", "Starter"))
        self.starter_Header_L.setText(_translate("starter_window", "Hi. I\'m a ..."))
        self.starter_Recep_PB.setText(_translate("starter_window", "Receptionist"))
        self.starter_Guest_PB.setText(_translate("starter_window", "Guest"))
        self.starter_Admin_PB.setText(_translate("starter_window", "Admin"))

    def show_receptionist_login_page(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recep_login_window()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_guest_signup_page(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Guest_signup_page()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_admin_welcome_page_page(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Admin_WelcomePage()
        self.ui.setupUi(self.window)
        self.window.show()