# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_test.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(997, 756)
        Dialog.setStyleSheet(u"QPushButton {\n"
"    background-color: lightgray; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px solid red; /* \u0426\u0432\u0435\u0442 \u0440\u0430\u043c\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"	border-radius: 5px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u0440\u0430\u043c\u043a\u0438 */\n"
"    background-color: lightgreen; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"QPushButton:focus {\n"
"      border: 2px solid red; /* \u0426\u0432\u0435\u0442 \u0440\u0430\u043c\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.checkBox_answer_b = QCheckBox(Dialog)
        self.checkBox_answer_b.setObjectName(u"checkBox_answer_b")
        self.checkBox_answer_b.setGeometry(QRect(800, 460, 79, 20))
        self.btn_accept_answer = QPushButton(Dialog)
        self.btn_accept_answer.setObjectName(u"btn_accept_answer")
        self.btn_accept_answer.setGeometry(QRect(590, 680, 271, 51))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 401, 590))
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

        self.checkBox_answer_c = QCheckBox(Dialog)
        self.checkBox_answer_c.setObjectName(u"checkBox_answer_c")
        self.checkBox_answer_c.setGeometry(QRect(530, 640, 79, 20))
        self.checkBox_answer_a = QCheckBox(Dialog)
        self.checkBox_answer_a.setObjectName(u"checkBox_answer_a")
        self.checkBox_answer_a.setGeometry(QRect(530, 460, 79, 20))
        self.checkBox_answer_d = QCheckBox(Dialog)
        self.checkBox_answer_d.setObjectName(u"checkBox_answer_d")
        self.checkBox_answer_d.setGeometry(QRect(800, 640, 79, 20))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 401, 41))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 690, 391, 51))
        self.text_quest = QTextEdit(Dialog)
        self.text_quest.setObjectName(u"text_quest")
        self.text_quest.setGeometry(QRect(450, 140, 531, 161))
        self.text_answer_a = QTextEdit(Dialog)
        self.text_answer_a.setObjectName(u"text_answer_a")
        self.text_answer_a.setGeometry(QRect(450, 340, 251, 111))
        self.text_answer_b = QTextEdit(Dialog)
        self.text_answer_b.setObjectName(u"text_answer_b")
        self.text_answer_b.setGeometry(QRect(720, 340, 261, 111))
        self.text_answer_c = QTextEdit(Dialog)
        self.text_answer_c.setObjectName(u"text_answer_c")
        self.text_answer_c.setGeometry(QRect(450, 520, 251, 91))
        self.text_answer_d = QTextEdit(Dialog)
        self.text_answer_d.setObjectName(u"text_answer_d")
        self.text_answer_d.setGeometry(QRect(720, 520, 261, 91))
        self.comboBox_theme = QComboBox(Dialog)
        self.comboBox_theme.setObjectName(u"comboBox_theme")
        self.comboBox_theme.setGeometry(QRect(450, 90, 531, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 30, 131, 16))
        self.label_2.setFont(font)
        self.list_test_name = QLineEdit(Dialog)
        self.list_test_name.setObjectName(u"list_test_name")
        self.list_test_name.setGeometry(QRect(610, 30, 113, 22))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(550, 310, 61, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(830, 310, 61, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(550, 500, 61, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(820, 500, 61, 16))
        self.label_6.setFont(font)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(450, 60, 131, 16))
        self.label_7.setFont(font)
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(450, 120, 131, 16))
        self.label_8.setFont(font)
        self.btn_exit = QPushButton(Dialog)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(770, 30, 181, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_answer_b.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.btn_accept_answer.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u043e\u043f\u0440\u043e\u0441 \u0441 \u043e\u0442\u0432\u0435\u0442\u0430\u043c\u0438", None))
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
        self.checkBox_answer_c.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_answer_a.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.checkBox_answer_d.setText(QCoreApplication.translate("Dialog", u"CheckBox", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0442\u0435\u0441\u0442\u0430/\u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u0441\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u0441\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 \u0430", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 b", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 c", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442 d", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043c\u0430 \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u043a\u0441\u0442 \u0432\u043e\u043f\u0440\u043e\u0441\u0430", None))
        self.btn_exit.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434 \u0432 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

