import hashlib
import random
import re
from threading import Thread
from PySide2.QtCore import QSettings
from shared_ptr import SP
from PySide2.QtWidgets import QWidget, QMessageBox
from resetPwd_ui import Ui_Form
from EGLS_Backend.backend import MySQL


class ResetPwd(QWidget):
    def __init__(self, username):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.username = username
        self.ui.reset.clicked.connect(self.reset)
        self.ui.repwd.returnPressed.connect(self.reset)
        self.pwd_pattern = r"^(?=.*?[a-z])(?=.*?[0-9]).{8,15}$"
        # Minimum 8 characters and maximum 15 characters, at least one lower case English letter, one digital

    def reset(self):
        self.ui.nowPwdTips.setText('')
        self.ui.pwdTips.setText('')
        self.ui.repwdTips.setText('')
        nonce = random.getrandbits(128)
        inputPwd = self.ui.pwd.text().strip().encode()

        currentPwd = hashlib.md5((str(hashlib.md5(inputPwd).hexdigest()) + str(hex(nonce))).encode()).hexdigest()
        newPwd = self.ui.newPwd.text().strip()
        re_pwd = self.ui.repwd.text().strip()
        con = MySQL(database='User', sql=f"SELECT Password FROM Userdata WHERE Username = '{self.username}'")
        con.exe()
        pwd = con.getData()
        # hash(pwd_db + nonce) ?= hash(hash(pwd_in) + nonce)
        if hashlib.md5((str(pwd[0][0]) + str(hex(nonce))).encode()).hexdigest() != currentPwd:
            self.ui.nowPwdTips.setText('Wrong password')
            return
        if not re.findall(self.pwd_pattern, newPwd):
            self.ui.pwdTips.setText('The length is between 8 and 15,'
                                    ' at least \none lower case English letter and one digital')
            return
        if newPwd != re_pwd:
            self.ui.repwdTips.setText('Re-password mismatch.')
            return
        self.resetPwd(self.username, newPwd.encode())

    def resetPwd(self, username, password):
        reset = f"UPDATE Userdata SET Password = '{hashlib.md5(password).hexdigest()}' WHERE Username = '{username}'"
        MySQL(database='User', sql=reset).exe()
        QMessageBox.information(self, 'Notcie', 'Reset your password succeed, please Re-login.')
        SP.mainWindow.user = 'None'
        SP.mainWindow.ui.actionSign_in.setText('Sign in')
        SP.mainWindow.ui.trueLink.setPlainText("")
        SP.mainWindow.ui.progressBar.setValue(0)
        SP.mainWindow.ui.actionReset_Password.setVisible(False)
        Thread(target=SP.mainWindow.clearFavorites).start()
        ini = QSettings(".setting.ini", QSettings.IniFormat)
        ini.setIniCodec('uft-8')
        ini.setValue('Account/Username', "None")
        ini.setValue('Account/Password', '')
        self.close()
