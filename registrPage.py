from PyQt5.QtWidgets import QLabel,QApplication,QLineEdit,QPushButton,QWidget,QMainWindow,QMessageBox
from getGenetate import generation
from emailServer import EmailService
from confirmationPage import ConfirmationWindow
from index import Repository
import datetime

class OtpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registraction")
        self.setFixedSize(400,400)
        self.btnLogin = QPushButton("Login",self)
        self.LblWelcome = QLabel("Welcome to Login!",self)
        self.LblWelcome.move(20,20)
        self.btnLogin.setGeometry(120,150,150,30)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(20,50)

        self.btnLogin.clicked.connect(self.sendOtp)

    def sendOtp(self):
        otpPas = generation(6)
        emailS = EmailService(
            sender_email="shaxriyorziyodullayev816@gmail.com",
            receiver_email=self.lineEdit.text(),
            sender_password="itag klxi wegj bfcv",
            subject="Registratsiya",
            message=f"Your code {otpPas}"
        )
        otpRepo = Repository().otpRepository().create(
            email=self.lineEdit.text(),
            pasw=otpPas,
            expireAt=datetime.datetime.now() + datetime.timedelta(seconds=60)
        )


        if emailS.sendSucces:
            self.confWin = ConfirmationWindow(email=self.lineEdit.text(),token=otpRepo)
            self.confWin.show() 
            self.close()
        else:
            self.MessageBox("kod yuborishda xatolik")


    def MessageBox(self,message):
        msg = QMessageBox()
        msg.setText(message)
        msg.exec()

app = QApplication([])
window = OtpWindow()
window.show()
app.exec()