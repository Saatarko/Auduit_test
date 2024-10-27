import os
import random
import sys

import PySide6
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QListWidgetItem, QLabel

from window.mainwindow import Ui_MainWindow
from window.password import Ui_Dialog
from window.menu import Ui_Dialog as Ui_Dialog_menu
from window.add_test import Ui_Dialog as Ui_Dialog_add_test
from window.create_test_menu import  Ui_Dialog as Ui_Dialog_create_test_menu
from window.list_test import Ui_Dialog as Ui_Dialog_list_test
from window.list_applicant import Ui_Dialog as Ui_Dialog_list_applicant
from window.test import Ui_Dialog as Ui_Dialog_test
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

        self.test_dialog = None
        self.test_ui = None


        self.list_test_dialog = None
        self.list_test_ui = None

        self.create_test_menu_dialog = None
        self.create_test_menu_ui = None

        self.list_applicant_dialog = None
        self.list_applicant_ui = None

        # Устанавливаем изображение в label_logo
        self.pixmap = QPixmap("logo.png")  # Убедитесь, что путь к изображению правильный
        self.ui.label_logo.setPixmap(self.pixmap)  # Установка изображения в QLabel с именем label_logo

        DatabaseHelper.create_table()

        # Привязываем нажатие кнопки к подготовке теста
        self.ui.btnstart_test.clicked.connect(self.prepare_test)

        # Привязываем нажатие кнопки к функции открытия новой формы
        self.ui.btn_go_menu.clicked.connect(self.open_pass_dialog)



    def prepare_test(self):

        # Получаем фио соискателя из поля
        fio = self.ui.linefio_edit.text()

        if fio:
            self.open_test(fio)
        else:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Ошибка входа")
            msg.setText("Вы не ввели свое ФИО")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()


    def open_test(self, fio: str):
        # Здесь создаем объект формы прохождения теста
        test_dialog = Testing(fio)
        test_dialog.exec()  # Открываем диалог


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
        self.menu_ui.btn_list_applicant.clicked.connect(self.open_list_applicant)

        self.menu_dialog.exec()



    def open_list_applicant(self):

        # закрываем меню
        if self.menu_dialog is not None:
            self.menu_dialog.accept()


        # Создаем и отображаем список тестов
        self.list_applicant_dialog = QDialog()
        self.list_applicant_ui = Ui_Dialog_list_applicant()
        self.list_applicant_ui.setupUi(self.list_applicant_dialog)

        # Получаем всех соискателей из базы данных
        applicants = DatabaseHelper.get_all_applicant()

        # Очищаем QListWidget перед добавлением новых элементов
        self.list_applicant_ui.list_applicant.clear()

        if not applicants:
            # Если соискателей нет, добавляем сообщение
            item = QListWidgetItem("Соискателей пока небыло")
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Делаем элемент выделяемым и активным
            self.list_applicant_ui.list_applicant.addItem(item)
        else:

            for applicant in applicants:
                fio = applicant.fio  # Получаем fio соискателя
                created_at = applicant.created_at.strftime("%Y-%m-%d %H:%M:%S")  # Форматируем дату
                item_text = f"{fio} - {created_at}"  # Формируем текст элемента
                item = QListWidgetItem(item_text)  # Создаем элемент списка
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Делаем элемент выделяемым и активным
                self.list_applicant_ui.list_applicant.addItem(item)  # Добавляем элемент в QListWidget

        # кнопка возврата в меню

        self.list_applicant_ui.btn_exit_to_menu.clicked.connect(self.open_menu)


        # Подключаем обработчик события двойного клика
        self.list_applicant_ui.list_applicant.itemDoubleClicked.connect(self.on_test_double_clicked)


        self.list_applicant_dialog.exec()





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

        # Инициализируем ComboBox темами
        self.load_themes_into_combobox()

        # Получаем тест по ID
        test = DatabaseHelper.get_tests_from_id(self.test_id)
        if test:
            self.ui.list_test_name.setText(test.name)  # Заполняем поле именем теста
            self.ui.list_test_name.setReadOnly(True)   # Делаем поле доступным только для чтения
        else:
            QMessageBox.warning(self, "Ошибка", "Тест не найден")

        questions = DatabaseHelper.get_all_questions()
        question_ids = {question_id for question_id, _ in questions}  # Собираем id вопросов в множество



        # Подключаем кнопки вопросов к обработчику
        for i in range(1, 38):
            button = getattr(self.ui, f"btn_quest_{i}")
            button.clicked.connect(lambda _, num=i: self.on_question_button_clicked(num))

            # Если вопрос с таким id существует, устанавливаем зелёный фон
            if i in question_ids:
                button.setStyleSheet("background-color: lightgreen;")

        # Подключаем кнопку сохранения
        self.ui.btn_accept_answer.clicked.connect(self.save_question)

    def on_question_button_clicked(self, question_number):
        """Вызывается при нажатии на кнопку вопроса."""
        #  добавляем красную рамку к выбранной кнопке
        self.highlight_button_red(question_number)

        # Загружаем вопрос
        self.load_question(question_number)


    def highlight_button_red(self, question_number):
        """Добавляет красную рамку к кнопке."""
        button = getattr(self.ui, f"btn_quest_{question_number}")
        # button.setStyleSheet("border: 2px solid red;")

    def highlight_button_green(self, question_number):
        """Изменяет фон кнопки на светло-зелёный."""
        button = getattr(self.ui, f"btn_quest_{question_number}")
        # button.setStyleSheet("background-color: lightgreen;")


    def load_themes_into_combobox(self):
        """Загружает список тем в ComboBox из базы данных."""
        themes = DatabaseHelper.get_all_themes()  # Метод для получения всех тем
        self.ui.comboBox_theme.clear()
        for theme in themes:
            self.ui.comboBox_theme.addItem(theme.name, theme.id_themas)

    def load_question(self, question_number):
        """Загружает вопрос из базы по номеру."""
        self.selected_question_number = question_number

        # Получаем вопрос из базы по индексу
        question = DatabaseHelper.get_question_by_index(self.test_id, question_number-1)

        if question:
            # Устанавливаем текст вопроса
            self.ui.text_quest.setText(question.name)

            # Извлекаем ответы для данного вопроса
            answers = question.answers
            # Упорядочиваем ответы по id_answer, если это необходимо
            answers.sort(key=lambda ans: ans.id_answer)


            # Назначаем текст и состояния для ответов, если они есть
            if len(answers) >= 1:
                self.ui.text_answer_a.setText(answers[0].name)
                self.ui.checkBox_answer_a.setChecked(answers[0].is_correct)
            if len(answers) >= 2:
                self.ui.text_answer_b.setText(answers[1].name)
                self.ui.checkBox_answer_b.setChecked(answers[1].is_correct)
            if len(answers) >= 3:
                self.ui.text_answer_c.setText(answers[2].name)
                self.ui.checkBox_answer_c.setChecked(answers[2].is_correct)
            if len(answers) >= 4:
                self.ui.text_answer_d.setText(answers[3].name)
                self.ui.checkBox_answer_d.setChecked(answers[3].is_correct)

            # Устанавливаем выбранную тему в ComboBox
            index = self.ui.comboBox_theme.findData(question.id_quest_themas)
            self.ui.comboBox_theme.setCurrentIndex(index)

            # Меняем цвет кнопки на зеленый для успешной загрузки
            self.highlight_button_green(question_number)
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
            self.ui.comboBox_theme.setCurrentIndex(-1)


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
        theme_name = self.ui.comboBox_theme.currentText()

        if not question_text or not theme_name or (not answer_a and not answer_b and not answer_c and not answer_d):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля перед сохранением.")
            return

        # Получаем данные о правильных ответах
        is_correct_a = self.ui.checkBox_answer_a.isChecked()
        is_correct_b = self.ui.checkBox_answer_b.isChecked()
        is_correct_c = self.ui.checkBox_answer_c.isChecked()
        is_correct_d = self.ui.checkBox_answer_d.isChecked()

        # Получаем ID для выбранной темы
        theme_id = DatabaseHelper.get_theme_id_by_name(theme_name)
        if theme_id is None:
            QMessageBox.warning(self, "Ошибка", f"Тема '{theme_name}' не найдена в базе данных.")
            return

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
            theme_id=theme_id
        )

        self.highlight_button_green(self.selected_question_number)
        QMessageBox.information(self, "Сохранение", f"Вопрос №{self.selected_question_number} успешно сохранен.")



class Testing(QDialog):
    # класс для формы сохранения теста
    def __init__(self, fio:str):
        super(Testing, self).__init__()
        self.ui = Ui_Dialog_test()
        self.ui.setupUi(self)
        self.fio = fio

        self.selected_question_number = None

        # Получаем тест по ID
        tests = DatabaseHelper.get_all_tests()

        if tests:
            self.random_test = random.choice(tests)

            self.ui.line_test.setText(str(self.random_test.id_test))  # Заполняем поле id_test теста
            self.ui.line_test.setReadOnly(True)   # Делаем поле доступным только для чтения
            # Делаем поле невидимым
            self.ui.line_test.hide()

            self.ui.line_fio.setText(self.fio)  # Заполняем поле id_test теста
            self.ui.line_fio.setReadOnly(True)  # Делаем поле доступным только для чтения
            # Делаем поле невидимым
            self.ui.line_fio.hide()

        else:
            QMessageBox.warning(self, "Ошибка", "Тест не найден")
            return

        questions = DatabaseHelper.get_all_questions()
        question_ids = {question_id for question_id, _ in questions}  # Собираем id вопросов в множество

        # Подключаем кнопки вопросов к обработчику
        for i in range(1, 38):
            button = getattr(self.ui, f"btn_quest_{i}")
            button.clicked.connect(lambda _, num=i: self.load_question(num))

        # Подключаем кнопку сохранения
        self.ui.btn_accept_answer.clicked.connect(self.save_applicant_answer)


    def load_question(self, question_number):
        """Загружает вопрос из базы по номеру."""
        self.selected_question_number = question_number

        # Получаем вопрос из базы по индексу
        question = DatabaseHelper.get_question_for_applicant_by_index(self.random_test.id_test, question_number-1)

        if question:
            self.ui.list_quest_test.clear()
            self.ui.list_answer_a.clear()
            self.ui.list_answer_b.clear()
            self.ui.list_answer_c.clear()
            self.ui.list_answer_d.clear()
            self.ui.checkBox_answer_a.setChecked(False)
            self.ui.checkBox_answer_b.setChecked(False)
            self.ui.checkBox_answer_c.setChecked(False)
            self.ui.checkBox_answer_d.setChecked(False)

            # Устанавливаем текст вопроса
            text = f"Тема вопроса: {question.thema.name}\n {question.name}"
            self.ui.list_quest_test.addItem(text)

            # Извлекаем ответы для данного вопроса
            answers = question.answers
            # Упорядочиваем ответы по id_answer
            answers.sort(key=lambda ans: ans.id_answer)

            # Назначаем текст и состояния для ответов, если они есть
            if len(answers) >= 1:
                self.ui.list_answer_a.addItem(answers[0].name)
            if len(answers) >= 2:
                self.ui.list_answer_b.addItem(answers[1].name)
            if len(answers) >= 3:
                self.ui.list_answer_c.addItem(answers[2].name)
            if len(answers) >= 4:
                self.ui.list_answer_d.addItem(answers[3].name)

            applicant_answers = question.applicant_answers

            if  applicant_answers:
                applicant_answers.sort(key=lambda ans: ans.id_applicantAnswer)
                # Назначаем текст и состояния для ответов, если они есть
                if len(applicant_answers) >= 1:
                    self.ui.checkBox_answer_a.setChecked(applicant_answers[0].is_correct)
                if len(applicant_answers) >= 2:
                    self.ui.checkBox_answer_b.setChecked(applicant_answers[1].is_correct)
                if len(applicant_answers) >= 3:
                    self.ui.checkBox_answer_c.setChecked(applicant_answers[2].is_correct)
                if len(applicant_answers) >= 4:
                    self.ui.checkBox_answer_d.setChecked(applicant_answers[3].is_correct)
            else:
                self.ui.checkBox_answer_a.setChecked(False)
                self.ui.checkBox_answer_b.setChecked(False)
                self.ui.checkBox_answer_c.setChecked(False)
                self.ui.checkBox_answer_d.setChecked(False)

        else:
            # Очищаем поля, если вопрос не найден
            self.ui.list_quest_test.clear()
            self.ui.list_answer_a.clear()
            self.ui.list_answer_b.clear()
            self.ui.list_answer_c.clear()
            self.ui.list_answer_d.clear()
            self.ui.checkBox_answer_a.setChecked(False)
            self.ui.checkBox_answer_b.setChecked(False)
            self.ui.checkBox_answer_c.setChecked(False)
            self.ui.checkBox_answer_d.setChecked(False)

    def save_applicant_answer(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window =  Mainwindow()
    window.show()

    sys.exit(app.exec())