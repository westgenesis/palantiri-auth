from flask import request, jsonify
import secrets
from storage import api_key


def auth():
    key = request.json["parameters"].get("api_key", "").strip()
    if not key:
        return jsonify({"msg": "no api Key"}), 401

    key_list = api_key.get_api_key()
    print(key_list)
    if key in key_list:
        return jsonify({"msg": "Certification Success"}), 200
    else:
        return jsonify({"msg": "no matched Key"}), 401


def generate_api_key():
    key = secrets.token_hex(32)
    api_key.save_api_key(key)
    return jsonify({"api_key": key})
