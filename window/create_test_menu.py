# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_test_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(207, 222)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 181, 31))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.line_name_test = QLineEdit(Dialog)
        self.line_name_test.setObjectName(u"line_name_test")
        self.line_name_test.setGeometry(QRect(20, 100, 161, 22))
        self.btn_create_test = QPushButton(Dialog)
        self.btn_create_test.setObjectName(u"btn_create_test")
        self.btn_create_test.setGeometry(QRect(20, 150, 151, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u0441\u0442\u0430", None))
        self.btn_create_test.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
    # retranslateUi

