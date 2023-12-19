from flask import request, jsonify
import secrets
from storage import api_key

key_cache = {}


def init_key_cache():
    key_list = api_key.get_api_key()
    for key in key_list:
        key_cache[key] = 1


def auth():
    key = request.json["parameters"].get("api_key", "").strip()
    if not key:
        return jsonify({"msg": "no api Key"}), 401

    if key_cache.get(key):
        return jsonify({"msg": "Certification Success"}), 200
    else:
        return jsonify({"msg": "no matched Key"}), 401


def generate_api_key():
    key = secrets.token_hex(32)
    api_key.save_api_key(key)
    key_cache[key] = 1
    return jsonify({"api_key": key})
