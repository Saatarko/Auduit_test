from PySide6.QtWidgets import QMessageBox
from sqlalchemy.orm import joinedload

from .config import Base, engine, SessionLocal
from .models import Tests, Questions, Themas, Answer, Applicant


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