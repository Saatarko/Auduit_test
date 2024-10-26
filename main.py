import os
import sys

import PySide6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QListWidgetItem

from window.mainwindow import Ui_MainWindow
from window.password import Ui_Dialog
from window.menu import Ui_Dialog as Ui_Dialog_menu
from window.add_test import Ui_Dialog as Ui_Dialog_add_test
from window.create_test_menu import  Ui_Dialog as Ui_Dialog_create_test_menu
from window.list_test import Ui_Dialog as Ui_Dialog_list_test
from core.crud import DatabaseHelper


class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pass_dialog = None
        self.pass_ui = None

        self.menu_dialog = None
        self.menu_ui = None

        self.list_test_dialog = None
        self.list_test_ui = None

        self.create_test_menu_dialog = None
        self.create_test_menu_ui = None

        DatabaseHelper.create_table()



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

        if self.list_test_ui is not None:
            self.list_test_dialog.accept()  # Закрываем текущее окно

        self.menu_dialog = QDialog()
        self.menu_ui = Ui_Dialog_menu()
        self.menu_ui.setupUi(self.menu_dialog)

        self.menu_ui.btn_addtest.clicked.connect(self.open_add_test)
        self.menu_ui.btn_list_test.clicked.connect(self.open_list_test)


        self.menu_dialog.exec()


    def open_list_test(self):

        # закрываем меню
        if self.menu_dialog is not None:
            self.menu_dialog.accept()


        # Создаем и отображаем список тестов
        self.list_test_dialog = QDialog()
        self.list_test_ui = Ui_Dialog_list_test()
        self.list_test_ui.setupUi(self.list_test_dialog)

        # Получаем все тесты из базы данных
        tests = DatabaseHelper.get_all_tests()

        # Очищаем QListWidget перед добавлением новых элементов
        self.list_test_ui.list_test.clear()

        if not tests:
            # Если тестов нет, добавляем сообщение
            item = QListWidgetItem("Тестов нет")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Делаем элемент выделяемым и активным
            self.list_test_ui.list_test.addItem(item)
        else:
            # Добавляем названия тестов в QListWidget
            for test_id, test_name in tests:
                item = QListWidgetItem(test_name)
                item.setData(Qt.UserRole, test_id)  # Сохраняем id теста в данных элемента
                self.list_test_ui.list_test.addItem(item)

        # кнопка возврата в меню

        self.list_test_ui.btn_exit_to_menu.clicked.connect(self.open_menu)


        # Подключаем обработчик события двойного клика
        self.list_test_ui.list_test.itemDoubleClicked.connect(self.on_test_double_clicked)


        self.list_test_dialog.exec()

    def on_test_double_clicked(self, item):

        # закрываем спиоск
        if self.list_test_dialog is not None:
            self.list_test_dialog.accept()



        # Получаем id теста из данных элемента
        test_id = item.data(Qt.UserRole)  # Извлекаем id
        self.open_edit_test(test_id)  # Открываем форму редактирования теста


    def open_add_test(self):

        # Создаем и отображаем диалоговое окно для добавления теста
        self.create_test_menu_dialog = QDialog()
        self.create_test_menu_ui = Ui_Dialog_create_test_menu()
        self.create_test_menu_ui.setupUi(self.create_test_menu_dialog)

        self.create_test_menu_ui.btn_create_test.clicked.connect(self.handle_create_test)


        self.create_test_menu_dialog.exec()

    def handle_create_test(self):
        test_name = self.create_test_menu_ui.line_name_test.text()  # Получаем название теста из поля
        if test_name:

            try:
                DatabaseHelper.add_test(test_name)  # Метод для добавления теста в базу
                # После добавления теста, получаем его id
                test_id = DatabaseHelper.get_test_id_by_name(test_name)  # Получаем id теста из таблицы
            except Exception as e:
                print(f"Ошибка при создании теста: {e}")
                return None  # Возвращаем None в случае ошибки

            if test_id is not None:
                # Если тест успешно создан, открываем форму редактирования теста
                self.open_edit_test(test_id)
            else:
                # Обработка случая, если создание теста не удалось
                QMessageBox.warning(self, "Ошибка", "Не удалось создать тест.")
        else:
            QMessageBox.warning(self, "Ошибка", "Введите название теста.")


    def open_edit_test(self, test_id: int):
        # Здесь создаем объект формы редактирования теста
        edit_test_dialog = EditTestDialog(test_id)
        edit_test_dialog.exec()  # Открываем диалог


class EditTestDialog(QDialog):
    # класс для формы сохранения теста
    def __init__(self, test_id: int):
        super(EditTestDialog, self).__init__()
        self.ui = Ui_Dialog_add_test()
        self.ui.setupUi(self)
        self.test_id = test_id

        self.selected_question_number = None

        # Получаем тест по ID
        test = DatabaseHelper.get_tests_from_id(self.test_id)
        if test:
            self.ui.list_test_name.setText(test.name)  # Заполняем поле именем теста
            self.ui.list_test_name.setReadOnly(True)   # Делаем поле доступным только для чтения
        else:
            QMessageBox.warning(self, "Ошибка", "Тест не найден")

        # Подключаем кнопки вопросов к обработчику
        for i in range(1, 37):
            button = getattr(self.ui, f"btn_quest_{i}")
            button.clicked.connect(lambda _, num=i: self.load_question(num))

        # Подключаем кнопку сохранения
        self.ui.btn_accept_answer.clicked.connect(self.save_question)

    def load_question(self, question_number):
        """Загружает вопрос из базы по номеру."""
        self.selected_question_number = question_number

        # Получаем вопрос из базы
        question = DatabaseHelper.get_question_by_test_id_and_number(self.test_id, question_number)

        if question:
            # Заполняем данные вопроса и ответов
            self.ui.text_quest.setText(question.text)
            self.ui.text_answer_a.setText(question.answer_a)
            self.ui.text_answer_b.setText(question.answer_b)
            self.ui.text_answer_c.setText(question.answer_c)
            self.ui.text_answer_d.setText(question.answer_d)

            # Устанавливаем состояния CheckBox для правильных ответов
            self.ui.checkBox_answer_a.setChecked(question.is_correct_a)
            self.ui.checkBox_answer_b.setChecked(question.is_correct_b)
            self.ui.checkBox_answer_c.setChecked(question.is_correct_c)
            self.ui.checkBox_answer_d.setChecked(question.is_correct_d)

            # Устанавливаем выбранную тему в ComboBox
            index = self.ui.comboBox_theme.findText(question.theme)
            self.ui.comboBox_theme.setCurrentIndex(index)
        else:
            # Очищаем поля, если вопрос не найден
            self.ui.text_quest.clear()
            self.ui.text_answer_a.clear()
            self.ui.text_answer_b.clear()
            self.ui.text_answer_c.clear()
            self.ui.text_answer_d.clear()
            self.ui.checkBox_answer_a.setChecked(False)
            self.ui.checkBox_answer_b.setChecked(False)
            self.ui.checkBox_answer_c.setChecked(False)
            self.ui.checkBox_answer_d.setChecked(False)
            self.ui.comboBox_theme.setCurrentIndex(-1)  # Сбрасываем выбор темы

    def save_question(self):
        """Сохраняет текущий вопрос в базу данных."""
        if self.selected_question_number is None:
            QMessageBox.warning(self, "Ошибка", "Выберите вопрос для сохранения.")
            return

        # Проверяем заполненность данных
        question_text = self.ui.text_quest.toPlainText()
        answer_a = self.ui.text_answer_a.toPlainText()
        answer_b = self.ui.text_answer_b.toPlainText()
        answer_c = self.ui.text_answer_c.toPlainText()
        answer_d = self.ui.text_answer_d.toPlainText()
        theme = self.ui.comboBox_theme.currentText()

        if not question_text or not answer_a or not answer_b or not answer_c or not answer_d or not theme:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля перед сохранением.")
            return

        # Получаем данные о правильных ответах
        is_correct_a = self.ui.checkBox_answer_a.isChecked()
        is_correct_b = self.ui.checkBox_answer_b.isChecked()
        is_correct_c = self.ui.checkBox_answer_c.isChecked()
        is_correct_d = self.ui.checkBox_answer_d.isChecked()

        # Сохраняем данные в базе
        DatabaseHelper.save_question(
            test_id=self.test_id,
            question_number=self.selected_question_number,
            text=question_text,
            answer_a=answer_a,
            answer_b=answer_b,
            answer_c=answer_c,
            answer_d=answer_d,
            is_correct_a=is_correct_a,
            is_correct_b=is_correct_b,
            is_correct_c=is_correct_c,
            is_correct_d=is_correct_d,
            theme=theme
        )

        QMessageBox.information(self, "Сохранение", f"Вопрос №{self.selected_question_number} успешно сохранен.")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window =  Mainwindow()
    window.show()

    sys.exit(app.exec())