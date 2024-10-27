# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(284, 255)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 49, 16))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.btn_list_test = QPushButton(Dialog)
        self.btn_list_test.setObjectName(u"btn_list_test")
        self.btn_list_test.setGeometry(QRect(80, 100, 121, 31))
        self.btn_list_test.setFont(font)
        self.btn_addtest = QPushButton(Dialog)
        self.btn_addtest.setObjectName(u"btn_addtest")
        self.btn_addtest.setGeometry(QRect(80, 50, 121, 31))
        self.btn_addtest.setFont(font)
        self.btn_list_applicant = QPushButton(Dialog)
        self.btn_list_applicant.setObjectName(u"btn_list_applicant")
        self.btn_list_applicant.setGeometry(QRect(50, 150, 191, 31))
        self.btn_list_applicant.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041c\u0435\u043d\u044e", None))
        self.btn_list_test.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0435\u0441\u0442\u043e\u0432", None))
        self.btn_addtest.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.btn_list_applicant.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0438\u0441\u043a\u0430\u0442\u0435\u043b\u0435\u0439", None))
    # retranslateUi

