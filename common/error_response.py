from app import app
from flask import jsonify


with app.app_context():
    USER_PARAM_NULL = jsonify({"code": 1000, "msg": "缺少参数"})
    USER_NOT_EXIST = jsonify({"code": 1001, "msg": "用户不存在"})
    USER_LOGIN_FAIL = jsonify({"code": 1002, "msg": "登录失败"})
    USER_REGISTER_FAIL = jsonify({"code": 1003, "msg": "注册用户失败"})
    USER_GET_FAIL = jsonify({"code": 1004, "msg": "查询用户失败"})
    USER_UPDATE_FAIL = jsonify({"code": 1005, "msg": "修改用户失败"})
    USER_DELETE_FAIL = jsonify({"code": 1006, "msg": "删除用户失败"})
    USER_ALREADY_EXIST = jsonify({"code": 1007, "msg": "用户已存在"})
