# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resetPwd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 400)
        Form.setMinimumSize(QSize(500, 400))
        Form.setMaximumSize(QSize(500, 400))
        Form.setStyleSheet(u"*{\n"
"                background-color:rgb(255,255,255);\n"
"                color: rgb(0,0,0);\n"
"                font-size: 15px;\n"
"                font-family:Consolas, \u5fae\u8f6f\u96c5\u9ed1\n"
"                }\n"
"                #roomID{\n"
"                border:1px solid rgb(170, 170, 170);\n"
"                }\n"
"                QMenu{\n"
"                border:.5px solid rgb(150, 150, 150);\n"
"                }\n"
"                #trueLink{\n"
"                font-size: 17px;\n"
"				border:1px solid rgb(0,0, 0);\n"
"                }\n"
"                #favorites{\n"
"                font-size: 17px;\n"
"                }\n"
"                QMenu::item:selected{\n"
"                background-color:rgb(38, 117, 191);\n"
"                }\n"
"                QComboBox::item:selected{\n"
"                background-color:rgb(38, 117, 191);\n"
"                }\n"
"                QListWidget::item:selected{\n"
"                background-color:rgb(38, 117, 191);\n"
"                "
                        "}\n"
"                QPushButton:hover{\n"
"                border:1px solid rgb(0,0, 0);\n"
"                }\n"
"                #trueLink{\n"
"                border:1px solid rgb(0,0, 0);\n"
"                }\n"
"                QListWidget{\n"
"                border:1px solid rgb(0,0, 0);\n"
"                }\n"
"                #menubar{\n"
"                border-bottom:.5px solid rgb(242, 242, 242);\n"
"				\n"
"	background-color:rgb(242, 242, 242);\n"
"                }\n"
"            ")
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Consolas")
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size:30px")

        self.verticalLayout_2.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.pwd = QLineEdit(Form)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.pwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.pwd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.nowPwdTips = QLabel(Form)
        self.nowPwdTips.setObjectName(u"nowPwdTips")
        self.nowPwdTips.setStyleSheet(u"color:red;\n"
"	font-size:16px")

        self.verticalLayout.addWidget(self.nowPwdTips)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.newPwd = QLineEdit(Form)
        self.newPwd.setObjectName(u"newPwd")
        self.newPwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.newPwd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pwdTips = QLabel(Form)
        self.pwdTips.setObjectName(u"pwdTips")
        self.pwdTips.setStyleSheet(u"color:red;\n"
"font-size:16px")

        self.verticalLayout.addWidget(self.pwdTips)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.repwd = QLineEdit(Form)
        self.repwd.setObjectName(u"repwd")
        self.repwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.repwd)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.repwdTips = QLabel(Form)
        self.repwdTips.setObjectName(u"repwdTips")
        self.repwdTips.setStyleSheet(u"color:red;\n"
"	font-size:16px")

        self.verticalLayout.addWidget(self.repwdTips)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.reset = QPushButton(Form)
        self.reset.setObjectName(u"reset")
        self.reset.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.reset)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"        Reset Password", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Your Password:", None))
        self.nowPwdTips.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"New Password :", None))
        self.pwdTips.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u" Re-password :", None))
        self.repwdTips.setText("")
        self.reset.setText(QCoreApplication.translate("Form", u"Reset", None))
    # retranslateUi

