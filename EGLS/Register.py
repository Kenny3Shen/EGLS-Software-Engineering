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
        self.username_pattern = r"^[A-za-z0-9_]{5,15}$"
        # Minimum 5 characters and maximum 15 characters, only digital, English letters and _
        self.pwd_pattern = r"^(?=.*?[a-z])(?=.*?[0-9]).{8,15}$"
        # Minimum 8 characters and maximum 15 characters, at least one lower case English letter, one digital

    def submit(self):
        self.ui.usernameTips.clear()
        self.ui.pwdTips.clear()
        self.ui.repwdTips.clear()
        username = self.ui.username.text().strip()
        pwd = self.ui.pwd.text().strip()
        re_pwd = self.ui.repwd.text().strip()
        con = MySQL(database='User', sql=f"SELECT Username FROM Userdata WHERE Username = '{username}'")
        con.exe()
        if not re.findall(self.username_pattern, username):
            self.ui.usernameTips.setText('The length is between 5 and 15,'
                                         'only digital, \nEnglish letters and _')
            return
        if con.getData():
            self.ui.usernameTips.setText('The current username had used.')
            return
        if not re.findall(self.pwd_pattern, pwd):
            self.ui.pwdTips.setText('The length is between 8 and 15,'
                                    ' at least \none lower case English letter and one digital')
            return
        if pwd != re_pwd:
            self.ui.repwdTips.setText('Re-password mismatch.')
            return
        self.newUser(username, pwd.encode())

    def newUser(self, username, password):
        create_newUser = f"INSERT INTO Userdata (Username, Password) VALUES ('{username}', '{hashlib.md5(password).hexdigest()}')"
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
