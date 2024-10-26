from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
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


class Answer(Base):
    __tablename__ = 'answer'

    id_answer = Column(Integer, primary_key=True)
    name = Column(String)
    is_correct = Column(Boolean)

    id_answer_quest = Column(Integer, ForeignKey('questions.id_quest'))

    question = relationship('Questions', back_populates='answers')
    applicant_answers = relationship('ApplicantAnswer', back_populates='answer')


class Applicant(Base):
    __tablename__ = 'applicant'

    id_applicant = Column(Integer, primary_key=True)
    fio = Column(Text)

    id_applicant_test = Column(Integer, ForeignKey('tests.id_test'))

    test = relationship('Tests', back_populates='applicants')
    answers = relationship('ApplicantAnswer', back_populates='applicant')


class ApplicantAnswer(Base):
    __tablename__ = 'applicantanswer'

    id_applicantAnswer = Column(Integer, primary_key=True)
    is_correct = Column(Boolean)
    time_spent = Column(Integer)

    id_applicantanswer_applicant = Column(Integer, ForeignKey('applicant.id_applicant'))
    id_applicantanswer_answer = Column(Integer, ForeignKey('answer.id_answer'))

    applicant = relationship('Applicant', back_populates='answers')
    answer = relationship('Answer', back_populates='applicant_answers')