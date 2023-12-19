from flask_jwt_extended import create_access_token

import storage.user
from flask import request

from common.md5_operate import get_md5

# def get_all_users():
#     """获取所有用户信息"""
#     data = storage.user.user_list()
#     print("获取所有用户信息 == >> {}".format(data))
#     return jsonify({"code": 0, "data": data, "msg": "查询成功"})
#
#
# def get_user():
#     """获取某个用户信息"""
#     username = request.json.get("username", "").strip()
#     data = storage.user.get_user(username)
#     print("获取 {} 用户信息 == >> {}".format(username, data))
#     if data:
#         return jsonify({"code": 0, "data": data, "msg": "查询成功"})
#     return USER_GET_FAIL
#
#
# def user_register():
#     """注册用户"""
#     username = request.json.get("username", "").strip()
#     password = request.json.get("password", "").strip()
#     if username and password:
#         user = storage.user.get_user(username)
#         if user:
#             return USER_ALREADY_EXIST
#         password = get_md5(username, password)
#         storage.user.create_user(username, password)
#         return jsonify({"code": 0, "msg": "恭喜，注册成功！"})
#     else:
#         return USER_PARAM_NULL
#
#
# def user_login():
#     """登录用户"""
#     username = request.values.get("username", "").strip()
#     password = request.values.get("password", "").strip()
#     if username and password:
#         md5_password = get_md5(username, password)
#         user = storage.user.get_user(username, md5_password)
#         if user:
#             access_token = create_access_token(identity=username)
#             return jsonify({"code": 0, "token": access_token, "msg": "恭喜，登录成功！"}),200
#         return USER_LOGIN_FAIL, 401
#     else:
#         return USER_PARAM_NULL, 401
#
#
# def user_update():  # id为准备修改的用户ID
#     """修改用户信息"""
#     username = request.json.get("username", "").strip()
#     password = request.json.get("password", "").strip()
#     if username and password:
#         data = storage.user.get_user(username)
#         if not data:
#             return USER_NOT_EXIST
#         password = get_md5(username, password)
#         storage.user.update_user(username, password)
#         return jsonify({"code": 0, "msg": "修改用户密码成功！"})
#     else:
#         return USER_PARAM_NULL
#
#
# def user_delete():
#     username = request.json.get("username", "").strip()
#     if username:
#         storage.user.delete_user(username)
#         return jsonify({"code": 0, "msg": "删除用户成功！"})
#     else:
#         return USER_PARAM_NULL


def auth():

    return


def generate():

    return
