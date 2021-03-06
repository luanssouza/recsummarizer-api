from sqlalchemy import Column, Integer, SmallInteger, ForeignKey

from ..utils.database import Base

class Explanation(Base):
    __tablename__ = "explanation"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    liked = Column(SmallInteger, nullable=False)
    understood = Column(SmallInteger, nullable=False)
    interest = Column(SmallInteger, nullable=False)
    useful = Column(SmallInteger, nullable=False)
    preferences = Column(SmallInteger, nullable=False)
    levelFit = Column(SmallInteger, nullable=False)
    
    def __init__(self, user_id, movie_id, liked, understood, interest, useful, preferences, levelFit):
        self.user_id = user_id
        self.movie_id = movie_id
        self.liked = liked
        self.understood = understood
        self.interest = interest
        self.useful = useful
        self.preferences = preferences
        self.levelFit = levelFit