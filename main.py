import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import pyrebase

firebaseConfig = {'apiKey': "AIzaSyDUKhnGN9Cl94HL1aAWaMzLH_t0dZqog3c",
                  'authDomain': "pyparser-90d09.firebaseapp.com",
                  'databaseURL': "https://pyparser-90d0.firebaseio.com",
                  'projectId': "pyparser-90d09",
                  'storageBucket': "pyparser-90d09.appspot.com",
                  'messagingSenderId': "522296716745",
                  'appId': "1:522296716745:web:0e8f2c27b4bc66cade0c18",
                  'measurementId': "G-PFCCPQBC00"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("login.ui", self)
        self.linePass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnConfirm.clicked.connect(self.loginfunction)

    def loginfunction(self):
        email = self.lineLogin.text()
        password = self.linePass.text()
        try:
            # auth.sign_in_with_email_and_password(email, password)
            print(1)
            main = Main()
            widget.addWidget(main)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            widget.setFixedWidth(650)
            widget.setFixedHeight(554)
        except:
            print(False)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.btncsvok.clicked.connect(self.csvfile)

    def csvfile(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Login()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(327)
    widget.setFixedHeight(428)
    widget.show()
    app.exec_()
