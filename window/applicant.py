# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'applicant.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(919, 692)
        Dialog.setStyleSheet(u"QPushButton:focus {\n"
"      border: 2px solid red; /* \u0426\u0432\u0435\u0442 \u0440\u0430\u043c\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 101, 16))
        self.linefio = QLineEdit(Dialog)
        self.linefio.setObjectName(u"linefio")
        self.linefio.setGeometry(QRect(90, 30, 191, 22))
        self.table_applicant_answer = QTableWidget(Dialog)
        self.table_applicant_answer.setObjectName(u"table_applicant_answer")
        self.table_applicant_answer.setGeometry(QRect(40, 100, 621, 221))
        self.table_correct_answer = QTableWidget(Dialog)
        self.table_correct_answer.setObjectName(u"table_correct_answer")
        self.table_correct_answer.setGeometry(QRect(40, 420, 621, 201))
        self.list_result = QListWidget(Dialog)
        self.list_result.setObjectName(u"list_result")
        self.list_result.setGeometry(QRect(690, 100, 211, 541))
        self.list_result.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_result.setWordWrap(True)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 70, 111, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 390, 111, 16))
        self.line_test_name = QLineEdit(Dialog)
        self.line_test_name.setObjectName(u"line_test_name")
        self.line_test_name.setGeometry(QRect(460, 30, 191, 22))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 30, 101, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0438\u0441\u043a\u0430\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0432\u0435\u0442\u044b \u0441\u043e\u0438\u0441\u043a\u0430\u0442\u0435\u043b\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0440\u0440\u0435\u043a\u0442\u043d\u044b\u0435 \u043e\u0442\u0432\u0435\u0442\u044b", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0422\u0435\u0441\u0442", None))
    # retranslateUi

