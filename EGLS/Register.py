import hashlib
import re
from PySide2.QtWidgets import QWidget, QMessageBox
from register_ui import Ui_Form
from EGLS_Backend.backend import MySQL


class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.submit.clicked.connect(self.submit)
        self.ui.repwd.returnPressed.connect(self.submit)
        self.ui.username.textChanged.connect(self.setUsernameTips)
        self.ui.pwd.textChanged.connect(self.setPasswordTips)
        self.ui.repwd.textChanged.connect(self.setRePasswordTips)
        self.flag1, self.flag2, self.flag3 = False, False, False
        self.username, self.pwd = '', ''
        self.username_pattern = r"^[A-za-z0-9_]{6,12}$"
        # Minimum 6 characters and maximum 12 characters, only digital, English letters and _
        self.pwd_pattern = r"^(?=.*?[a-z])(?=.*?[0-9]).{8,15}$"
        # Minimum 8 characters and maximum 15 characters, at least one lower case English letter, one digital

    def setUsernameTips(self):
        self.username = self.ui.username.text().strip()
        if not re.findall(self.username_pattern, self.username):
            self.ui.usernameTips.setText('The length is between 5 and 15,'
                                         'only digital, \nEnglish letters and _')
            self.flag1 = False
        else:
            con = MySQL(database='User', sql=f"SELECT Username FROM Userdata WHERE Username = '{self.username}'")
            con.exe()
            if con.getData():
                self.ui.usernameTips.setText('The current username had used.')
                self.flag1 = False
            else:
                self.ui.usernameTips.setText('<font color="green">Available</font>')
                self.flag1 = True

    def setPasswordTips(self):
        self.pwd = self.ui.pwd.text().strip()
        if not re.findall(self.pwd_pattern, self.pwd):
            self.ui.pwdTips.setText('The length is between 8 and 15,'
                                    ' at least \none lower case English letter and one digital')
            self.flag2 = False
        else:
            self.ui.pwdTips.setText('<font color="green">Available</font>')
            self.flag2 = True

    def setRePasswordTips(self):
        if self.ui.pwd.text().strip() != self.ui.repwd.text().strip():
            self.ui.repwdTips.setText('Re-password mismatch.')
            self.flag3 = False
        else:
            self.ui.repwdTips.setText('<font color="green">Available</font>')
            self.flag3 = True

    def submit(self):
        # self.ui.usernameTips.clear()
        # self.ui.pwdTips.clear()
        # self.ui.repwdTips.clear()
        # username = self.ui.username.text().strip()
        # pwd = self.ui.pwd.text().strip()
        # re_pwd = self.ui.repwd.text().strip()
        # con = MySQL(database='User', sql=f"SELECT Username FROM Userdata WHERE Username = '{username}'")
        # con.exe()
        # if not re.findall(self.username_pattern, username):
        #     self.ui.usernameTips.setText('The length is between 5 and 15,'
        #                                  'only digital, \nEnglish letters and _')
        #     return
        # if con.getData():
        #     self.ui.usernameTips.setText('The current username had used.')
        #     return
        # if not re.findall(self.pwd_pattern, pwd):
        #     self.ui.pwdTips.setText('The length is between 8 and 15,'
        #                             ' at least \none lower case English letter and one digital')
        #     return
        # if pwd != re_pwd:
        #     self.ui.repwdTips.setText('Re-password mismatch.')
        #     return
        if self.flag1 and self.flag2 and self.flag3:
            self.newUser(self.username, self.pwd.encode())
        else:
            QMessageBox.critical(self, 'ERROR', 'Please enter the correct information according to the tips')

    def newUser(self, username, password):
        create_newUser = f"INSERT INTO Userdata (Username, Password) " \
                         f"VALUES ('{username}', '{hashlib.md5(password).hexdigest()}')"
        MySQL(database='User', sql=create_newUser).exe()
        newUserTable = f'''CREATE TABLE {username} (
              Title      varchar(32) NOT NULL,
              Platform   tinyint NOT NULL,
              RoomId     varchar(32) NOT NULL,
              Definition tinyint NOT NULL,
              id         int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
        '''
        MySQL(database='user', sql=newUserTable).exe()
        QMessageBox.information(self, 'Succeed', f'User "{username}" created successfully')
        self.close()
