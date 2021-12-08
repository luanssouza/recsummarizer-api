from ..utils.database import session_factory
from ..models.recommendation import Recommendation

def insert_recommendation_dict(recommendation_dict):
    session = session_factory()

    recommendation = Recommendation(**recommendation_dict)
    session.add(recommendation)

    session.flush()
    recommendation_id = recommendation.id
    
    session.commit()
    session.close()

    return recommendation_id