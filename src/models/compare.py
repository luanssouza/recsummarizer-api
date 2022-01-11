from sqlalchemy import Column, Integer, SmallInteger, ForeignKey

from ..utils.database import Base

class Compare(Base):
    __tablename__ = "compare"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    understood = Column(SmallInteger, nullable=False)
    useful = Column(SmallInteger, nullable=False)
    interest = Column(SmallInteger, nullable=False)
    preferences = Column(SmallInteger, nullable=False)
    
    def __init__(self, user_id, movie_id, understood, useful, interest, preferences):
        self.user_id = user_id
        self.movie_id = movie_id
        self.understood = understood
        self.useful = useful
        self.interest = interest
        self.preferences = preferences