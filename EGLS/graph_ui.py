# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graph.ui'
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
        Form.resize(650, 500)
        Form.setMinimumSize(QSize(650, 500))
        Form.setMaximumSize(QSize(650, 500))
        Form.setStyleSheet(u"*{\n"
"                background-color:rgb(53,53,53);\n"
"                color: rgb(255,255,255);\n"
"                font-size: 15px;\n"
"                font-family:Consolas, \u5fae\u8f6f\u96c5\u9ed1\n"
"                }\n"
"\n"
"            ")
        self.graphicsView = QGraphicsView(Form)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(-10, 0, 671, 511))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Analyze Your Favoirtes", None))
    # retranslateUi

