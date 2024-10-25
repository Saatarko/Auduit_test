import os
import sys

import PySide6
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from mainwindow import Ui_MainWindow
from sqlalchemy import create_engine
from password import Ui_Dialog
from menu import Ui_Dialog as Ui_Dialog_menu
from add_test import Ui_Dialog as Ui_Dialog_add_test

from sqlalchemy.orm import Session


engine = create_engine("sqlite+pysqlite:///base.db", echo = True)

basedir = os.path.abspath(os.path.dirname(PySide6.__file__))
plugin_path =  os.path.join(basedir, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Привязываем нажатие кнопки к функции открытия новой формы
        self.ui.btn_go_menu.clicked.connect(self.open_pass_dialog)

    def open_pass_dialog(self):
        # Создаем и отображаем диалоговое окно из password.py
        self.pass_dialog = QDialog()
        self.pass_ui = Ui_Dialog()
        self.pass_ui.setupUi(self.pass_dialog)

        # Привязываем кнопку входа к проверке логина и пароля
        self.pass_ui.btn_enter.clicked.connect(self.check_login)
        self.pass_dialog.exec()


    def check_login(self):
        # Получаем данные из полей логина и пароля
        login = self.pass_ui.linelogin.text()
        password = self.pass_ui.linepass.text()

        # Проверяем логин и пароль (на соответствие заданным значениям)
        if login == "admin" and password == "1234":
            # Если логин и пароль верные, закрываем диалог входа и открываем меню
            self.pass_dialog.accept()  # Закрываем диалог входа
            self.open_menu()
        else:
            # Логин или пароль неверны, можно отобразить сообщение
            # Логин или пароль неверны, показываем сообщение для пользователя
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Ошибка входа")
            msg.setText("Неверный логин или пароль. Попробуйте еще раз.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()


    def open_menu(self):
        # Создаем и отображаем меню
        self.menu_dialog = QDialog()
        self.menu_ui = Ui_Dialog_menu()
        self.menu_ui.setupUi(self.menu_dialog)

        self.menu_ui.btn_addtest.clicked.connect(self.open_add_test)

        self.menu_dialog.exec()

    def open_add_test(self):
        # Создаем и отображаем диалоговое окно для добавления теста
        self.add_test_dialog = QDialog()
        self.add_test_ui = Ui_Dialog_add_test()
        self.add_test_ui.setupUi(self.add_test_dialog)

        self.add_test_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window =  Mainwindow()
    window.show()

    sys.exit(app.exec())