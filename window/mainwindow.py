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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLCDNumber,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1061, 808)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblicon = QLabel(self.centralwidget)
        self.lblicon.setObjectName(u"lblicon")
        self.lblicon.setGeometry(QRect(10, 10, 281, 61))
        font = QFont()
        font.setPointSize(22)
        self.lblicon.setFont(font)
        self.btnstart_test = QPushButton(self.centralwidget)
        self.btnstart_test.setObjectName(u"btnstart_test")
        self.btnstart_test.setGeometry(QRect(460, 150, 221, 51))
        font1 = QFont()
        font1.setPointSize(24)
        self.btnstart_test.setFont(font1)
        self.lblicon_2 = QLabel(self.centralwidget)
        self.lblicon_2.setObjectName(u"lblicon_2")
        self.lblicon_2.setGeometry(QRect(590, 20, 251, 31))
        self.lblicon_2.setFont(font)
        self.lcdNumber_timer = QLCDNumber(self.centralwidget)
        self.lcdNumber_timer.setObjectName(u"lcdNumber_timer")
        self.lcdNumber_timer.setGeometry(QRect(870, 10, 181, 41))
        self.list_quest_test = QListWidget(self.centralwidget)
        self.list_quest_test.setObjectName(u"list_quest_test")
        self.list_quest_test.setGeometry(QRect(460, 210, 591, 221))
        self.checkBox_answer_a = QCheckBox(self.centralwidget)
        self.checkBox_answer_a.setObjectName(u"checkBox_answer_a")
        self.checkBox_answer_a.setGeometry(QRect(520, 610, 79, 20))
        self.checkBox_answer_b = QCheckBox(self.centralwidget)
        self.checkBox_answer_b.setObjectName(u"checkBox_answer_b")
        self.checkBox_answer_b.setGeometry(QRect(640, 610, 79, 20))
        self.checkBox_answer_c = QCheckBox(self.centralwidget)
        self.checkBox_answer_c.setObjectName(u"checkBox_answer_c")
        self.checkBox_answer_c.setGeometry(QRect(790, 610, 79, 20))
        self.checkBox_answer_d = QCheckBox(self.centralwidget)
        self.checkBox_answer_d.setObjectName(u"checkBox_answer_d")
        self.checkBox_answer_d.setGeometry(QRect(940, 600, 79, 20))
        self.btnendtest = QPushButton(self.centralwidget)
        self.btnendtest.setObjectName(u"btnendtest")
        self.btnendtest.setGeometry(QRect(690, 150, 221, 51))
        self.btnendtest.setFont(font1)
        self.list_answer_d = QListWidget(self.centralwidget)
        self.list_answer_d.setObjectName(u"list_answer_d")
        self.list_answer_d.setGeometry(QRect(910, 450, 141, 121))
        self.list_answer_c = QListWidget(self.centralwidget)
        self.list_answer_c.setObjectName(u"list_answer_c")
        self.list_answer_c.setGeometry(QRect(760, 450, 141, 121))
        self.list_answer_a = QListWidget(self.centralwidget)
        self.list_answer_a.setObjectName(u"list_answer_a")
        self.list_answer_a.setGeometry(QRect(460, 450, 141, 121))
        self.btn_accept_answer = QPushButton(self.centralwidget)
        self.btn_accept_answer.setObjectName(u"btn_accept_answer")
        self.btn_accept_answer.setGeometry(QRect(620, 650, 271, 51))
        self.btn_go_menu = QPushButton(self.centralwidget)
        self.btn_go_menu.setObjectName(u"btn_go_menu")
        self.btn_go_menu.setGeometry(QRect(10, 70, 121, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 70, 211, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(460, 100, 451, 22))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 200, 401, 590))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_quest_1 = QPushButton(self.layoutWidget)
        self.btn_quest_1.setObjectName(u"btn_quest_1")
        self.btn_quest_1.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_1, 0, 0, 1, 1)

        self.btn_quest_2 = QPushButton(self.layoutWidget)
        self.btn_quest_2.setObjectName(u"btn_quest_2")
        self.btn_quest_2.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_2, 0, 1, 1, 1)

        self.btn_quest_3 = QPushButton(self.layoutWidget)
        self.btn_quest_3.setObjectName(u"btn_quest_3")
        self.btn_quest_3.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_3, 0, 2, 1, 1)

        self.btn_quest_4 = QPushButton(self.layoutWidget)
        self.btn_quest_4.setObjectName(u"btn_quest_4")
        self.btn_quest_4.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_4, 0, 3, 1, 1)

        self.btn_quest_5 = QPushButton(self.layoutWidget)
        self.btn_quest_5.setObjectName(u"btn_quest_5")
        self.btn_quest_5.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_5, 1, 0, 1, 1)

        self.btn_quest_6 = QPushButton(self.layoutWidget)
        self.btn_quest_6.setObjectName(u"btn_quest_6")
        self.btn_quest_6.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_6, 1, 1, 1, 1)

        self.btn_quest_7 = QPushButton(self.layoutWidget)
        self.btn_quest_7.setObjectName(u"btn_quest_7")
        self.btn_quest_7.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_7, 1, 2, 1, 1)

        self.btn_quest_8 = QPushButton(self.layoutWidget)
        self.btn_quest_8.setObjectName(u"btn_quest_8")
        self.btn_quest_8.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_8, 1, 3, 1, 1)

        self.btn_quest_9 = QPushButton(self.layoutWidget)
        self.btn_quest_9.setObjectName(u"btn_quest_9")
        self.btn_quest_9.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_9, 2, 0, 1, 1)

        self.btn_quest_10 = QPushButton(self.layoutWidget)
        self.btn_quest_10.setObjectName(u"btn_quest_10")
        self.btn_quest_10.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_10, 2, 1, 1, 1)

        self.btn_quest_11 = QPushButton(self.layoutWidget)
        self.btn_quest_11.setObjectName(u"btn_quest_11")
        self.btn_quest_11.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_11, 2, 2, 1, 1)

        self.btn_quest_12 = QPushButton(self.layoutWidget)
        self.btn_quest_12.setObjectName(u"btn_quest_12")
        self.btn_quest_12.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_12, 2, 3, 1, 1)

        self.btn_quest_13 = QPushButton(self.layoutWidget)
        self.btn_quest_13.setObjectName(u"btn_quest_13")
        self.btn_quest_13.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_13, 3, 0, 1, 1)

        self.btn_quest_14 = QPushButton(self.layoutWidget)
        self.btn_quest_14.setObjectName(u"btn_quest_14")
        self.btn_quest_14.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_14, 3, 1, 1, 1)

        self.btn_quest_15 = QPushButton(self.layoutWidget)
        self.btn_quest_15.setObjectName(u"btn_quest_15")
        self.btn_quest_15.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_15, 3, 2, 1, 1)

        self.btn_quest_16 = QPushButton(self.layoutWidget)
        self.btn_quest_16.setObjectName(u"btn_quest_16")
        self.btn_quest_16.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_16, 3, 3, 1, 1)

        self.btn_quest_17 = QPushButton(self.layoutWidget)
        self.btn_quest_17.setObjectName(u"btn_quest_17")
        self.btn_quest_17.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_17, 4, 0, 1, 1)

        self.btn_quest_18 = QPushButton(self.layoutWidget)
        self.btn_quest_18.setObjectName(u"btn_quest_18")
        self.btn_quest_18.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_18, 4, 1, 1, 1)

        self.btn_quest_19 = QPushButton(self.layoutWidget)
        self.btn_quest_19.setObjectName(u"btn_quest_19")
        self.btn_quest_19.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_19, 4, 2, 1, 1)

        self.btn_quest_20 = QPushButton(self.layoutWidget)
        self.btn_quest_20.setObjectName(u"btn_quest_20")
        self.btn_quest_20.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_20, 4, 3, 1, 1)

        self.btn_quest_21 = QPushButton(self.layoutWidget)
        self.btn_quest_21.setObjectName(u"btn_quest_21")
        self.btn_quest_21.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_21, 5, 0, 1, 1)

        self.btn_quest_22 = QPushButton(self.layoutWidget)
        self.btn_quest_22.setObjectName(u"btn_quest_22")
        self.btn_quest_22.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_22, 5, 1, 1, 1)

        self.btn_quest_23 = QPushButton(self.layoutWidget)
        self.btn_quest_23.setObjectName(u"btn_quest_23")
        self.btn_quest_23.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_23, 5, 2, 1, 1)

        self.btn_quest_24 = QPushButton(self.layoutWidget)
        self.btn_quest_24.setObjectName(u"btn_quest_24")
        self.btn_quest_24.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_24, 5, 3, 1, 1)

        self.btn_quest_25 = QPushButton(self.layoutWidget)
        self.btn_quest_25.setObjectName(u"btn_quest_25")
        self.btn_quest_25.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_25, 6, 0, 1, 1)

        self.btn_quest_26 = QPushButton(self.layoutWidget)
        self.btn_quest_26.setObjectName(u"btn_quest_26")
        self.btn_quest_26.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_26, 6, 1, 1, 1)

        self.btn_quest_27 = QPushButton(self.layoutWidget)
        self.btn_quest_27.setObjectName(u"btn_quest_27")
        self.btn_quest_27.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_27, 6, 2, 1, 1)

        self.btn_quest_28 = QPushButton(self.layoutWidget)
        self.btn_quest_28.setObjectName(u"btn_quest_28")
        self.btn_quest_28.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_28, 6, 3, 1, 1)

        self.btn_quest_29 = QPushButton(self.layoutWidget)
        self.btn_quest_29.setObjectName(u"btn_quest_29")
        self.btn_quest_29.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_29, 7, 0, 1, 1)

        self.btn_quest_30 = QPushButton(self.layoutWidget)
        self.btn_quest_30.setObjectName(u"btn_quest_30")
        self.btn_quest_30.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_30, 7, 1, 1, 1)

        self.btn_quest_31 = QPushButton(self.layoutWidget)
        self.btn_quest_31.setObjectName(u"btn_quest_31")
        self.btn_quest_31.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_31, 7, 2, 1, 1)

        self.btn_quest_32 = QPushButton(self.layoutWidget)
        self.btn_quest_32.setObjectName(u"btn_quest_32")
        self.btn_quest_32.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_32, 7, 3, 1, 1)

        self.btn_quest_33 = QPushButton(self.layoutWidget)
        self.btn_quest_33.setObjectName(u"btn_quest_33")
        self.btn_quest_33.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_33, 8, 0, 1, 1)

        self.btn_quest_34 = QPushButton(self.layoutWidget)
        self.btn_quest_34.setObjectName(u"btn_quest_34")
        self.btn_quest_34.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_34, 8, 1, 1, 1)

        self.btn_quest_35 = QPushButton(self.layoutWidget)
        self.btn_quest_35.setObjectName(u"btn_quest_35")
        self.btn_quest_35.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_35, 8, 2, 1, 1)

        self.btn_quest_36 = QPushButton(self.layoutWidget)
        self.btn_quest_36.setObjectName(u"btn_quest_36")
        self.btn_quest_36.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_36, 8, 3, 1, 1)

        self.btn_quest_37 = QPushButton(self.layoutWidget)
        self.btn_quest_37.setObjectName(u"btn_quest_37")
        self.btn_quest_37.setMinimumSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_quest_37, 8, 4, 1, 1)

        self.list_answer_b = QListWidget(self.centralwidget)
        self.list_answer_b.setObjectName(u"list_answer_b")
        self.list_answer_b.setGeometry(QRect(610, 450, 141, 121))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblicon.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u0430\u0443\u0434\u0438\u0438\u0442\u043f\u043b\u044e\u0441", None))
        self.btnstart_test.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.lblicon_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0432\u0448\u0435\u0435\u0441\u044f \u0432\u0440\u0435\u043c\u044f", None))
        self.checkBox_answer_a.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_answer_b.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_answer_c.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_answer_d.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.btnendtest.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043e\u043d\u0447\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.btn_accept_answer.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043e\u0442\u0432\u0435\u0442\u044b", None))
        self.btn_go_menu.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0436\u0435\u044e\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0442\u0435\u0441\u0442\u0430 \u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0412\u0430\u0448\u0435 \u0424\u0418\u041e", None))
        self.btn_quest_1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 1", None))
        self.btn_quest_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 2", None))
        self.btn_quest_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 3", None))
        self.btn_quest_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 4", None))
        self.btn_quest_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 5", None))
        self.btn_quest_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 6", None))
        self.btn_quest_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 7", None))
        self.btn_quest_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 8", None))
        self.btn_quest_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 9", None))
        self.btn_quest_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 10", None))
        self.btn_quest_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 11", None))
        self.btn_quest_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 12", None))
        self.btn_quest_13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 13", None))
        self.btn_quest_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 14", None))
        self.btn_quest_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 15", None))
        self.btn_quest_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 16", None))
        self.btn_quest_17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 17", None))
        self.btn_quest_18.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 18", None))
        self.btn_quest_19.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 19", None))
        self.btn_quest_20.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 20", None))
        self.btn_quest_21.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 21", None))
        self.btn_quest_22.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 22", None))
        self.btn_quest_23.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 23", None))
        self.btn_quest_24.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 24", None))
        self.btn_quest_25.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 25", None))
        self.btn_quest_26.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 26", None))
        self.btn_quest_27.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 27", None))
        self.btn_quest_28.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 28", None))
        self.btn_quest_29.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 29", None))
        self.btn_quest_30.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 30", None))
        self.btn_quest_31.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 31", None))
        self.btn_quest_32.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 32", None))
        self.btn_quest_33.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 33", None))
        self.btn_quest_34.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 34", None))
        self.btn_quest_35.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 35", None))
        self.btn_quest_36.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 36", None))
        self.btn_quest_37.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043f\u0440\u043e\u0441 37", None))
    # retranslateUi

