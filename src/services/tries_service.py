from ..utils.database import session_factory
from ..models.tries import Tries

def insert_tries_dict(tries_dict):
    session = session_factory()

    tries = Tries(**tries_dict)
    session.add(tries)

    session.flush()
    tries_id = tries.id
    
    session.commit()
    session.close()

    return tries_id