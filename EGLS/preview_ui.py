# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preview.ui'
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
        Form.resize(320, 180)
        Form.setMinimumSize(QSize(320, 180))
        Form.setMaximumSize(QSize(320, 180))
        Form.setStyleSheet(u"*{\n"
"                background-color:rgb(53,53,53);\n"
"                color: rgb(255,255,255);\n"
"                font-size: 15px;\n"
"                font-family:Consolas, \u5fae\u8f6f\u96c5\u9ed1\n"
"                }\n"
"            ")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Camera1 = QLabel(Form)
        self.Camera1.setObjectName(u"Camera1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Camera1.sizePolicy().hasHeightForWidth())
        self.Camera1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Camera1, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Preview", None))
        self.Camera1.setText("")
    # retranslateUi

