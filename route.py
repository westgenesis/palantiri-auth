from app import app
from flask import Flask, request
import api.apikeys


def init():
    # app.add_url_rule("/get", methods=["POST"], view_func=api.user.get_user)
    # app.add_url_rule("/list", methods=["POST"], view_func=api.user.get_all_users)
    # app.add_url_rule("/register", methods=["OPTIONS"], view_func=api.user.user_register)
    # app.add_url_rule("/login", methods=["POST"], view_func=api.user.user_login)
    # app.add_url_rule("/update", methods=["POST"], view_func=api.user.user_update)
    # app.add_url_rule("/delete", methods=["POST"], view_func=api.user.user_delete)
    # app = Flask(__name__)
    # auth

    # @app.route('/generate', methods=['POST'])
    # def generate():
    #     api.apikeys.generate_api_key()
    #
    # @app.route('/auth', methods=['POST'])
    # def auth():
    #     data = request.form.get("sha")
    #     api.apikeys.auth(data)
    app.add_url_rule("/generate", methods=["POST"], view_func=api.apikeys.generate_api_key)
    app.add_url_rule("/auth", methods=["POST"], view_func=api.apikeys.auth)
    return
