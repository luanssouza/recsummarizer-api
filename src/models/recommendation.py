from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.sql.sqltypes import JSON

from ..utils.database import Base

class Recommendation(Base):
    __tablename__ = "recommendations"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    movie_id = Column(Integer, nullable=False)
    rates = Column(JSON)

    def __init__(self, user_id, movie_id, rates):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rates = rates