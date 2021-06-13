import hashlib
import random
from threading import Thread

from PySide2.QtCore import QSettings
from PySide2.QtWidgets import QWidget, QMessageBox

from shared_ptr import SP
from delete_ui import Ui_Form
from EGLS_Backend.backend import MySQL


class DelAcc(QWidget):
    def __init__(self, username):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.username = username
        self.ui.submit.clicked.connect(self.submit)
        self.ui.confirm.textChanged.connect(self.confirm)
        self.flag1, self.flag2, self.flag3 = False, False, False
        self.pwd = ''
        self.confirmString = f"Delete {self.username}"
        self.ui.label_2.setText(f"Type <b>{self.confirmString}</b> to confirm.")
        # self.flag = False

    def confirm(self):
        if self.ui.confirm.text() == self.confirmString:
            self.ui.submit.setEnabled(True)
        else:
            self.ui.submit.setEnabled(False)

    def submit(self):
        nonce = random.getrandbits(128)
        inputPwd = self.ui.pwd.text().strip().encode()
        currentPwd = hashlib.md5((str(hashlib.md5(inputPwd).hexdigest()) + str(hex(nonce))).encode()).hexdigest()
        con = MySQL(database='User', sql=f"SELECT Password FROM Userdata WHERE Username = '{self.username}'")
        con.exe()
        pwd = con.getData()
        # hash(pwd_db + nonce) ?= hash(hash(pwd_in) + nonce)
        if hashlib.md5((str(pwd[0][0]) + str(hex(nonce))).encode()).hexdigest() != currentPwd:
            QMessageBox.critical(self, 'Error', 'Wrong password')
        else:
            self.delAccount()

    def delAccount(self):
        del1 = f"DELETE FROM userdata WHERE Username = '{self.username}'"
        del2 = f"DROP TABLE {self.username}"
        MySQL(database='User', sql=del2).exe()
        MySQL(database='User', sql=del1).exe()
        QMessageBox.information(self, 'Notcie', 'Your account have been delete.')
        SP.mainWindow.user = 'None'
        SP.mainWindow.ui.actionSign_in.setText('Sign in')
        SP.mainWindow.ui.trueLink.setPlainText("")
        SP.mainWindow.ui.progressBar.setValue(0)
        SP.mainWindow.ui.actionReset_Password.setVisible(False)
        SP.mainWindow.ui.actionExport_Favorites.setVisible(False)
        SP.mainWindow.ui.actionAnalyze_Favorites.setVisible(False)
        SP.mainWindow.ui.actionImport_Favorites.setVisible(False)
        SP.mainWindow.ui.actionDelete_Account.setVisible(False)
        Thread(target=SP.mainWindow.clearFavorites).start()
        ini = QSettings(".setting.ini", QSettings.IniFormat)
        ini.setIniCodec('uft-8')
        ini.setValue('Account/Username', "None")
        ini.setValue('Account/Password', '')
        self.close()
