from PyQt5.QtWidgets import QLabel,QApplication,QLineEdit,QPushButton,QWidget,QMainWindow,QMessageBox
from getGenetate import generation
from emailServer import EmailService
from index import Repository
from datetime import datetime
class ConfirmationWindow(QWidget):
    def __init__(self,email,token):
        super().__init__()
        self.token = token
        self.email = email
        self.setWindowTitle("Confirmation")
        self.setFixedSize(400,400)
        self.btnLogin = QPushButton("Submit",self)
        self.LblWelcome = QLabel("Confirmation!",self)
        self.LblWelcome.move(20,20)
        self.btnLogin.setGeometry(120,150,150,30)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(20,50)
        self.lineEdit.setPlaceholderText("Code..")

        self.btnLogin.clicked.connect(self.sendOtp)

    def sendOtp(self):
        repObj = Repository().otpRepository().getByTokenEmail(token=self.token,email=self.email)
        if repObj.expireAt < datetime.now():
            self.MessageBox("Code eskirgan")

        elif repObj.pasw == self.lineEdit.text():
            self.MessageBox("Register bo'ldingiiz!")
        else:
            self.MessageBox("Code hato")




    def MessageBox(self,message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec()




# app = QApplication([])
# window = ConfirmationWindow()
# window.show()
# app.exec()