from app import app
import api.user


def init():
    # app.add_url_rule("/get", methods=["POST"], view_func=api.user.get_user)
    # app.add_url_rule("/list", methods=["POST"], view_func=api.user.get_all_users)
    # app.add_url_rule("/register", methods=["OPTIONS"], view_func=api.user.user_register)
    # app.add_url_rule("/login", methods=["POST"], view_func=api.user.user_login)
    # app.add_url_rule("/update", methods=["POST"], view_func=api.user.user_update)
    # app.add_url_rule("/delete", methods=["POST"], view_func=api.user.user_delete)

    # auth
    app.add_url_rule("/generate", methods=["POST"], view_func=api.user.generate)
    app.add_url_rule("/auth", methods=["POST"], view_func=api.user.auth)
    return
