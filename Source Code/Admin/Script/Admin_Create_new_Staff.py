import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

from Start.DB_Configuration import exe_query


class Ui_Admin_create_new_staff(object):

    def __init__(self):
        self.role = 1

    def setupUi(self, Admin_create_new_staff):
        Admin_create_new_staff.setObjectName("Admin_create_new_staff")
        Admin_create_new_staff.resize(1107, 846)
        Admin_create_new_staff.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        icon = QtGui.QIcon.fromTheme("Icon")
        Admin_create_new_staff.setWindowIcon(icon)
        Admin_create_new_staff.setStyleSheet("background-color: rgb(199, 233, 255);")
        self.create_new_staff_header_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_header_L.setGeometry(QtCore.QRect(360, 30, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_header_L.setFont(font)
        self.create_new_staff_header_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.create_new_staff_header_L.setStyleSheet("background-color: rgb(255, 102, 104);")
        self.create_new_staff_header_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_header_L.setObjectName("create_new_staff_header_L")
        self.create_new_staff_Firstname_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_Firstname_L.setGeometry(QtCore.QRect(100, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Firstname_L.setFont(font)
        self.create_new_staff_Firstname_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                        "color: rgb(245, 243, 255);")
        self.create_new_staff_Firstname_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_Firstname_L.setObjectName("create_new_staff_Firstname_L")
        self.create_new_staff_Family_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_Family_L.setGeometry(QtCore.QRect(580, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Family_L.setFont(font)
        self.create_new_staff_Family_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                     "color: rgb(245, 243, 255);")
        self.create_new_staff_Family_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_Family_L.setObjectName("create_new_staff_Family_L")
        self.create_new_staff_Firstname_LE = QtWidgets.QLineEdit(Admin_create_new_staff)
        self.create_new_staff_Firstname_LE.setGeometry(QtCore.QRect(340, 200, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Firstname_LE.setFont(font)
        self.create_new_staff_Firstname_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_Firstname_LE.setObjectName("create_new_staff_Firstname_LE")
        self.Signup_Button = QtWidgets.QPushButton(Admin_create_new_staff)
        self.Signup_Button.setGeometry(QtCore.QRect(460, 710, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Signup_Button.setFont(font)
        self.Signup_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Signup_Button.setAcceptDrops(False)
        self.Signup_Button.setAutoFillBackground(False)
        self.Signup_Button.setStyleSheet("background-color: rgb(35, 255, 97);")
        self.Signup_Button.setObjectName("Signup_Button")
        self.create_new_staff_Family_LE = QtWidgets.QLineEdit(Admin_create_new_staff)
        self.create_new_staff_Family_LE.setGeometry(QtCore.QRect(800, 200, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Family_LE.setFont(font)
        self.create_new_staff_Family_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_Family_LE.setObjectName("create_new_staff_Family_LE")
        self.create_new_staff_Role_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_Role_L.setGeometry(QtCore.QRect(580, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Role_L.setFont(font)
        self.create_new_staff_Role_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                   "color: rgb(245, 243, 255);")
        self.create_new_staff_Role_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_Role_L.setObjectName("create_new_staff_Role_L")
        self.create_new_staff_StartDate_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_StartDate_L.setGeometry(QtCore.QRect(90, 450, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_StartDate_L.setFont(font)
        self.create_new_staff_StartDate_L.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.create_new_staff_StartDate_L.setStyleSheet("background-color: rgb(7, 85, 127);\n"
                                                        "color: rgb(255, 249, 249);")
        self.create_new_staff_StartDate_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_StartDate_L.setObjectName("create_new_staff_StartDate_L")
        self.create_new_staff_Recep_RD = QtWidgets.QRadioButton(Admin_create_new_staff)
        self.create_new_staff_Recep_RD.setGeometry(QtCore.QRect(800, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Recep_RD.setFont(font)
        self.create_new_staff_Recep_RD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_Recep_RD.setStyleSheet("background-color: rgb(255, 111, 111);")
        self.create_new_staff_Recep_RD.setCheckable(True)
        self.create_new_staff_Recep_RD.setObjectName("create_new_staff_Recep_RD")
        self.create_new_staff_Housekeeper_RD = QtWidgets.QRadioButton(Admin_create_new_staff)
        self.create_new_staff_Housekeeper_RD.setGeometry(QtCore.QRect(950, 290, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Housekeeper_RD.setFont(font)
        self.create_new_staff_Housekeeper_RD.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_Housekeeper_RD.setStyleSheet("background-color: rgb(255, 111, 111);")
        self.create_new_staff_Housekeeper_RD.setIconSize(QtCore.QSize(20, 20))
        self.create_new_staff_Housekeeper_RD.setObjectName("create_new_staff_Housekeeper_RD")
        self.create_new_staff_National_Id_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_National_Id_L.setGeometry(QtCore.QRect(100, 290, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_National_Id_L.setFont(font)
        self.create_new_staff_National_Id_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                          "color: rgb(245, 243, 255);")
        self.create_new_staff_National_Id_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_National_Id_L.setObjectName("create_new_staff_National_Id_L")
        self.create_new_staff_Salary_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_Salary_L.setGeometry(QtCore.QRect(90, 570, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Salary_L.setFont(font)
        self.create_new_staff_Salary_L.setStyleSheet("background-color: rgb(7, 85, 127);\n"
                                                     "color: rgb(255, 249, 249);")
        self.create_new_staff_Salary_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_Salary_L.setObjectName("create_new_staff_Salary_L")
        self.create_new_staff_National_Id_LE = QtWidgets.QLineEdit(Admin_create_new_staff)
        self.create_new_staff_National_Id_LE.setGeometry(QtCore.QRect(340, 290, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_National_Id_LE.setFont(font)
        self.create_new_staff_National_Id_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_National_Id_LE.setObjectName("create_new_staff_National_Id_LE")
        self.Address_LE = QtWidgets.QLineEdit(Admin_create_new_staff)
        self.Address_LE.setGeometry(QtCore.QRect(330, 570, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Address_LE.setFont(font)
        self.Address_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Address_LE.setObjectName("Address_LE")
        self.create_new_staff_startDate_DE = QtWidgets.QDateEdit(Admin_create_new_staff)
        self.create_new_staff_startDate_DE.setGeometry(QtCore.QRect(340, 460, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_startDate_DE.setFont(font)
        self.create_new_staff_startDate_DE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_startDate_DE.setStyleSheet("background-color: rgb(231, 255, 248);")
        self.create_new_staff_startDate_DE.setObjectName("create_new_staff_startDate_DE")
        self.create_new_staff_Email_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_Email_L.setGeometry(QtCore.QRect(100, 370, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Email_L.setFont(font)
        self.create_new_staff_Email_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                    "color: rgb(245, 243, 255);")
        self.create_new_staff_Email_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_Email_L.setObjectName("create_new_staff_Email_L")
        self.create_new_staff_Email_LE = QtWidgets.QLineEdit(Admin_create_new_staff)
        self.create_new_staff_Email_LE.setGeometry(QtCore.QRect(340, 370, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Email_LE.setFont(font)
        self.create_new_staff_Email_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_Email_LE.setObjectName("create_new_staff_Email_LE")
        self.create_new_staff_Password_L = QtWidgets.QLabel(Admin_create_new_staff)
        self.create_new_staff_Password_L.setGeometry(QtCore.QRect(580, 370, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Password_L.setFont(font)
        self.create_new_staff_Password_L.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                                       "color: rgb(245, 243, 255);")
        self.create_new_staff_Password_L.setAlignment(QtCore.Qt.AlignCenter)
        self.create_new_staff_Password_L.setObjectName("create_new_staff_Password_L")
        self.create_new_staff_Password_LE = QtWidgets.QLineEdit(Admin_create_new_staff)
        self.create_new_staff_Password_LE.setGeometry(QtCore.QRect(800, 360, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create_new_staff_Password_LE.setFont(font)
        self.create_new_staff_Password_LE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_new_staff_Password_LE.setObjectName("create_new_staff_Password_LE")

        self.retranslateUi(Admin_create_new_staff)
        QtCore.QMetaObject.connectSlotsByName(Admin_create_new_staff)

        # TODO:ADD_NEW_EMPLOYEE_CLICKED
        self.Signup_Button.clicked.connect(self.add_new_staff)

    def retranslateUi(self, Admin_create_new_staff):
        _translate = QtCore.QCoreApplication.translate
        Admin_create_new_staff.setWindowTitle(_translate("Admin_create_new_staff", "SignUp Page"))
        self.create_new_staff_header_L.setText(_translate("Admin_create_new_staff", "Create new Staff"))
        self.create_new_staff_Firstname_L.setText(_translate("Admin_create_new_staff", "First name"))
        self.create_new_staff_Family_L.setText(_translate("Admin_create_new_staff", "Family"))
        self.Signup_Button.setText(_translate("Admin_create_new_staff", "Create"))
        self.create_new_staff_Role_L.setText(_translate("Admin_create_new_staff", "Role"))
        self.create_new_staff_StartDate_L.setText(_translate("Admin_create_new_staff", "Start Date"))
        self.create_new_staff_Recep_RD.setText(_translate("Admin_create_new_staff", "Receptionist"))
        self.create_new_staff_Housekeeper_RD.setText(_translate("Admin_create_new_staff", "Housekeeper"))
        self.create_new_staff_National_Id_L.setText(_translate("Admin_create_new_staff", "National Id"))
        self.create_new_staff_Salary_L.setText(_translate("Admin_create_new_staff", "Salary"))
        self.create_new_staff_Email_L.setText(_translate("Admin_create_new_staff", "Email"))
        self.create_new_staff_Password_L.setText(_translate("Admin_create_new_staff", "Password"))

    def add_new_staff(self):

        if self.create_new_staff_Housekeeper_RD.isChecked():
            self.role = 0

        year = self.create_new_staff_startDate_DE.date().year()
        month = self.create_new_staff_startDate_DE.date().month()
        day = self.create_new_staff_startDate_DE.date().day()
        start_date = datetime.datetime(year, month, day).isoformat()

        exe_query(f""" 
                        INSERT INTO staff_information(Staff_Firstname, Staff_Lastname, Staff_Password, Staff_Email, 
                                                Staff_National_ID,Staff_Salary, Staff_StartDate, 
                                                Staff_Role_Recep_Cleaning)
                                                        VALUES
                         ('{self.create_new_staff_Firstname_LE.text()}','{self.create_new_staff_Family_LE.text()}',
                         '{self.create_new_staff_Password_LE.text()}','{self.create_new_staff_Email_LE.text()}',
                         '{self.create_new_staff_National_Id_LE.text()}',
                         '{self.Address_LE.text()}','{start_date}',{self.role});
                        """)


