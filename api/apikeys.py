from flask import request, jsonify

from common.sha265_operate import decrypt
from common.sha265_operate import encrypt
import secrets
from storage import api_key_operation


# password = "412312"


def auth():
    try:
        token = request.values.get("key", "").strip()
    except Exception:
        return jsonify({"msg": "no API Key been received"}), 401
    # key = decrypt(sha256_token, password)
    if api_key_operation.compare_api_key(token):
        return jsonify({"msg": ""}), 200
    else:
        return jsonify({"msg": "no matched Key"}), 401


def generate_api_key():
    usr = request.values.get("usr", "").strip()
    try:
        token = secrets.token_hex(16)
    except Exception:
        return jsonify({"msg": "failed to generate the API Key"}), 401
    try:
        api_key_operation.save_api_key(usr, token)
    except Exception:
        return jsonify({"msg": "failed to save the key"}), 401

    # try:
    #     sha256_token = encrypt(token.encode(), password)
    # except Exception:
    #     return jsonify({"failed to encrypt"}), 401

    return token
