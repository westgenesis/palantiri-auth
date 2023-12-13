import os
import sys
import route
import model
from app import app, db
from config.setting import SERVER_PORT

# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将项目根路径临时加入环境变量，程序退出后失效
sys.path.insert(0, BASE_PATH)

# app = Flask(__name__)
# auth

# @app.route('/generate', methods=['POST'])
# def generate():
#     api.apikeys.generate_api_key()
#
# @app.route('/auth', methods=['POST'])
# def auth():
#     data = request.get_data()
#     api.apikeys.auth(data)

if __name__ == '__main__':
    route.init()
    # db.create_all()
    app.run(host="localhost", port=SERVER_PORT, debug=True)
