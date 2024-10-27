# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1088, 727)
        self.list_answer_c = QListWidget(Dialog)
        self.list_answer_c.setObjectName(u"list_answer_c")
        self.list_answer_c.setGeometry(QRect(440, 500, 281, 121))
        self.list_answer_c.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_answer_c.setWordWrap(True)
        self.list_answer_a = QListWidget(Dialog)
        self.list_answer_a.setObjectName(u"list_answer_a")
        self.list_answer_a.setGeometry(QRect(440, 290, 281, 121))
        self.list_answer_a.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_answer_a.setWordWrap(True)
        self.checkBox_answer_d = QCheckBox(Dialog)
        self.checkBox_answer_d.setObjectName(u"checkBox_answer_d")
        self.checkBox_answer_d.setGeometry(QRect(860, 640, 79, 20))
        self.list_quest_test = QListWidget(Dialog)
        self.list_quest_test.setObjectName(u"list_quest_test")
        self.list_quest_test.setGeometry(QRect(440, 90, 591, 161))
        self.list_quest_test.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_quest_test.setWordWrap(True)
        self.list_answer_d = QListWidget(Dialog)
        self.list_answer_d.setObjectName(u"list_answer_d")
        self.list_answer_d.setGeometry(QRect(750, 500, 281, 121))
        self.list_answer_d.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_answer_d.setWordWrap(True)
        self.checkBox_answer_c = QCheckBox(Dialog)
        self.checkBox_answer_c.setObjectName(u"checkBox_answer_c")
        self.checkBox_answer_c.setGeometry(QRect(540, 630, 79, 20))
        self.checkBox_answer_b = QCheckBox(Dialog)
        self.checkBox_answer_b.setObjectName(u"checkBox_answer_b")
        self.checkBox_answer_b.setGeometry(QRect(840, 430, 79, 20))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 401, 590))
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

        self.checkBox_answer_a = QCheckBox(Dialog)
        self.checkBox_answer_a.setObjectName(u"checkBox_answer_a")
        self.checkBox_answer_a.setGeometry(QRect(550, 420, 79, 20))
        self.list_answer_b = QListWidget(Dialog)
        self.list_answer_b.setObjectName(u"list_answer_b")
        self.list_answer_b.setGeometry(QRect(750, 290, 281, 121))
        self.list_answer_b.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_answer_b.setWordWrap(True)
        self.btn_accept_answer = QPushButton(Dialog)
        self.btn_accept_answer.setObjectName(u"btn_accept_answer")
        self.btn_accept_answer.setGeometry(QRect(590, 670, 271, 51))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 50, 181, 16))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(550, 270, 49, 16))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(860, 270, 49, 16))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(550, 470, 49, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(860, 470, 49, 16))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 620, 381, 101))
        self.line_test = QLineEdit(Dialog)
        self.line_test.setObjectName(u"line_test")
        self.line_test.setGeometry(QRect(1020, 20, 61, 22))
        self.line_fio = QLineEdit(Dialog)
        self.line_fio.setObjectName(u"line_fio")
        self.line_fio.setGeometry(QRect(1020, 50, 61, 22))
        self.btn_end_test = QPushButton(Dialog)
        self.btn_end_test.setObjectName(u"btn_end_test")
        self.btn_end_test.setGeometry(QRect(630, 10, 271, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_answer_d.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_answer_c.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_answer_b.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.btn_quest_1.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 1", None))
        self.btn_quest_2.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 2", None))
        self.btn_quest_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 3", None))
        self.btn_quest_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 4", None))
        self.btn_quest_5.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 5", None))
        self.btn_quest_6.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 6", None))
        self.btn_quest_7.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 7", None))
        self.btn_quest_8.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 8", None))
        self.btn_quest_9.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 9", None))
        self.btn_quest_10.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 10", None))
        self.btn_quest_11.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 11", None))
        self.btn_quest_12.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 12", None))
        self.btn_quest_13.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 13", None))
        self.btn_quest_14.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 14", None))
        self.btn_quest_15.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 15", None))
        self.btn_quest_16.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 16", None))
        self.btn_quest_17.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 17", None))
        self.btn_quest_18.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 18", None))
        self.btn_quest_19.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 19", None))
        self.btn_quest_20.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 20", None))
        self.btn_quest_21.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 21", None))
        self.btn_quest_22.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 22", None))
        self.btn_quest_23.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 23", None))
        self.btn_quest_24.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 24", None))
        self.btn_quest_25.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 25", None))
        self.btn_quest_26.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 26", None))
        self.btn_quest_27.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 27", None))
        self.btn_quest_28.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 28", None))
        self.btn_quest_29.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 29", None))
        self.btn_quest_30.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 30", None))
        self.btn_quest_31.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 31", None))
        self.btn_quest_32.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 32", None))
        self.btn_quest_33.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 33", None))
        self.btn_quest_34.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 34", None))
        self.btn_quest_35.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 35", None))
        self.btn_quest_36.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 36", None))
        self.btn_quest_37.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u043f\u0440\u043e\u0441 37", None))
        self.checkBox_answer_a.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.btn_accept_answer.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0435 \u043e\u0442\u0432\u0435\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0441\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 \u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 \u0431", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 c", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 d", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"<html>\n"
"<head/>\n"
"<body>\n"
"    <p align=\"justify\" style=\"line-height: 1.0;\">\n"
"        \u0412\u043e\u043f\u0440\u043e\u0441 \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0439 \u0412\u044b \u043e\u0442\u0432\u0435\u0447\u0430\u0435\u0442\u0435 \u0432\u044b\u0434\u0435\u043b\u044f\u0435\u0442\u0441\u044f \u043a\u0440\u0430\u0441\u043d\u043e\u0439 \u0440\u0430\u043c\u043a\u043e\u0439.\n"
"    </p>\n"
"    <p align=\"justify\" style=\"line-height: 1.0;\">\n"
"        \u0412\u043e\u043f\u0440\u043e\u0441 \u043d\u0430 \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0412\u044b \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u043b\u0438 \u043e\u0442\u0432\u0435\u0442\u044b \u0432\u044b\u0434\u0435\u043b\u044f\u044e\u0442\u0441\u044f\n"
"    </p>\n"
"    <p align=\"justify\" style=\"line-height: 1.0;\">\n"
"        \u0437\u0435\u043b\u0435\u043d\u044b\u043c \u0446\u0432\u0435\u0442\u043e\u043c. \u0415\u0441\u043b\u0438 \u0432\u044b \u043f\u0435\u0440\u0435\u0439\u0434\u0435\u0442\u0435 \u043d\u0430"
                        " \u0434\u0440\u0443\u0433\u043e\u0439 \u0432\u043e\u043f\u0440\u043e\u0441 \u043d\u0435\n"
"    </p>\n"
"    <p align=\"justify\" style=\"line-height: 1.0;\">\n"
"        \u043d\u0430\u0436\u0430\u0432 \u043a\u043d\u043e\u043f\u043a\u0443 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0412\u0430\u0448\u0438 \u0432\u044b\u0431\u043e\u0440\u044b \u043d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u0441\u044f.\n"
"    </p>\n"
"</body>\n"
"</html>", None))
        self.btn_end_test.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
    # retranslateUi

