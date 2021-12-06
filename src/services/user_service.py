from ..utils.database import session_factory
from ..models.user import User

def insert_user_dict(user_dict):
    session = session_factory()
    user = User(**user_dict)
    session.add(user)
    session.commit()
    session.close()