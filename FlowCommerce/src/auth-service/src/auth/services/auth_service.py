#from auth.models.users import User
from ..models.users import User


def create_user(username, password):
    if User.query.filter_by(username=username).first():
        return False
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return True

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return True
    return False