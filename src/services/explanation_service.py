from ..utils.database import session_factory
from ..models.explanation import Explanation

def insert_explanation_dict(explanation_dict):
    session = session_factory()

    explanation = Explanation(**explanation_dict)
    session.add(explanation)

    session.flush()
    explanation_id = explanation.id
    
    session.commit()
    session.close()

    return explanation_id