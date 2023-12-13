from model.user import User
from app import db


def get_user(username, password=""):
    if not password:
        return User.query.get(username)
    return User.query.get(username, password)


def user_list():
    return User.query.all()


def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return


def delete_user(username):
    user = User.query.get(username)
    if user:
        db.session.delete(user)
        db.session.commit()
    return


def update_user(username, password):
    user = User.query.get(username)
    if user:
        user.password = password
        db.session.commit()
    return
