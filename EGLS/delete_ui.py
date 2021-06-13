# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
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
        Form.resize(500, 300)
        Form.setMinimumSize(QSize(500, 300))
        Form.setMaximumSize(QSize(500, 300))
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
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pwd = QLineEdit(Form)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.pwd)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.confirm = QLineEdit(Form)
        self.confirm.setObjectName(u"confirm")

        self.verticalLayout.addWidget(self.confirm)

        self.submit = QPushButton(Form)
        self.submit.setObjectName(u"submit")
        self.submit.setEnabled(False)

        self.verticalLayout.addWidget(self.submit)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Are you absolutely sure?", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"This action cannot be undone. This will permanently delete\n"
"your account and remove all your data.\n"
"\n"
"Please input your password first.", None))
        self.label.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Type <b>I want to delete my account</b> to confirm.", None))
        self.submit.setText(QCoreApplication.translate("Form", u"I understand the consequence, delete this account", None))
    # retranslateUi

