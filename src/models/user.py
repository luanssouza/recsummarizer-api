from sqlalchemy import Column, DateTime, Integer, Boolean, SmallInteger
from sqlalchemy.sql import func

from ..utils.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, )
    accept = Column(Boolean, nullable=False)
    age = Column(SmallInteger)
    gender = Column(SmallInteger)
    education = Column(SmallInteger)
    recommender = Column(SmallInteger)
    created = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, accept, age, gender, education, recommender):
        self.accept = accept
        self.age = age
        self.gender = gender
        self.education = education
        self.recommender = recommender