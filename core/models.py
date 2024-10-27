from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship

from .config import Base

class Themas(Base):
    __tablename__ = 'themas'

    id_themas = Column(Integer, primary_key=True)
    name = Column(String)

    questions = relationship('Questions', back_populates='thema')


class Tests(Base):
    __tablename__ = 'tests'

    id_test = Column(Integer, primary_key=True)
    name = Column(String)

    questions = relationship('Questions', back_populates='test')
    applicants = relationship('Applicant', back_populates='test')


class Questions(Base):
    __tablename__ = 'questions'

    id_quest = Column(Integer, primary_key=True)
    name = Column(String)

    id_quest_test = Column(Integer, ForeignKey('tests.id_test'))
    id_quest_themas = Column(Integer, ForeignKey('themas.id_themas'))

    test = relationship('Tests', back_populates='questions')
    thema = relationship('Themas', back_populates='questions')
    answers = relationship('Answer', back_populates='question')
    applicant_answers = relationship('ApplicantAnswer', back_populates='question')


class Answer(Base):
    __tablename__ = 'answer'

    id_answer = Column(Integer, primary_key=True)
    name = Column(String)
    is_correct = Column(Boolean)

    id_answer_quest = Column(Integer, ForeignKey('questions.id_quest'))

    question = relationship('Questions', back_populates='answers')



class Applicant(Base):
    __tablename__ = 'applicant'

    id_applicant = Column(Integer, primary_key=True)
    fio = Column(Text)

    #  столбец для даты
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    id_applicant_test = Column(Integer, ForeignKey('tests.id_test'))

    test = relationship('Tests', back_populates='applicants')
    answers = relationship('ApplicantAnswer', back_populates='applicant')


class ApplicantAnswer(Base):
    __tablename__ = 'applicantanswer'

    id_applicantAnswer = Column(Integer, primary_key=True)
    is_correct = Column(Boolean)
    time_spent = Column(Integer)

    id_applicantanswer_applicant = Column(Integer, ForeignKey('applicant.id_applicant'))
    id_applicantanswer_questions = Column(Integer, ForeignKey('questions.id_quest'))

    applicant = relationship('Applicant', back_populates='answers')
    question = relationship('Questions', back_populates='applicant_answers')