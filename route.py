from app import app
from flask import Flask, request
import api.apikeys


def init():
    app.add_url_rule("/generate", methods=["POST"], view_func=api.apikeys.generate_api_key)
    app.add_url_rule("/auth", methods=["POST"], view_func=api.apikeys.auth)
    return
