import random
import sys


from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox, QListWidgetItem, QTableWidgetItem

from window.mainwindow import Ui_MainWindow
from window.password import Ui_Dialog
from window.menu import Ui_Dialog as Ui_Dialog_menu
from window.add_test import Ui_Dialog as Ui_Dialog_add_test
from window.create_test_menu import Ui_Dialog as Ui_Dialog_create_test_menu
from window.list_test import Ui_Dialog as Ui_Dialog_list_test
from window.list_applicant import Ui_Dialog as Ui_Dialog_list_applicant
from window.test import Ui_Dialog as Ui_Dialog_test
from window.mid_menu_applicant import Ui_Dialog as Ui_Dialog_mid_menu_applicant
from window.applicant import Ui_Dialog as Ui_Dialog_applicant
from window.mid_menu_test import Ui_Dialog as Ui_Dialog_mid_menu_test

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

        self.mid_menu_applicant_dialog = None
        self.mid_menu_applicant_ui = None

        self.mid_menu_test_dialog = None
        self.mid_menu_test_ui = None

        # Устанавливаем изображение в label_logo
        self.pixmap = QPixmap("logo.png")  # Убедитесь, что путь к изображению правильный
        self.ui.label_logo.setPixmap(self.pixmap)  # Установка изображения в QLabel с именем label_logo

        DatabaseHelper.create_table()

        if self.menu_dialog is not None:
            self.menu_dialog.accept()  # Закрываем текущее окно

        # Привязываем нажатие кнопки к подготовке теста
        self.ui.btnstart_test.clicked.connect(self.prepare_test)

        # Привязываем нажатие кнопки к функции открытия новой формы
        self.ui.btn_go_menu.clicked.connect(self.open_pass_dialog)
        self.ui.btnclose.clicked.connect(self.close_current_window)

    def close_current_window(self):

        self.close()

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
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Внимание")
        msg.setText("Для прохождения теста Вам необходимо ответить на 37 вопросов."
                    "Отвечать можно в любом порядке. Для этого вы нажимаете на соответствующий "
                    "вопрос. Оно отобразится в окне справа. Под вопросом будут варианты ответа. "
                    "Вам нужно выбрать правильный вариант (правильных ответов может быть несколько). "
                    "Если вы уверены в своем выборе нажимайте на кнопку сохранить ответ. Отвеченный"
                    "вопрос выделяется зеленым цветом, но даже в этом случае, если Вы засомневались в ответе "
                    "и хоите его поменять, то Вы можете поменять свой ответ и снова нажать на кнопку сохранить. "
                    "Если вопрос Вам кажется сложным, то Вы можете перейти к любому другому вопросу,а к этому вернуться позднее. "
                    "Когда Вы ответите на все вопросы или решите, что на какие-то вопросы вы не хотите отвечать -  "
                    "нажмите на кнопку завершить тест.")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
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

        if self.list_test_dialog is not None:
            self.list_test_dialog.accept()  # Закрываем текущее окно
        if self.list_applicant_dialog is not None:
            self.list_applicant_dialog.accept()  # Закрываем текущее окно

        self.menu_dialog = QDialog()
        self.menu_ui = Ui_Dialog_menu()
        self.menu_ui.setupUi(self.menu_dialog)

        self.menu_ui.btn_addtest.clicked.connect(self.open_add_test)
        self.menu_ui.btn_list_test.clicked.connect(self.open_list_test)
        self.menu_ui.btn_list_applicant.clicked.connect(self.open_list_applicant)
        self.menu_ui.btn_exit.clicked.connect(self.menu_dialog.reject)

        self.menu_dialog.exec()

    def open_list_applicant(self):
        if self.mid_menu_applicant_dialog is not None:
            self.mid_menu_applicant_dialog.accept()

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

                # Устанавливаем applicant_id в качестве данных элемента
                item.setData(Qt.UserRole, applicant.id_applicant)

                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Делаем элемент выделяемым и активным
                self.list_applicant_ui.list_applicant.addItem(item)  # Добавляем элемент в QListWidget

        # Кнопка возврата в меню
        self.list_applicant_ui.btn_exit_to_menu.clicked.connect(self.open_menu)

        # Подключаем обработчик события двойного клика
        self.list_applicant_ui.list_applicant.itemDoubleClicked.connect(self.on_applicant_double_clicked)

        self.list_applicant_dialog.exec()

    def on_applicant_double_clicked(self, item):
        # Получаем id соискателя из данных элемента
        applicant_id = item.data(Qt.UserRole)  # Извлекаем id
        if applicant_id is not None:
            self.open_menu_applicant(applicant_id)  # Открываем форму редактирования соискателя
        else:
            QMessageBox.warning(self, "Ошибка", "ID соискателя не найден")


    def open_menu_applicant(self,applican_id):
        # закрываем спиоск
        if self.list_applicant_dialog is not None:
            self.list_applicant_dialog.accept()

        # Создаем и отображаем меню выбора действия с соискателем
        self.mid_menu_applicant_dialog = QDialog()
        self.mid_menu_applicant_ui = Ui_Dialog_mid_menu_applicant()
        self.mid_menu_applicant_ui.setupUi(self.mid_menu_applicant_dialog)

        # Создаем кнопки в меню

        self.mid_menu_applicant_ui.btn_exit.clicked.connect(self.open_list_applicant)
        self.mid_menu_applicant_ui.btn_open.clicked.connect(lambda: self.open_applicant(applican_id))
        self.mid_menu_applicant_ui.btn_delete.clicked.connect(lambda: self.delete_applicant(applican_id))

        self.mid_menu_applicant_dialog.exec()


    def delete_applicant(self, applicant_id):
        """Удаляет соискателя после подтверждения."""
        # Создаем диалоговое окно с вопросом
        reply = QMessageBox.question(self, 'Подтверждение удаления',
                                     "Точно хотите удалить соискателя?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Если пользователь нажал "Да", выполняем удаление
            DatabaseHelper.delete_applicant_and_answers(applicant_id)

            # Закрываем диалог или обновляем интерфейс после удаления
            if self.mid_menu_applicant_dialog is not None:
                self.mid_menu_applicant_dialog.accept()

            self.open_list_applicant()  # Например, обновляем список соискателей
        else:
            # Если пользователь нажал "Нет", игнорируем действие
            pass

    def open_applicant(self, applicant_id):
        """Загрузка формы просмотра тестирования соискателя"""
        if self.mid_menu_applicant_dialog is not None:
            self.mid_menu_applicant_dialog.accept()

        self.applicant_dialog = QDialog()
        self.applicant_ui = Ui_Dialog_applicant()
        self.applicant_ui.setupUi(self.applicant_dialog)

        # Получаем результаты тестирования соискателя
        result_summary = DatabaseHelper.open_applicant_result(applicant_id)

        if result_summary:
            # Заполнение полей формы
            self.applicant_ui.linefio.setText(result_summary['fio'])
            self.applicant_ui.line_test_name.setText(result_summary['test_name'])

            total_questions = result_summary["total_questions_all"]
            answered_questions = result_summary["answered_questions"]
            correct_answers_percent = result_summary["correct_answers_percent"]
            correct_answers_percent_all = result_summary["correct_answers_percent_all"]
            time = (result_summary["time"])/60

            # Обновление list_result
            self.applicant_ui.list_result.clear()  # Очищаем список перед добавлением новых результатов
            answered_questions_text = f"Соискатель ответил на {answered_questions} из {total_questions} вопросов."
            result_answered_text = f"Результат из учета отвеченных вопросов: {correct_answers_percent:.2f}%."
            result_all_text = f"Общий результат: {correct_answers_percent_all:.2f}%."
            all_time = f"Итоговое время составило: {time:.2f} минут."


            # Добавляем строки в list_result
            self.applicant_ui.list_result.addItem(answered_questions_text)
            self.applicant_ui.list_result.addItem("")  # Пустая строка
            self.applicant_ui.list_result.addItem(result_answered_text)
            self.applicant_ui.list_result.addItem(result_all_text)
            self.applicant_ui.list_result.addItem("")  # Пустая строка
            self.applicant_ui.list_result.addItem(all_time)
            self.applicant_ui.list_result.addItem("")  # Пустая строка

            theme_results = result_summary.get("theme_results", [])
            for theme_result in theme_results:
                theme_text = f"Тема: {theme_result['theme_name']}, Результат: {theme_result['correct_percent']:.2f}%."
                self.applicant_ui.list_result.addItem(theme_text)

            # Настройка QTableWidget для ответов соискателя
            self.applicant_ui.table_applicant_answer.setRowCount(6)  # 4 варианта ответа + 1 для времени
            self.applicant_ui.table_applicant_answer.setColumnCount(37)  # 37 вопросов

            # Установка заголовков для первого столбца
            self.applicant_ui.table_applicant_answer.setVerticalHeaderLabels([
                "Вопросы", "Ответ а", "Ответ b", "Ответ c", "Ответ d", "Затраченное время"
            ])

            # Установка заголовков для столбцов (например, вопросы 1-37)
            self.applicant_ui.table_applicant_answer.setHorizontalHeaderLabels(
                [str(i + 1) for i in range(37)]
            )

            for question_index in range(37):
                # Получаем ответы соискателя для текущего вопроса
                answers_for_question = [answer for answer in result_summary['applicant_answers'] if
                                        answer['question_id'] == question_index + 1]

                for answer_index in range(4):  # 4 строки для каждого варианта ответа
                    if answer_index < len(answers_for_question):
                        is_correct = answers_for_question[answer_index]['is_correct']
                        self.applicant_ui.table_applicant_answer.setItem(answer_index + 1, question_index,
                                                                         QTableWidgetItem(
                                                                             "Да" if is_correct else "Нет"))
                    else:
                        self.applicant_ui.table_applicant_answer.setItem(answer_index + 1, question_index,
                                                                         QTableWidgetItem(""))

                # Временные затраты (все варианты ответов имеют одинаковое время)
                if answers_for_question:
                    time_spent = answers_for_question[0]['time_spent']
                    self.applicant_ui.table_applicant_answer.setItem(5, question_index,
                                                                     QTableWidgetItem(str(time_spent)))

            # Настройка QTableWidget для правильных ответов
            self.applicant_ui.table_correct_answer.setRowCount(5)  # 4 варианта ответа + 1 для заголовков
            self.applicant_ui.table_correct_answer.setColumnCount(37)  # 37 вопросов

            # Установка заголовков для первого столбца
            self.applicant_ui.table_correct_answer.setVerticalHeaderLabels([
                "Вопросы", "Ответ а", "Ответ b", "Ответ c", "Ответ d"
            ])

            # Установка заголовков для столбцов (например, вопросы 1-37)
            self.applicant_ui.table_correct_answer.setHorizontalHeaderLabels(
                [str(i + 1) for i in range(37)]
            )

            for question_index in range(37):
                correct_answers_for_question = [answer for answer in result_summary['correct_answers'] if
                                                answer.question.id_quest == question_index + 1]

                for answer_index in range(4):  # 4 строки для каждого варианта ответа
                    if answer_index < len(correct_answers_for_question):
                        is_correct = correct_answers_for_question[answer_index].is_correct
                        self.applicant_ui.table_correct_answer.setItem(answer_index + 1, question_index,
                                                                       QTableWidgetItem("Да" if is_correct else "Нет"))
                    else:
                        self.applicant_ui.table_correct_answer.setItem(answer_index + 1, question_index,
                                                                       QTableWidgetItem(""))

        # Отображение диалога
        self.applicant_dialog.exec()

    def open_list_test(self):

        if self.mid_menu_test_dialog is not None:
            self.mid_menu_test_dialog.accept()

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

         # Получаем id теста из данных элемента
        test_id = item.data(Qt.UserRole)  # Извлекаем id
        # self.open_edit_test(test_id)  # Открываем форму редактирования теста
        self.open_menu_test(test_id)

    def open_menu_test(self, test_id):

        # закрываем спиоск
        if self.list_test_dialog is not None:
            self.list_test_dialog.accept()

        # загружаем форму

        self.mid_menu_test_dialog = QDialog()
        self.mid_menu_test_ui = Ui_Dialog_mid_menu_test()
        self.mid_menu_test_ui.setupUi(self.mid_menu_test_dialog)



        # кнопка удаления
        self.mid_menu_test_ui.btn_delete.clicked.connect(lambda: self.delete_test(test_id))

        # кнопка редактирования теста
        self.mid_menu_test_ui.btn_edit.clicked.connect(lambda: self.open_edit_test(test_id))

        # кнопка возврата
        self.mid_menu_test_ui.btn_exit.clicked.connect(self.open_list_test)


        self.mid_menu_test_dialog.exec()

    def delete_test(self, test_id):
        """Удаляем тесты после подтвреждения"""


        # Создаем диалоговое окно с вопросом
        reply = QMessageBox.question(self, 'Подтверждение удаления',
                                     "Вы точно хотите удалить тест?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            # Если пользователь нажал "Да", выполняем удаление
            DatabaseHelper.delete_tests_and_answers(test_id)

            # Закрываем диалог или обновляем интерфейс после удаления

            if self.mid_menu_test_dialog is not None:
                self.mid_menu_test_dialog.accept()

            self.open_list_test()  # Например, обновляем список тестов
        else:
            # Если пользователь нажал "Нет", игнорируем действие
            pass

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

        if self.mid_menu_test_dialog is not None:
            self.mid_menu_test_dialog.accept()
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
            self.ui.list_test_name.setReadOnly(True)  # Делаем поле доступным только для чтения
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

        self.ui.btn_exit.clicked.connect(self.close_current_window)

    def close_current_window(self):
        self.close()  # Закрывает текущее окно

    def on_question_button_clicked(self, question_number):
        """Вызывается при нажатии на кнопку вопроса."""
        #  добавляем красную рамку к выбранной кнопке
        self.highlight_button_red(question_number)

        # Загружаем вопрос
        self.load_question(question_number)

    def highlight_button_red(self, question_number):
        """Добавляет красную рамку к кнопке."""
        getattr(self.ui, f"btn_quest_{question_number}")
        # button.setStyleSheet("border: 2px solid red;")

    def highlight_button_green(self, question_number):
        """Изменяет фон кнопки на светло-зелёный."""
        getattr(self.ui, f"btn_quest_{question_number}")
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
        question = DatabaseHelper.get_question_by_index(self.test_id, question_number - 1)

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
    def __init__(self, fio: str):
        super(Testing, self).__init__()
        self.ui = Ui_Dialog_test()
        self.ui.setupUi(self)
        self.fio = fio

        self.current_questions = 0

        self.time_spent = 0  # Переменная для учета времени
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)  # Обновление таймера каждую секунду

        self.selected_question_number = None



        # Получаем тест по ID
        tests = DatabaseHelper.get_all_tests()

        if tests:
            self.random_test = random.choice(tests)

            self.ui.line_test.setText(str(self.random_test.id_test))  # Заполняем поле id_test теста
            self.ui.line_test.setReadOnly(True)  # Делаем поле доступным только для чтения
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

        # сразу создаем соискателя в базе
        DatabaseHelper.add_applicant(self.fio, self.random_test.id_test)

        self.applicant = DatabaseHelper.get_last_applicant()


        # Подключаем кнопки вопросов к обработчику
        for i in range(1, 38):
            button = getattr(self.ui, f"btn_quest_{i}")
            button.clicked.connect(lambda _, num=i: self.load_question(num))

        # Подключаем кнопку сохранения
        self.ui.btn_accept_answer.clicked.connect(self.save_applicant_answer)

        self.ui.btn_end_test.clicked.connect(lambda _, num=i: self.close_current_window(self.applicant.id_applicant))


    def close_current_window(self, applicant_id):

        result_summary = DatabaseHelper.open_applicant_result(applicant_id)

        if result_summary:
            total_questions = result_summary["total_questions_all"]
            answered_questions = result_summary["answered_questions"]
            correct_answers_percent = result_summary["correct_answers_percent"]
            correct_answers_percent_all = result_summary["correct_answers_percent_all"]

            answered_questions_text = f"Вы ответили на {answered_questions} из {total_questions} вопросов."
            result_answered_text = f"Результат из учета отвеченных вопросов: {correct_answers_percent:.2f}%."
            result_all_text = f"Общий результат: {correct_answers_percent_all:.2f}%."


            QMessageBox.warning(self, "Результаты", f"Ваши результаты {answered_questions_text} {result_answered_text} {result_all_text}")

        self.close()  # Закрывает текущее окно

    def update_time(self):
        """Увеличивает время на 1 секунду."""
        self.time_spent += 1

    def load_question(self, question_number):
        """Загружает вопрос из базы по номеру."""

        # Проверяем, был ли уже ответ на вопрос
        is_answered = DatabaseHelper.check_answer(
            id_applicantanswer_applicant=self.applicant.id_applicant,
            id_applicantanswer_questions=question_number
        )

        if not is_answered:

            # Сохраняем потраченное время на предыдущий вопрос
            if self.selected_question_number is not None:
                DatabaseHelper.presave_applicant_answer(
                    test_id=self.random_test.id_test,
                    time_spent=self.time_spent,
                    is_correct_a=False,
                    is_correct_b=False,
                    is_correct_c=False,
                    is_correct_d=False,
                    id_applicantanswer_applicant=self.applicant.id_applicant,
                    id_applicantanswer_questions=self.selected_question_number
                )
        else:
            # Получаем уже сохраненное время на текущем вопросе, если оно есть
            timer = DatabaseHelper.get_timer(
                id_applicantanswer_applicant=self.applicant.id_applicant,
                id_applicantanswer_questions=question_number
            )

            DatabaseHelper.get_application_answer_is_correct
            # Сохраняем потраченное время на предыдущий вопрос
            if self.selected_question_number is not None:
                DatabaseHelper.presave_applicant_answer(
                    test_id=self.random_test.id_test,
                    time_spent=timer+self.time_spent,
                    is_correct_a=False,
                    is_correct_b=False,
                    is_correct_c=False,
                    is_correct_d=False,
                    id_applicantanswer_applicant=self.applicant.id_applicant,
                    id_applicantanswer_questions=self.selected_question_number
                )

        # Запускаем таймер заново для нового вопроса
        self.selected_question_number = question_number
        self.time_spent = 0  # Сбрасываем счетчик времени для нового вопроса
        self.timer.start(1000)  # Обновление каждую секунду (1000 мс)


        self.selected_question_number = question_number


        # Получаем вопрос из базы по индексу
        question = DatabaseHelper.get_question_for_applicant_by_index(self.random_test.id_test, question_number - 1, self.applicant.id_applicant)

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

            if applicant_answers:
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

        # Получаем данные о правильных ответах
        is_correct_a = self.ui.checkBox_answer_a.isChecked()
        is_correct_b = self.ui.checkBox_answer_b.isChecked()
        is_correct_c = self.ui.checkBox_answer_c.isChecked()
        is_correct_d = self.ui.checkBox_answer_d.isChecked()

        # Получаем уже сохраненное время на текущем вопросе, если оно есть
        timer = DatabaseHelper.get_timer(
            id_applicantanswer_applicant=self.applicant.id_applicant,
            id_applicantanswer_questions=self.selected_question_number
        )
        # Сохраняем данные в базе
        DatabaseHelper.save_applicant_answer(
            is_correct_a=is_correct_a,
            is_correct_b=is_correct_b,
            is_correct_c=is_correct_c,
            is_correct_d=is_correct_d,
            test_id = self.random_test.id_test,
            time_spent = timer + self.time_spent,
            id_applicantanswer_applicant = self.applicant.id_applicant,
            id_applicantanswer_questions = self.selected_question_number
        )

        self.timer.stop()
        self.highlight_button_green(self.selected_question_number)

    def highlight_button_green(self, question_number):
        """Изменяет фон кнопки на светло-зелёный."""
        button = getattr(self.ui, f"btn_quest_{question_number}")
        button.setStyleSheet("background-color: lightgreen;")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Mainwindow()
    window.show()

    sys.exit(app.exec())
