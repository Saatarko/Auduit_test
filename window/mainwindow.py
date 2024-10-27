# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(617, 194)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnstart_test = QPushButton(self.centralwidget)
        self.btnstart_test.setObjectName(u"btnstart_test")
        self.btnstart_test.setGeometry(QRect(10, 130, 221, 51))
        font = QFont()
        font.setPointSize(24)
        self.btnstart_test.setFont(font)
        self.btn_go_menu = QPushButton(self.centralwidget)
        self.btn_go_menu.setObjectName(u"btn_go_menu")
        self.btn_go_menu.setGeometry(QRect(480, 20, 121, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 291, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.linefio_edit = QLineEdit(self.centralwidget)
        self.linefio_edit.setObjectName(u"linefio_edit")
        self.linefio_edit.setGeometry(QRect(10, 100, 451, 22))
        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(0, 0, 191, 71))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnstart_test.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.btn_go_menu.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0436\u0435\u0431\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0442\u0435\u0441\u0442\u0430 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448\u0435 \u0424\u0418\u041e", None))
        self.label_logo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

