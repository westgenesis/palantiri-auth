# from app import db
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     email = db.Column(db.String(64), unique=True)
#     password = db.Column(db.String(64))
#
#     def __repr__(self):
#         return 'User:%s' % self.username
