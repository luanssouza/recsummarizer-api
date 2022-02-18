from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger
from sqlalchemy.sql import func

from ..utils.database import Base

class Tries(Base):
    __tablename__ = "tries"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    liked = Column(SmallInteger, nullable=False)
    created = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, user_id, movie_id, liked):
        self.user_id = user_id
        self.movie_id = movie_id
        self.liked = liked