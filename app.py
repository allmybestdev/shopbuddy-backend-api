from flask import Flask, request, g
import os
from flask_cors import CORS
import logging
import json
from datetime import datetime
import time
from dotenv import load_dotenv

# Flask 앱 초기화
app = Flask(__name__)


# .env 파일 로드
load_dotenv()

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('api_requests.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# CORS 설정 추가
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 데이터베이스 설정 (MySQL with UTF8MB4)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?charset=utf8mb4"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_recycle': 280,
    'pool_pre_ping': True,
    'connect_args': {
        'charset': 'utf8mb4',
        'collation': 'utf8mb4_general_ci'
    }
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB 초기화
from models import db, ma
db.init_app(app)
ma.init_app(app)

# Blueprint 등록
from routes.main_routes import main
from routes.product_routes import product
from routes.user_routes import users
from routes.uuid_routes import uuid

app.register_blueprint(main)
app.register_blueprint(product)
app.register_blueprint(users)
app.register_blueprint(uuid)



# 요청 시작 시 로깅
@app.before_request
def log_request_info():
    # 요청 시작 시간 저장
    g.start_time = time.time()
    
    # 요청 정보 로깅
    request_data = {
        'method': request.method,
        'url': request.url,
        'path': request.path,
        'headers': dict(request.headers),
        'args': dict(request.args),
        'form': dict(request.form),
        'remote_addr': request.remote_addr,
        'timestamp': datetime.now().isoformat()
    }
    
    # JSON 데이터가 있으면 추가
    if request.is_json:
        try:
            request_data['json'] = request.get_json()
        except Exception as e:
            request_data['json_error'] = str(e)
    
    # 로그 출력
    logger.info(f"API 요청: {json.dumps(request_data, ensure_ascii=False, default=str)}")

# 응답 완료 시 로깅
@app.after_request
def log_response_info(response):
    # 응답 시간 계산
    duration = time.time() - g.start_time
    
    # 응답 정보 로깅
    response_data = {
        'path': request.path,
        'status_code': response.status_code,
        'duration_ms': round(duration * 1000, 2),
        'content_length': response.content_length,
        'content_type': response.content_type
    }
    
    # 응답 본문 (선택적)
    if response.content_type == 'application/json':
        try:
            # 응답 본문 복사 (읽은 후 다시 설정)
            response_body = response.get_data()
            if response_body:
                response_data['body'] = json.loads(response_body)
                
            # 원래 응답 본문 복원
            response.set_data(response_body)
        except Exception as e:
            response_data['body_error'] = str(e)
    
    # 로그 출력
    logger.info(f"API 응답: {json.dumps(response_data, ensure_ascii=False, default=str)}")
    
    return response



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
