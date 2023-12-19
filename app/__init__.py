from flask import Flask


app = Flask("palantiri-auth")
app.config["JSON_AS_ASCII"] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = STORAGE_DSN
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ECHO'] = True
