# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_applicant.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 0, 151, 41))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.btn_exit_to_menu = QPushButton(Dialog)
        self.btn_exit_to_menu.setObjectName(u"btn_exit_to_menu")
        self.btn_exit_to_menu.setGeometry(QRect(110, 250, 181, 24))
        self.list_applicant = QListWidget(Dialog)
        self.list_applicant.setObjectName(u"list_applicant")
        self.list_applicant.setGeometry(QRect(30, 40, 341, 192))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0438\u0441\u043a\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.btn_exit_to_menu.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

