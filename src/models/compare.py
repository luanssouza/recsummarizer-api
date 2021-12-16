from sqlalchemy import Column, Integer, SmallInteger, ForeignKey

from ..utils.database import Base

class Compare(Base):
    __tablename__ = "compare"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    understood = Column(SmallInteger, nullable=False)
    convincing = Column(SmallInteger, nullable=False)
    discover = Column(SmallInteger, nullable=False)
    trust = Column(SmallInteger, nullable=False)
    
    def __init__(self, user_id, movie_id, understood, convincing, discover, trust):
        self.user_id = user_id
        self.movie_id = movie_id
        self.understood = understood
        self.convincing = convincing
        self.discover = discover
        self.trust = trust