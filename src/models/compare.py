from sqlalchemy import Column, DateTime, Integer, SmallInteger, ForeignKey, String, func

from ..utils.database import Base

class Compare(Base):
    __tablename__ = "compare"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    understood = Column(SmallInteger, nullable=False)
    commentUnderstood = Column(String(255))
    useful = Column(SmallInteger, nullable=False)
    commentUseful = Column(String(255))
    interest = Column(SmallInteger, nullable=False)
    commentInterest = Column(String(255))
    preferences = Column(SmallInteger, nullable=False)
    commentPreferences = Column(String(255))
    created = Column(DateTime(timezone=True), default=func.now())
    
    def __init__(
        self, user_id, movie_id, 
        understood, commentUnderstood, 
        useful, commentUseful, 
        interest, commentInterest, 
        preferences, commentPreferences
        ):
        self.user_id = user_id
        self.movie_id = movie_id
        self.understood = understood
        self.commentUnderstood = commentUnderstood
        self.useful = useful
        self.commentUseful = commentUseful
        self.interest = interest
        self.commentInterest = commentInterest
        self.preferences = preferences
        self.commentPreferences = commentPreferences