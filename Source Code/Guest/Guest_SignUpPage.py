from PyQt5 import QtCore, QtGui, QtWidgets
from User.DB_Configuration import exe_query

from User.Guest_LoginPage import Ui_loginPage
import datetime


class Ui_Dialog(object):

    def __init__(self):
        self.Firstname_LE = QtWidgets.QLineEdit()
        self.Family_LE = QtWidgets.QLineEdit()
        self.Signup_Button = QtWidgets.QPushButton()
        self.Login_Button = QtWidgets.QPushButton()
        self.male_RD = QtWidgets.QRadioButton()
        self.female_RD = QtWidgets.QRadioButton()
        self.BirthDate_L = QtWidgets.QLabel()
        self.Phone_LE = QtWidgets.QLineEdit()
        self.Password_LE = QtWidgets.QLineEdit()
        self.National_LE = QtWidgets.QLineEdit()
        self.Address_LE = QtWidgets.QLineEdit()
        self.BirthDate_DE = QtWidgets.QDateEdit()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1107, 846)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        icon = QtGui.QIcon.fromTheme("Icon")
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)

        self.Firstname_LE = QtWidgets.QLineEdit(Dialog)
        self.Family_LE = QtWidgets.QLineEdit(Dialog)
        self.Signup_Button = QtWidgets.QPushButton(Dialog)
        self.Login_Button = QtWidgets.QPushButton(Dialog)
        self.male_RD = QtWidgets.QRadioButton(Dialog)
        self.female_RD = QtWidgets.QRadioButton(Dialog)
        self.BirthDate_L = QtWidgets.QLabel(Dialog)
        self.Phone_LE = QtWidgets.QLineEdit(Dialog)
        self.Password_LE = QtWidgets.QLineEdit(Dialog)
        self.National_LE = QtWidgets.QLineEdit(Dialog)
        self.Address_LE = QtWidgets.QLineEdit(Dialog)
        self.BirthDate_DE = QtWidgets.QDateEdit(Dialog)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 30, 471, 71))
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
        self.Firstname_L = QtWidgets.QLabel(Dialog)
        self.Firstname_L.setGeometry(QtCore.QRect(100, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Firstname_L.setFont(font)
        self.Firstname_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                       "color: rgb(245, 243, 255);")
        self.Firstname_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Firstname_L.setObjectName("Firstname_L")
        self.Family_L = QtWidgets.QLabel(Dialog)
        self.Family_L.setGeometry(QtCore.QRect(580, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Family_L.setFont(font)
        self.Family_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                    "color: rgb(245, 243, 255);")
        self.Family_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Family_L.setObjectName("Family_L")

        self.Firstname_LE.setGeometry(QtCore.QRect(340, 200, 191, 41))
        self.Firstname_LE.setObjectName("Firstname_LE")

        self.Signup_Button.setGeometry(QtCore.QRect(250, 680, 251, 71))
        self.Login_Button.setGeometry(QtCore.QRect(650, 680, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Signup_Button.setFont(font)
        self.Signup_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Signup_Button.setAcceptDrops(False)
        self.Signup_Button.setAutoFillBackground(False)
        self.Signup_Button.setStyleSheet("background-color: rgb(208, 209, 255);\n"
                                         "color: rgb(102, 64, 255);")
        self.Signup_Button.setObjectName("Signup_Button")

        self.Login_Button.setFont(font)
        self.Login_Button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Login_Button.setAcceptDrops(False)
        self.Login_Button.setAutoFillBackground(False)
        self.Login_Button.setStyleSheet("background-color: rgb(208, 209, 255);\n"
                                        "color: rgb(102, 64, 255);")
        self.Login_Button.setObjectName("Login_Button")

        self.Family_LE.setGeometry(QtCore.QRect(800, 200, 271, 41))
        self.Family_LE.setObjectName("Family_LE")
        self.Gender_L = QtWidgets.QLabel(Dialog)
        self.Gender_L.setGeometry(QtCore.QRect(580, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Gender_L.setFont(font)
        self.Gender_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                    "color: rgb(245, 243, 255);")
        self.Gender_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Gender_L.setObjectName("Gender_L")

        self.BirthDate_L.setGeometry(QtCore.QRect(90, 450, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BirthDate_L.setFont(font)
        self.BirthDate_L.setStyleSheet("background-color: rgb(7, 85, 127);\n"
                                       "color: rgb(255, 249, 249);")
        self.BirthDate_L.setAlignment(QtCore.Qt.AlignCenter)
        self.BirthDate_L.setObjectName("BirthDate_L")

        self.male_RD.setGeometry(QtCore.QRect(800, 290, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.male_RD.setFont(font)
        self.male_RD.setStyleSheet("background-color: rgb(255, 111, 111);")
        self.male_RD.setCheckable(True)
        self.male_RD.setObjectName("male_RD")

        self.female_RD.setGeometry(QtCore.QRect(950, 290, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.female_RD.setFont(font)
        self.female_RD.setStyleSheet("background-color: rgb(255, 111, 111);")
        self.female_RD.setIconSize(QtCore.QSize(20, 20))
        self.female_RD.setObjectName("female_RD")
        self.Phone_L = QtWidgets.QLabel(Dialog)
        self.Phone_L.setGeometry(QtCore.QRect(100, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Phone_L.setFont(font)
        self.Phone_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                   "color: rgb(245, 243, 255);")
        self.Phone_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Phone_L.setObjectName("Phone_L")
        self.Address_L = QtWidgets.QLabel(Dialog)
        self.Address_L.setGeometry(QtCore.QRect(90, 570, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Address_L.setFont(font)
        self.Address_L.setStyleSheet("background-color: rgb(7, 85, 127);\n"
                                     "color: rgb(255, 249, 249);")
        self.Address_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Address_L.setObjectName("Address_L")

        self.Phone_LE.setGeometry(QtCore.QRect(340, 290, 191, 41))
        self.Phone_LE.setObjectName("Phone_LE")

        self.Address_LE.setGeometry(QtCore.QRect(330, 570, 321, 51))
        self.Address_LE.setObjectName("Address_LE")

        self.BirthDate_DE.setGeometry(QtCore.QRect(340, 460, 191, 41))
        self.BirthDate_DE.setObjectName("BirthDate_DE")
        self.National_L = QtWidgets.QLabel(Dialog)
        self.National_L.setGeometry(QtCore.QRect(100, 370, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.National_L.setFont(font)
        self.National_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                      "color: rgb(245, 243, 255);")
        self.National_L.setAlignment(QtCore.Qt.AlignCenter)
        self.National_L.setObjectName("National_L")

        self.National_LE.setGeometry(QtCore.QRect(340, 370, 191, 41))
        self.National_LE.setObjectName("National_LE")
        self.Password_L = QtWidgets.QLabel(Dialog)
        self.Password_L.setGeometry(QtCore.QRect(580, 370, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Password_L.setFont(font)
        self.Password_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                      "color: rgb(245, 243, 255);")
        self.Password_L.setAlignment(QtCore.Qt.AlignCenter)
        self.Password_L.setObjectName("Password_L")

        self.Password_LE.setGeometry(QtCore.QRect(800, 360, 271, 51))
        self.Password_LE.setObjectName("Password_LE")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # signUp_Clicked
        self.Signup_Button.clicked.connect(self.Fill_Guest_Information)

        # login_Clicked
        self.Login_Button.clicked.connect(self.Guest_Login_Window)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SignUp Page"))
        self.label_2.setText(_translate("Dialog", "Welcome To Guest Registeration Page"))
        self.Firstname_L.setText(_translate("Dialog", "First name"))
        self.Family_L.setText(_translate("Dialog", "Family"))
        self.Signup_Button.setText(_translate("Dialog", "Sign up"))
        self.Login_Button.setText(_translate("Dialog", "Log in"))
        self.Gender_L.setText(_translate("Dialog", "Gender"))
        self.BirthDate_L.setText(_translate("Dialog", "Birth Date"))
        self.male_RD.setText(_translate("Dialog", "Male"))
        self.female_RD.setText(_translate("Dialog", "Female"))
        self.Phone_L.setText(_translate("Dialog", "Phone.No"))
        self.Address_L.setText(_translate("Dialog", "Address"))
        self.National_L.setText(_translate("Dialog", "National ID"))
        self.Password_L.setText(_translate("Dialog", "Password"))

    def Fill_Guest_Information(self):
        gender = 0
        if self.male_RD.isChecked():
            gender = 1

        year = self.BirthDate_DE.date().year()
        month = self.BirthDate_DE.date().month()
        day = self.BirthDate_DE.date().day()
        str_now = datetime.datetime(year, month, day).isoformat()

        if (self.Firstname_LE.text() != '') and (self.Family_LE.text() != '') and (self.Password_LE.text() != '') and \
                (self.Phone_LE.text() != '') and (self.Address_LE.text() != '') and (self.National_LE.text() != ''):

            exe_query(f""" 
                          INSERT INTO guest 
                          (Guest_Firstname,Guest_Lastname,Guest_Password,Guest_PhoneNumber,
                           Guest_Address,Guest_BirthDate,Guest_Gender,Guest_National_ID) 
                                              VALUES
                          ('{self.Firstname_LE.text()}','{self.Family_LE.text()}','{self.Password_LE.text()}',
                           '{self.Phone_LE.text()}','{self.Address_LE.text()}' ,
                           '{str_now}', {gender},'{self.National_LE.text()}'); 
                       """)

            print("Registration Successful")
            self.Guest_Login_Window()

        else:
            print("Registration Failed")

    def Guest_Login_Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_loginPage()
        self.ui.setupUi(self.window)
        self.window.show()
