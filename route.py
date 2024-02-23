from app import app
import api.apikeys


def init():
    app.add_url_rule("/generate", methods=["POST"], view_func=api.apikeys.generate_api_key)
    app.add_url_rule("/auth", methods=["POST"], view_func=api.apikeys.auth)
    app.add_url_rule("/auth_bs", methods=["POST"], view_func=api.apikeys.auth_bs)
    return
