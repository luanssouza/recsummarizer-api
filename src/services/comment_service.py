from ..utils.database import session_factory
from ..models.comment import Comment

def insert_comment_dict(comment_dict):
    session = session_factory()

    comment = Comment(**comment_dict)
    session.add(comment)

    session.flush()
    comment_id = comment.id
    
    session.commit()
    session.close()

    return comment_id