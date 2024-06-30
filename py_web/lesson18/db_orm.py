from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///base.db')
Base = declarative_base(bind=engine)
Session = sessionmaker()


class Word(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True)
    word = Column(String(50), index=True)
    count = Column(Float, default=0)
    up = Column(Float, default=0)
    down = Column(Float, default=0)


class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), unique=True)


class WordSkill(Base):
    __tablename__ = 'wordskills'
    id = Column(Integer, primary_key=True)
    id_word = Column(Integer, ForeignKey('words.id'))
    id_skill = Column(Integer, ForeignKey('skills.id'))
    count = Column(Float, default=0)
    percent = Column(Float, default=0)

    def __str__(self):
        return f'{self.id}) {self.id_word} | {self.id_skill} | {self.count} | {self.percent} |'


class Area(Base):
    __tablename__ = 'area'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, index=True)
    ind = Column(Integer)

    def __str__(self):
        return f'{self.id}) {self.name} | {self.ind} |'

    def __repr__(self):
        return f'{self.id} - {self.name} - {self.ind}'


Base.metadata.create_all()
