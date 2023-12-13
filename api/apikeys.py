from flask import request, jsonify

from common.sha265_operate import decrypt
from common.sha265_operate import encrypt
import secrets

password = "412312"


def auth():
    sha256_token = request.values.get("sha", "").strip()
    key = decrypt(sha256_token, password)
    with open("api_key.txt", 'r', encoding="utf-8") as f:
        for line in f:
            if line == key:
                return jsonify({""}), 200
            else:
                return jsonify({""}), 401


def generate_api_key():
    token = secrets.token_hex(16)
    print(token)
    file = open("api_key.txt", 'w')
    file.write(token)
    file.close()
    sha256_token = encrypt(token.encode(), password)

    return sha256_token
