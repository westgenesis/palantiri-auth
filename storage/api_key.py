from flask import request, jsonify
import os.path
import json

api_key_dir = "/etc/palantiri-auth"
api_key_file = "/etc/palantiri-auth/api_key"


def save_api_key(key):
    if not os.path.exists(api_key_dir):
        os.makedirs(api_key_dir)
    with open(api_key_file, 'a') as f:
        f.write(key + "\n")
    return


def get_api_key():
    key_list = []
    with open(api_key_file, 'r') as f:
        for line in f:
            key_list.append(line.strip())
    return key_list
