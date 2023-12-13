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


if __name__ == '__main__':
    route.init()
    # db.create_all()
    app.run(host="0.0.0.0", port=SERVER_PORT, debug=True)
