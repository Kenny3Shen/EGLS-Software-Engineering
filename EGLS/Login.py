from threading import Thread
import pymysql
from PySide2.QtCore import QFile, QSettings
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMessageBox
import hashlib
import random
from shared_ptr import SP
from EGLS_Backend.backend import MySQL
import Register


# close  'django.middleware.csrf.CsrfViewMiddleware',

class Login:
    def __init__(self):
        ui_file = QFile('ui/login.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)
        self.username, self.pwd = '', ''
        self.ui.sign_in.clicked.connect(self.sign_in)
        self.ui.Register.clicked.connect(self.showRegister)
        self.ui.username.returnPressed.connect(self.sign_in)
        self.ui.password.returnPressed.connect(self.sign_in)

    @staticmethod
    def showRegister(self):
        SP.registerWindow = Register.Register()
        SP.registerWindow.show()

    def check(self):
        con = pymysql.connect(host="localhost", user="root", password="123456", database="User")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {self.username} WHERE Username = '{self.username}'")
        data = cursor.fetchone()
        if data:
            QMessageBox.critical(self.ui, 'ERROR', 'The current username exist.')

    def sign_in(self):
        # self.username = self.ui.username.text().strip()
        # pwd = self.ui.password.text().strip()
        # json = {
        #     'action': 'signin',
        #     'username': self.username,
        #     'password': pwd
        # }
        # url = 'http://127.0.0.1/api/sign'
        # s = requests.session()
        # res = s.post(url=url, json=json).json()
        # if res['ret'] != 0:
        #     QMessageBox.critical(self.ui, 'ERROR', 'Wrong username or password.')
        # else:
        #     SP.mainWindow.user = self.username
        #     self.ui.password.setText('')
        #     SP.mainWindow.ui.actionSign_in.setText('Sign out')
        #     SP.mainWindow.ui.trueLink.setPlainText(f'Hello, {self.username}!')
        #     thread = Thread(target=self.loadFavorites)
        #     thread.start()
        #     self.ui.close()

        rand = random.getrandbits(128)
        self.username = self.ui.username.text().strip()
        t = self.ui.password.text().strip().encode()
        # md5(md5(password)+random))
        self.pwd = hashlib.md5((str(hashlib.md5(t).hexdigest()) + str(hex(rand))).encode()).hexdigest()
        # print(self.pwd)
        con = MySQL(database='User', sql=f"SELECT Password FROM USERDATA WHERE Username = '{self.username}'")
        con.exe()
        data = con.getData()
        # con = pymysql.connect(host="localhost", user="root", password="123456", database="User")
        # cursor = con.cursor()
        # cursor.execute(f"SELECT * FROM USERDATA WHERE Username = '{self.username}'")
        # data = cursor.fetchone()
        # cursor.close()
        # con.close()

        # print(hashlib.md5((str(data[1]) + str(hex(rand))).encode()).hexdigest())
        if not data:
            QMessageBox.critical(self.ui, 'ERROR', 'Username not exist')
            return
        elif hashlib.md5((str(data[0][0]) + str(hex(rand))).encode()).hexdigest() != self.pwd:
            QMessageBox.critical(self.ui, 'ERROR', 'Wrong username or password.')
            return
        else:
            SP.mainWindow.user = self.username
            if self.ui.keepLogin.isChecked():
                ini = QSettings(".setting.ini", QSettings.IniFormat)
                ini.setIniCodec('uft-8')
                ini.setValue('Account/Username', self.ui.username.text().strip())
                ini.setValue('Account/Password', self.ui.password.text().strip())
            else:
                ini = QSettings(".setting.ini", QSettings.IniFormat)
                ini.setIniCodec('uft-8')
                ini.setValue('Account/Username', "None")
                ini.setValue('Account/Password', '')
            SP.mainWindow.ui.actionSign_in.setText('Sign out')
            SP.mainWindow.ui.trueLink.setPlainText(f'Hello, {self.username}!')
            Thread(target=self.loadFavorites).start()
            self.ui.close()

    def loadFavorites(self):
        # con = pymysql.connect(host="localhost", user="root", password="123456", database="LiveLink")
        con = MySQL(database='User', sql=f"SELECT Title FROM {self.username}")
        con.exe()
        data = con.getData()
        for i in data:
            SP.mainWindow.ui.favorites.addItem(i[0])
        Thread(target=SP.mainWindow.detect).start()

    def sign_up(self):
        self.check()
