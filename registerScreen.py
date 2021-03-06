import databaseOperation
from PyQt5 import QtCore, QtGui, QtWidgets
from userAddQuestion import Ui_FormQuestion

class Ui_txtRegisterScreen(object):
    tcNumber=''
    firstName=''
    lastName=''
    password=''
    birthday=''
    address=''
    dialog=''


    def setupUi(self, txtRegisterScreen):
        txtRegisterScreen.setObjectName("txtRegisterScreen")
        txtRegisterScreen.setWindowModality(QtCore.Qt.WindowModal)
        txtRegisterScreen.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(txtRegisterScreen.sizePolicy().hasHeightForWidth())
        txtRegisterScreen.setSizePolicy(sizePolicy)
        txtRegisterScreen.setMinimumSize(QtCore.QSize(400, 500))
        txtRegisterScreen.setMaximumSize(QtCore.QSize(400, 500))
        txtRegisterScreen.setSizeIncrement(QtCore.QSize(400, 500))
        txtRegisterScreen.setBaseSize(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        txtRegisterScreen.setFont(font)
        txtRegisterScreen.setMouseTracking(True)
        txtRegisterScreen.setFocusPolicy(QtCore.Qt.ClickFocus)
        #txtRegisterScreen.setSizeGripEnabled(False)
        #txtRegisterScreen.setModal(False)
        self.label_3 = QtWidgets.QLabel(txtRegisterScreen)
        self.label_3.setGeometry(QtCore.QRect(133, 9, 16, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.txtTcNumber_2 = QtWidgets.QLabel(txtRegisterScreen)
        self.txtTcNumber_2.setGeometry(QtCore.QRect(10, 60, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtTcNumber_2.setFont(font)
        self.txtTcNumber_2.setObjectName("txtTcNumber_2")
        self.lnPasswordNumber = QtWidgets.QLineEdit(txtRegisterScreen)
        self.lnPasswordNumber.setGeometry(QtCore.QRect(120, 240, 201, 20))
        self.lnPasswordNumber.setToolTipDuration(1)
        self.lnPasswordNumber.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lnPasswordNumber.setMaxLength(16)
        self.lnPasswordNumber.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lnPasswordNumber.setClearButtonEnabled(True)
        self.lnPasswordNumber.setObjectName("lnPasswordNumber")
        self.lnTcNumber = QtWidgets.QLineEdit(txtRegisterScreen)
        self.lnTcNumber.setGeometry(QtCore.QRect(120, 60, 201, 20))
        self.lnTcNumber.setMinimumSize(QtCore.QSize(0, 0))
        self.lnTcNumber.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.lnTcNumber.setMaxLength(11)
        self.lnTcNumber.setClearButtonEnabled(True)
        self.lnTcNumber.setProperty("numberOnly", "")
        self.lnTcNumber.setObjectName("lnTcNumber")
        self.lnName = QtWidgets.QLineEdit(txtRegisterScreen)
        self.lnName.setGeometry(QtCore.QRect(120, 120, 201, 20))
        self.lnName.setMaxLength(20)
        self.lnName.setClearButtonEnabled(True)
        self.lnName.setObjectName("lnName")
        self.lnNameP = QtWidgets.QLineEdit(txtRegisterScreen)
        self.lnNameP.setGeometry(QtCore.QRect(120, 180, 201, 20))
        self.lnNameP.setMaxLength(20)
        self.lnNameP.setClearButtonEnabled(True)
        self.lnNameP.setObjectName("lnNameP")
        self.txtName = QtWidgets.QLabel(txtRegisterScreen)
        self.txtName.setGeometry(QtCore.QRect(10, 120, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtName.setFont(font)
        self.txtName.setObjectName("txtName")
        self.txtNameP = QtWidgets.QLabel(txtRegisterScreen)
        self.txtNameP.setGeometry(QtCore.QRect(10, 180, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtNameP.setFont(font)
        self.txtNameP.setObjectName("txtNameP")
        self.txtPasswordNumber = QtWidgets.QLabel(txtRegisterScreen)
        self.txtPasswordNumber.setGeometry(QtCore.QRect(10, 240, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtPasswordNumber.setFont(font)
        self.txtPasswordNumber.setObjectName("txtPasswordNumber")
        self.txtDateTime = QtWidgets.QLabel(txtRegisterScreen)
        self.txtDateTime.setGeometry(QtCore.QRect(10, 290, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtDateTime.setFont(font)
        self.txtDateTime.setObjectName("txtDateTime")
        self.txtAddress = QtWidgets.QLabel(txtRegisterScreen)
        self.txtAddress.setGeometry(QtCore.QRect(10, 360, 71, 16))
        self.txtAddress.setMaximumSize(QtCore.QSize(1000, 1000))
        self.txtAddress.setSizeIncrement(QtCore.QSize(1000, 1000))
        self.txtAddress.setBaseSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtAddress.setFont(font)
        self.txtAddress.setObjectName("txtAddress")
        self.lnDateTime = QtWidgets.QDateEdit(txtRegisterScreen)
        self.lnDateTime.setGeometry(QtCore.QRect(120, 290, 201, 22))
        self.lnDateTime.setProperty("showGroupSeparator", True)
        self.lnDateTime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2050, 12, 31), QtCore.QTime(17, 59, 59)))
        self.lnDateTime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1910, 9, 12), QtCore.QTime(21, 0, 0)))
        self.lnDateTime.setMaximumTime(QtCore.QTime(17, 59, 59))
        self.lnDateTime.setMinimumTime(QtCore.QTime(21, 0, 0))
        self.lnDateTime.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.lnDateTime.setCalendarPopup(True)
        self.lnDateTime.setCurrentSectionIndex(0)
        self.lnDateTime.setTimeSpec(QtCore.Qt.UTC)
        self.lnDateTime.setDate(QtCore.QDate(2019, 12, 3))
        self.lnDateTime.setObjectName("lnDateTime")
        self.lnAddress = QtWidgets.QLineEdit(txtRegisterScreen)
        self.lnAddress.setGeometry(QtCore.QRect(120, 360, 201, 81))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.lnAddress.setFont(font)
        self.lnAddress.setToolTip("")
        self.lnAddress.setToolTipDuration(0)
        self.lnAddress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lnAddress.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lnAddress.setText("")
        self.lnAddress.setMaxLength(100)
        self.lnAddress.setCursorPosition(0)
        self.lnAddress.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lnAddress.setClearButtonEnabled(True)
        self.lnAddress.setObjectName("lnAddress")
        self.btnRegisterButton = QtWidgets.QPushButton(txtRegisterScreen)
        self.btnRegisterButton.setGeometry(QtCore.QRect(164, 460, 101, 31))
        self.btnRegisterButton.clicked.connect(self.registerUser) #kay??t komutu
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRegisterButton.sizePolicy().hasHeightForWidth())
        self.btnRegisterButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegisterButton.setFont(font)
        self.btnRegisterButton.setObjectName("btnRegisterButton")

        self.retranslateUi(txtRegisterScreen)
        QtCore.QMetaObject.connectSlotsByName(txtRegisterScreen)
        txtRegisterScreen.setTabOrder(self.lnTcNumber, self.lnName)
        txtRegisterScreen.setTabOrder(self.lnName, self.lnDateTime)
        txtRegisterScreen.setTabOrder(self.lnDateTime, self.lnPasswordNumber)
        txtRegisterScreen.setTabOrder(self.lnPasswordNumber, self.lnAddress)
        txtRegisterScreen.setTabOrder(self.lnAddress, self.lnNameP)
        self.dialog=txtRegisterScreen

    def retranslateUi(self, txtRegisterScreen):
        _translate = QtCore.QCoreApplication.translate
        txtRegisterScreen.setWindowTitle(_translate("txtRegisterScreen", "Kay??t Ekran??"))
        self.txtTcNumber_2.setText(_translate("txtRegisterScreen", "T.C. K??ML??K NO"))
        self.txtName.setText(_translate("txtRegisterScreen", "ADI"))
        self.txtNameP.setText(_translate("txtRegisterScreen", "SOYADI"))
        self.txtPasswordNumber.setText(_translate("txtRegisterScreen", "????FRE"))
        self.txtDateTime.setText(_translate("txtRegisterScreen", "DO??UM TAR??H??"))
        self.txtAddress.setText(_translate("txtRegisterScreen", "ADRES"))
        self.btnRegisterButton.setText(_translate("txtRegisterScreen", "Kay??t"))

    def clearForm(self):
        self.lnName.setText('')
        self.lnNameP.setText('')
        self.lnPasswordNumber.setText('')
        self.lnAddress.setText('')


    def controlUser(self):
        for element in self.tcNumber:
            if(element not in ['1','2','3','4','5','6','7','8','9','0']):
                return False
        if(self.firstName=='' or self.lastName=='' or self.address=='' or self.birthday=='' or self.password==''):
            return False
        if(len(self.tcNumber)!=11):
            return False
        return True
        
    def registerUser(self):
        userOperations=databaseOperation.UserOperations('database.db')
        self.firstName=self.lnName.text()
        self.lastName=self.lnNameP.text()
        self.tcNumber=self.lnTcNumber.text()
        self.birthday=self.lnDateTime.text()
        self.password=self.lnPasswordNumber.text()
        self.address=self.lnAddress.text()
        self.clearForm()

        if(len(userOperations.getUser(self.tcNumber))!=0):
            print("Kullan??c?? Zaten Var...!")
        elif(self.controlUser() and userOperations.addUser(self.tcNumber,self.firstName,self.lastName,self.birthday,self.password,self.address)):
            print("Kay??t Yap??ld??...")
            self.dialog.close()
            self.questionWindow=QtWidgets.QWidget()
            self.uiQuestionScreen=Ui_FormQuestion(self.tcNumber)
            self.uiQuestionScreen.setupUi(self.questionWindow)
            self.questionWindow.show()
        else:
            print("Yaz??m Hatas?? Var...!")
            
