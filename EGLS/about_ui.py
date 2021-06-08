# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
        Form.resize(600, 350)
        Form.setMinimumSize(QSize(600, 350))
        Form.setMaximumSize(QSize(600, 350))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(24)
        Form.setFont(font)
        Form.setStyleSheet(u"*{\n"
"                background-color:rgb(53,53,53);\n"
"                color: rgb(255,255,255);\n"
"                font-family:Consolas, \u5fae\u8f6f\u96c5\u9ed1\n"
"}\n"
"			\n"
"            ")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 471, 41))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(28)
        self.label.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 571, 31))
        font2 = QFont()
        font2.setFamily(u"Consolas")
        font2.setPointSize(14)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 551, 21))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 320, 271, 16))
        font3 = QFont()
        font3.setFamily(u"Consolas")
        font3.setPointSize(10)
        self.label_4.setFont(font3)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 200, 511, 21))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        font4.setPointSize(12)
        self.label_5.setFont(font4)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 240, 331, 21))
        self.label_6.setFont(font4)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 160, 531, 21))
        self.label_7.setFont(font4)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(510, 280, 51, 51))
        self.label_8.setFont(font3)
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 280, 421, 21))
        self.label_9.setFont(font4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"About EGLS", None))
        self.label.setText(QCoreApplication.translate("Form", u"Easy Get Live Streaming", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"A software used to extract a live streaming and save it", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>EGLS Open Source Project: <a href=\"https://github.com/Kenny3Shen/EGLS\"><span style=\" font-weight:600; font-style:italic; text-decoration: none; color:#00aaff;\">GitHub</span></a></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Copyright\u00a9 2021 Kenny3Shen(1815200045)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Powered by JetBrains PyCharm 2021.1.2 (Community Editon)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"GUI powered by PySide2 & Qt Designer", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Developing environment: Windows 10 21H1 & Bulit on 8/6/2021", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"This is\n"
"an ICON", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Database and backend powered by MySQL & Django", None))
    # retranslateUi

