# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'danmu.ui'
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
        Form.resize(296, 600)
        Form.setMinimumSize(QSize(200, 600))
        Form.setMaximumSize(QSize(320, 16777215))
        Form.setStyleSheet(u"*{\n"
"                background-color:rgb(53,53,53);\n"
"                color:rgb(0, 163, 245);\n"
"                font-size: 15px;\n"
"                font-family:Consolas, \u5fae\u8f6f\u96c5\u9ed1\n"
"}\n"
"\n"
"            ")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.danmuText = QTextBrowser(Form)
        self.danmuText.setObjectName(u"danmuText")

        self.horizontalLayout.addWidget(self.danmuText)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Danmu", None))
    # retranslateUi

