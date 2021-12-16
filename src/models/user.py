from sqlalchemy import Column, Integer, Boolean, SmallInteger

from ..utils.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, )
    accept = Column(Boolean, nullable=False)
    age = Column(SmallInteger)
    gender = Column(SmallInteger)
    education = Column(SmallInteger)
    recommender = Column(SmallInteger)

    def __init__(self, accept, age, gender, education, recommender):
        self.accept = accept
        self.age = age
        self.gender = gender
        self.education = education
        self.recommender = recommender