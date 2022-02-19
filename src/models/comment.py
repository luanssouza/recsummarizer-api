from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from ..utils.database import Base

class Comment(Base):
    __tablename__ = "comment"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    comment = Column(String(255), nullable=False)
    created = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, user_id, movie_id, comment):
        self.user_id = user_id
        self.movie_id = movie_id
        self.comment = comment