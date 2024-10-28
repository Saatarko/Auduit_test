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
    def get_question_for_applicant_by_index(test_id, question_index):
        with SessionLocal() as session:
            # Загружаем вопрос вместе с ответами и темой с помощью joinedload
            questions = (
                session.query(Questions)
                .filter_by(id_quest_test=test_id)
                .options(
                    joinedload(Questions.applicant_answers),  # Подгружаем ответы соискателя
                    joinedload(Questions.answers), # Подгружаем варианты ответа
                    joinedload(Questions.thema)  # Подгружаем тему вопроса
                )
                .order_by(Questions.id_quest)
                .all()
            )
            if 0 <= question_index < len(questions):
                return questions[question_index]
            return None

    @staticmethod
    def add_applicant(applicant_name: str):
        # Используем `with` для автоматического закрытия сессии после использования
        with SessionLocal() as session:
            new_applicant = Applicant(fio=applicant_name)
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

            if answers:
                # Если ответы уже существуют, обновляем только время
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

            if answers:
                # Если ответы уже существуют, обновляем только время
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

            # Получаем ответы соискателя
            applicant_answers = session.query(ApplicantAnswer).filter(
                ApplicantAnswer.id_applicantanswer_applicant == applicant_id
            ).all()

            # Получаем правильные ответы для теста
            correct_answers = session.query(Answer).join(Questions).filter(
                Questions.id_quest_test == applicant.id_applicant_test
            ).all()

            # Подсчитываем количество отвеченных вопросов и правильных ответов
            total_questions = len(correct_answers)
            answered_questions = len(applicant_answers)
            correct_answers_count = sum(1 for answer in applicant_answers if answer.is_correct)

            # Подсчитываем процент правильных ответов
            correct_answers_percent = (correct_answers_count / total_questions * 100) if total_questions > 0 else 0

            # Группируем данные по темам
            theme_stats = {}
            for answer in applicant_answers:
                question = session.query(Questions).filter(
                    Questions.id_quest == answer.id_applicantanswer_questions).one_or_none()
                if question:
                    theme_id = question.id_quest_themas
                    if theme_id not in theme_stats:
                        theme_stats[theme_id] = {"correct_count": 0, "total_count": 0}

                    # Увеличиваем общее количество вопросов по теме
                    theme_stats[theme_id]["total_count"] += 1

                    # Проверяем, правильный ли ответ
                    if answer.is_correct:
                        theme_stats[theme_id]["correct_count"] += 1

            # Подсчитываем процент правильных ответов по темам
            theme_results = []
            for theme_id, stats in theme_stats.items():
                theme_name = session.query(Themas).filter(Themas.id_themas == theme_id).one_or_none()
                if theme_name:
                    correct_percent = (stats["correct_count"] / stats["total_count"] * 100) if stats[
                                                                                                   "total_count"] > 0 else 0
                    theme_results.append({"theme_name": theme_name.name, "correct_percent": correct_percent})

            # Формируем итоговый результат
            result_summary = {
                "fio": applicant.fio,
                "test_name": test.name if test else "Неизвестный тест",
                "answered_questions": answered_questions,
                "total_questions": total_questions,
                "correct_answers_percent": correct_answers_percent,
                "themes": theme_results,
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