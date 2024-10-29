from PySide6.QtWidgets import QMessageBox
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

from .config import Base, engine, SessionLocal
from .models import Tests, Questions, Themas, Answer, Applicant, ApplicantAnswer


class DatabaseHelper:
    # def __init__(self, session: Session):
    #     self.session = session


    @staticmethod
    def create_table():
        Base.metadata.create_all(bind=engine)

    @staticmethod
    def add_test(test_name: str):
        # Используем `with` для автоматического закрытия сессии после использования
        with SessionLocal() as session:
            new_test = Tests(name=test_name)
            session.add(new_test)
            try:
                session.commit()
            except Exception as e:
                session.rollback()  # Откатываем изменения при ошибке
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Ошибка")
                msg.setText(f"Ошибка при добавлении теста: {e}")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

    @staticmethod
    def get_test_id_by_name(test_name: str):
        with SessionLocal() as session:
            # Используем запрос для поиска теста по имени
            result = session.query(Tests).filter(Tests.name == test_name).order_by(Tests.id_test.desc()).first()
            return result.id_test if result else None  # Возвращаем id, если тест найден

    @staticmethod
    def get_all_tests():
        with SessionLocal() as session:
            # Используем запрос для получения id и name тестов
            results = session.query(Tests.id_test, Tests.name).all()
            return results

    @staticmethod
    def get_all_applicant():
        with SessionLocal() as session:
            # Используем запрос для получения id и name соискателей
            results = session.query(Applicant.id_applicant, Applicant.fio, Applicant.created_at).all()
            return results

    @staticmethod
    def get_all_themes():
        with SessionLocal() as session:
            # Используем запрос для получения id и name тем
            results = session.query(Themas.id_themas, Themas.name).all()
            return results

    @staticmethod
    def get_tests_from_id(test_id):
        """Функция получения теста по id"""
        with SessionLocal() as session:
            result = session.get(Tests, test_id)
            return result

    @staticmethod
    def get_all_questions():
        """Функция получения всех вопросов"""

        with SessionLocal() as session:
            # Используем запрос для получения id и name тем
            results = session.query(Questions.id_quest, Questions.name).all()
            return results


    @staticmethod
    def get_question_by_index(test_id, question_index):
        with SessionLocal() as session:
            # Загружаем вопрос вместе с ответами с помощью joinedload
            questions = (
                session.query(Questions)
                .filter_by(id_quest_test=test_id)
                .options(joinedload(Questions.answers))  # Подгружаем ответы
                .order_by(Questions.id_quest)
                .all()
            )
            if 0 <= question_index < len(questions):
                return questions[question_index]
            return None

    @staticmethod
    def save_question(test_id, question_number, text, answer_a, answer_b, answer_c, answer_d,
                      is_correct_a, is_correct_b, is_correct_c, is_correct_d, theme_id):
        with SessionLocal() as session:
            # Находим или создаем вопрос
            question = (
                session.query(Questions)
                .filter_by(id_quest_test=test_id, id_quest=question_number)
                .first()
            )

            if not question:
                # Если вопрос не найден, создаем новый
                question = Questions(
                    id_quest_test=test_id,
                    name=text,
                    id_quest_themas=theme_id
                )
                session.add(question)
                session.commit()  # Фиксируем, чтобы получить id_quest для ответов
            else:
                # Обновляем существующий вопрос
                question.name = text
                question.id_quest_themas = theme_id

            # Сохраняем изменения вопроса
            session.commit()

            # Ответы для вопроса
            answers_data = [
                (answer_a, is_correct_a),
                (answer_b, is_correct_b),
                (answer_c, is_correct_c),
                (answer_d, is_correct_d)
            ]

            # Находим существующие ответы для этого вопроса
            existing_answers = session.query(Answer).filter_by(id_answer_quest=question.id_quest).all()

            for i, (answer_text, is_correct) in enumerate(answers_data):
                if i < len(existing_answers):
                    # Обновляем существующие ответы
                    existing_answers[i].name = answer_text
                    existing_answers[i].is_correct = is_correct
                else:
                    # Создаем новый ответ, если его нет
                    new_answer = Answer(
                        name=answer_text,
                        is_correct=is_correct,
                        id_answer_quest=question.id_quest
                    )
                    session.add(new_answer)

            # Сохраняем все изменения
            session.commit()

    @staticmethod
    def get_theme_id_by_name(theme_name):
        with SessionLocal() as session:
            theme = session.query(Themas).filter_by(name=theme_name).first()
            return theme.id_themas if theme else None

    @staticmethod
    def get_question_for_applicant_by_index(test_id, question_index, applicant_id):
        with SessionLocal() as session:
            # Загружаем вопрос, варианты ответов и тему
            question_query = (
                session.query(Questions)
                .filter(
                    Questions.id_quest_test == test_id)  # Используем filter вместо filter_by для более сложных условий
                .options(
                    joinedload(Questions.answers),  # Подгружаем варианты ответа
                    joinedload(Questions.thema)  # Подгружаем тему вопроса
                )
            )

            # Получаем все вопросы
            questions = question_query.all()

            if 0 <= question_index < len(questions):
                question = questions[question_index]

                # Фильтруем ответы соискателя по applicant_id
                applicant_answers = (
                    session.query(ApplicantAnswer)
                    .filter(ApplicantAnswer.id_applicantanswer_applicant == applicant_id,
                            ApplicantAnswer.id_applicantanswer_questions == question.id_quest)
                    .all()
                )
                question.applicant_answers = applicant_answers  # Заменяем на отфильтрованные ответы

                return question

            return None

    @staticmethod
    def add_applicant(applicant_name: str, id_applicant_test: int):
        # Используем `with` для автоматического закрытия сессии после использования
        with SessionLocal() as session:
            new_applicant = Applicant(fio=applicant_name, id_applicant_test=id_applicant_test)
            session.add(new_applicant)
            try:
                session.commit()
                print('Соискатель успешно добавлен')
            except Exception as e:
                session.rollback()  # Откатываем изменения при ошибке
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Ошибка")
                msg.setText(f"Ошибка при добавлении запуске теста: {e}")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()

    @staticmethod
    def get_last_applicant():
        with SessionLocal() as session:
            # Запрос для получения последнего соискателя по дате создания (или id)
            result = (
                session.query(Applicant.id_applicant, Applicant.fio, Applicant.created_at)
                .order_by(desc(Applicant.created_at))  # или desc(Applicant.id_applicant) для сортировки по id
                .first()
            )
            return result

    @staticmethod
    def presave_applicant_answer(
            test_id: int,
            time_spent: int,
            is_correct_a: bool,
            is_correct_b: bool,
            is_correct_c: bool,
            is_correct_d: bool,
            id_applicantanswer_applicant: int,
            id_applicantanswer_questions: int
    ):
        with SessionLocal() as session:
            # Получаем все ответы для текущего вопроса и соискателя
            answers = session.query(ApplicantAnswer).filter_by(
                id_applicantanswer_applicant=id_applicantanswer_applicant,
                id_applicantanswer_questions=id_applicantanswer_questions
            ).all()

            # проверяем был ли уже созраненный ответ
            if answers:
                if answers[0].is_correct is True or answers[1].is_correct is True or answers[2].is_correct is True or answers[3].is_correct is True:
                    for answer in answers:
                        answer.time_spent = time_spent
            else:
                # Если ответов не существует, создаем записи для каждого варианта ответа
                answers = [
                    ApplicantAnswer(
                        id_applicantanswer_applicant=id_applicantanswer_applicant,
                        id_applicantanswer_questions=id_applicantanswer_questions,
                        time_spent=time_spent,
                        is_correct=is_correct  # начальное значение, если ответ не выбран
                    )
                    for is_correct in (is_correct_a, is_correct_b, is_correct_c, is_correct_d)
                ]
                session.add_all(answers)

            # Сохраняем изменения в базе данных
            session.commit()

    @staticmethod
    def get_application_answer_is_correct(
            id_applicantanswer_applicant: int,
            id_applicantanswer_questions: int
    ):
        with SessionLocal() as session:
            answers = session.query(ApplicantAnswer).filter_by(
                id_applicantanswer_applicant=id_applicantanswer_applicant,
                id_applicantanswer_questions=id_applicantanswer_questions
            ).all()

        return answers


    @staticmethod
    def get_timer(
            id_applicantanswer_applicant: int,
            id_applicantanswer_questions: int
            ):

        with SessionLocal() as session:
            # Проверяем, есть ли уже ответ на этот вопрос от соискателя
            answers = session.query(ApplicantAnswer).filter_by(
                id_applicantanswer_applicant=id_applicantanswer_applicant,
                id_applicantanswer_questions=id_applicantanswer_questions
            ).all()

            if answers:
                # Получаем время из первой записи, так как оно одинаковое для всех ответов
                time_spent = answers[0].time_spent
            else:
                time_spent = 0  # Или любое другое значение по умолчанию, если записи нет


            return time_spent

    @staticmethod
    def save_applicant_answer(
            test_id: int,
            time_spent: int,
            is_correct_a: bool,
            is_correct_b: bool,
            is_correct_c: bool,
            is_correct_d: bool,
            id_applicantanswer_applicant: int,
            id_applicantanswer_questions: int
    ):
        with SessionLocal() as session:
            # Получаем все ответы для текущего вопроса и соискателя
            answers = session.query(ApplicantAnswer).filter_by(
                id_applicantanswer_applicant=id_applicantanswer_applicant,
                id_applicantanswer_questions=id_applicantanswer_questions
            ).all()

            is_correct_list = [is_correct_a, is_correct_b, is_correct_c, is_correct_d]

            if answers:
                # Если ответы уже существуют, обновляем только время
                for i, answer in enumerate(answers):
                    if i < len(is_correct_list):
                        answer.time_spent = time_spent
                        answer.is_correct = is_correct_list[i]
            else:
                # Если ответов не существует, создаем записи для каждого варианта ответа
                answers = [
                    ApplicantAnswer(
                        id_applicantanswer_applicant=id_applicantanswer_applicant,
                        id_applicantanswer_questions=id_applicantanswer_questions,
                        time_spent=time_spent,
                        is_correct=is_correct  # начальное значение, если ответ не выбран
                    )
                    for is_correct in (is_correct_a, is_correct_b, is_correct_c, is_correct_d)
                ]
                session.add_all(answers)

            # Сохраняем изменения в базе данных
            session.commit()

    @staticmethod
    def check_answer(
            id_applicantanswer_applicant: int,
            id_applicantanswer_questions: int
            ):

        with SessionLocal() as session:
            # Получаем все ответы для текущего вопроса и соискателя
            answers = session.query(ApplicantAnswer).filter_by(
                id_applicantanswer_applicant=id_applicantanswer_applicant,
                id_applicantanswer_questions=id_applicantanswer_questions
            ).all()

            if answers:
                # Если ответы уже существуют, обновляем только время
                for answer in answers:
                    if answer.is_correct is True:
                       return True
            else:
                return False

    def delete_applicant_and_answers(applicant_id: int):
        with SessionLocal() as session:
            # Находим соискателя
            applicant = session.query(Applicant).filter_by(id_applicant=applicant_id).first()

            if not applicant:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Ошибка")
                msg.setText(f"Такой соискатель не найден")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
                return

            # Удаляем все ответы, связанные с этим соискателем
            session.query(ApplicantAnswer).filter_by(id_applicantanswer_applicant=applicant_id).delete()

            # Удаляем самого соискателя
            session.delete(applicant)

            # Подтверждаем изменения в базе
            session.commit()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Внимание")
            msg.setText(f"Соискатель успешно удален")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

    @staticmethod
    def open_applicant_result(applicant_id):
        """Получает данные о результатах тестирования соискателя по его ID."""
        with SessionLocal() as session:
            # Получаем информацию о соискателе
            applicant = session.query(Applicant).filter(Applicant.id_applicant == applicant_id).one_or_none()

            if not applicant:
                return None

            # Получаем тест, связанный с соискателем
            test = session.query(Tests).filter(Tests.id_test == applicant.id_applicant_test).one_or_none()

            # Получаем ответы соискателя и подгружаем связанные объекты
            applicant_answers = session.query(ApplicantAnswer).options(
                joinedload(ApplicantAnswer.question)
            ).filter(
                ApplicantAnswer.id_applicantanswer_applicant == applicant_id
            ).all()

            # Список ответов соискателя с деталями
            applicant_answers_list = []
            for answer in applicant_answers:
                applicant_answers_list.append({
                    "question_id": answer.question.id_quest if answer.question else None,
                    "is_correct": answer.is_correct,
                    "time_spent": answer.time_spent
                })

            # Подсчитываем правильные ответы и прочие данные для теста
            correct_answers = session.query(Answer).options(
                joinedload(Answer.question)
            ).join(Questions).filter(
                Questions.id_quest_test == applicant.id_applicant_test
            ).all()


            # Формируем словарь для результатов
            results_dict = {}
            missing_questions = set(range(1, 38))  # Номера вопросов от 1 до 37
            answered_questions_count = 0


            # переменная для подсчет времени

            time = 0

            # Группируем правильные ответы по вопросам
            correct_answers_by_question = {}
            for answer in correct_answers:
                question_id = answer.question.id_quest
                if question_id not in correct_answers_by_question:
                    correct_answers_by_question[question_id] = []
                correct_answers_by_question[question_id].append(answer)

            # Сравниваем ответы соискателя с правильными ответами
            for question_id in range(1, 38):  # Для вопросов с 1 по 37




                if question_id in correct_answers_by_question:
                    correct_answers_list = correct_answers_by_question[question_id]
                    correct_count = sum(1 for answer in correct_answers_list if answer.is_correct)
                    matching_correct_answers = 0

                    # Получаем ответы соискателя для текущего вопроса
                    applicant_answers_for_question = [
                        answer for answer in applicant_answers if answer.question.id_quest == question_id
                    ]

                    if applicant_answers_for_question:
                        # answered_questions_count += 1  # Увеличиваем счетчик отвеченных вопросов
                        time += applicant_answers_for_question[0].time_spent
                        # Подсчитываем количество правильных ответов
                        for i in range(0,3):
                            if (correct_answers_list[i].is_correct is True) and (applicant_answers_for_question[i].is_correct is True):
                                matching_correct_answers += 1

                        if all(not answer.is_correct for answer in applicant_answers_for_question):
                            # Если все ответы не правильные, но вопрос прочитали
                            results_dict[
                                question_id] = 0  # Здесь можно задать любое значение, которое будет означать "не ответили"
                            missing_questions.remove(question_id)

                        else:
                            answered_questions_count += 1
                            if correct_count == 1:
                                # Один правильный ответ
                                results_dict[question_id] = 1 if matching_correct_answers == 1 else 0
                            elif correct_count == 2:
                                # Два правильных ответа
                                if matching_correct_answers == 2:
                                    results_dict[question_id] = 1
                                elif matching_correct_answers == 1:
                                    results_dict[question_id] = 0.5
                                else:
                                    results_dict[question_id] = 0
                            elif correct_count == 3:
                                # Три правильных ответа
                                if matching_correct_answers == 3:
                                    results_dict[question_id] = 1
                                elif matching_correct_answers == 2:
                                    results_dict[question_id] = 0.66
                                elif matching_correct_answers == 1:
                                    results_dict[question_id] = 0.33
                                else:
                                    results_dict[question_id] = 0
                    else:
                        # Вопрос не был отвечен
                        results_dict[
                            question_id] = 0
                        # missing_questions.remove(question_id)

            # Подсчитываем результаты
            total_questions_all = 37
            total_answered = answered_questions_count
            correct_answers_sum = sum(results_dict.values())

            # Процент правильных ответов
            if total_answered > 0:
                percentage_correct_answered = (correct_answers_sum / total_answered) * 100
            else:
                percentage_correct_answered = 0

            # Процент правильных ответов из всех вопросов
            percentage_correct_all = (correct_answers_sum / total_questions_all) * 100

            # Получаем все вопросы с темами
            question_with_thema = session.query(Questions).options(
                joinedload(Questions.thema)
            ).all()

            # Группируем данные по темам
            theme_scores = {}
            theme_counts = {}

            for question in question_with_thema:
                theme_name = question.thema.name if question.thema else "Неизвестная тема"

                # Инициализируем тему, если еще не добавлена в словари
                if theme_name not in theme_scores:
                    theme_scores[theme_name] = 0
                    theme_counts[theme_name] = 0

                # Добавляем оценку вопроса в тему, если вопрос есть в results_dict
                if question.id_quest in results_dict:
                    theme_scores[theme_name] += results_dict[question.id_quest]
                    theme_counts[theme_name] += 1

            # Рассчитываем процент правильных ответов по каждой теме
            theme_results = []
            for theme_name, score_sum in theme_scores.items():
                total_questions = theme_counts[theme_name]
                theme_percentage = (score_sum / total_questions * 100) if total_questions > 0 else 0
                theme_results.append({"theme_name": theme_name, "correct_percent": theme_percentage})

            result_summary = {
                "fio": applicant.fio,
                "test_name": test.name if test else "Неизвестный тест",
                "answered_questions": total_answered,
                "total_questions_all": total_questions_all,
                "correct_answers_percent": percentage_correct_answered,
                "correct_answers_percent_all": percentage_correct_all,
                "theme_results": theme_results,
                "applicant_answers": applicant_answers_list,  # добавляем ответы соискателя
                "id_applicant_test": applicant.id_applicant_test,
                "correct_answers": correct_answers,
                "time": time,
            }

            return result_summary

    @staticmethod
    def get_correct_answers_for_test(test_id):
        """Получает правильные ответы для теста по его ID"""
        with SessionLocal() as session:
            return session.query(Answer).join(Questions).filter(
                Questions.id_quest_test == test_id
            ).all()

    @staticmethod
    def delete_tests_and_answers(test_id):
        """Удаляет тест, все связанные с ним ответы, вопросы и соискателей без ответов."""
        with SessionLocal() as session:
            # Удаляем все ответы соискателей на вопросы данного теста
            session.query(ApplicantAnswer).join(Questions).filter(Questions.id_quest_test == test_id).delete(
                synchronize_session='fetch')

            # Удаляем все вопросы данного теста
            session.query(Questions).filter(Questions.id_quest_test == test_id).delete(synchronize_session='fetch')

            # Удаляем тест
            session.query(Tests).filter(Tests.id_test == test_id).delete(synchronize_session='fetch')

            # Удаляем соискателей
            session.query(Applicant).filter(Applicant.id_applicant_test == test_id).delete(synchronize_session='fetch')


            # Фиксируем изменения в базе данных
            session.commit()