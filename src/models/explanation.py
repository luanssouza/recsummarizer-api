from sqlalchemy import Column, DateTime, Integer, SmallInteger, ForeignKey, String, func

from ..utils.database import Base

class Explanation(Base):
    __tablename__ = "explanation"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    liked = Column(SmallInteger, nullable=False)
    commentLiked = Column(String(255))
    understood = Column(SmallInteger, nullable=False)
    commentUnderstood = Column(String(255))
    interest = Column(SmallInteger, nullable=False)
    commentInterest = Column(String(255))
    useful = Column(SmallInteger, nullable=False)
    commentUseful = Column(String(255))
    preferences = Column(SmallInteger, nullable=False)
    commentPreferences = Column(String(255))
    levelFit = Column(SmallInteger, nullable=False)
    commentLevelFit = Column(String(255))
    levelUseful = Column(SmallInteger, nullable=False)
    commentLevelUseful = Column(String(255))
    created = Column(DateTime(timezone=True), default=func.now())
    
    def __init__(
        self, user_id, movie_id, 
        liked, commentLiked, 
        understood, commentUnderstood, 
        interest, commentInterest, 
        useful, commentUseful, 
        preferences, commentPreferences, 
        levelFit, commentLevelFit, 
        levelUseful, commentLevelUseful
        ):
        self.user_id = user_id
        self.movie_id = movie_id
        self.liked = liked
        self.commentLiked = commentLiked
        self.understood = understood
        self.commentUnderstood = commentUnderstood
        self.interest = interest
        self.commentInterest = commentInterest
        self.useful = useful
        self.commentUseful = commentUseful
        self.preferences = preferences
        self.commentPreferences = commentPreferences
        self.levelFit = levelFit
        self.commentLevelFit = commentLevelFit
        self.levelUseful = levelUseful
        self.commentLevelUseful = commentLevelUseful