from flask import request

from common.sha265_operate import decrypt
from common.sha265_operate import encrypt
import secrets

password = "412312"
def auth(sha256_token):
    print("#########################################")
    print(sha256_token)
    print("#########################################")
    key = decrypt(sha256_token, password)
    # print(key)
    with open("api_key.txt", 'r', encoding="utf-8") as f:
        for line in f:
            if line == key:
                return 200
            else:
                return 500


def generate_api_key():
    token = secrets.token_hex(16)
    print(token)
    file = open("api_key.txt", 'w')
    file.write(token)
    file.close()
    sha256_token = encrypt(token.encode(), password)

    return sha256_token
