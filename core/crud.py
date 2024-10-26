from PySide6.QtWidgets import QMessageBox

from .config import Base, engine, SessionLocal
from .models import Tests, Questions


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
    def get_tests_from_id(test_id):
        """Функция получения теста по id"""
        with SessionLocal() as session:
            result = session.get(Tests, test_id)
            return result

    @staticmethod
    def get_question_by_test_id_and_number(test_id, question_number):
        with SessionLocal() as session:
            return session.query(Questions).filter_by(test_id=test_id, question_number=question_number).first()

    @staticmethod
    def save_question(test_id, question_number, text, answer_a, answer_b, answer_c, answer_d,
                      is_correct_a, is_correct_b, is_correct_c, is_correct_d, theme):
        with SessionLocal() as session:
            question = session.query(Questions).filter_by(test_id=test_id, question_number=question_number).first()

            if not question:
                # Если вопрос не найден, создаем новый
                question = Questions(
                    test_id=test_id,
                    question_number=question_number,
                    text=text,
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
                session.add(question)
            else:
                # Обновляем существующий вопрос
                question.text = text
                question.answer_a = answer_a
                question.answer_b = answer_b
                question.answer_c = answer_c
                question.answer_d = answer_d
                question.is_correct_a = is_correct_a
                question.is_correct_b = is_correct_b
                question.is_correct_c = is_correct_c
                question.is_correct_d = is_correct_d
                question.theme = theme

            session.commit()