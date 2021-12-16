from ..utils.database import session_factory
from ..models.compare import Compare

def insert_compare_dict(compare_dict):
    session = session_factory()

    compare = Compare(**compare_dict)
    session.add(compare)

    session.flush()
    compare_id = compare.id
    
    session.commit()
    session.close()

    return compare_id