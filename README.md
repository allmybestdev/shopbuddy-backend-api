# ShopBuddy Backend API

## 소개
ShopBuddy 크롬 확장 프로그램을 위한 백엔드 API 서버입니다.

## 기술 스택
- Python 3.12
- Flask
- SQLAlchemy
- MySQL
- Poetry (의존성 관리)

## 설치 방법
1. 저장소 클론
```bash
git clone https://github.com/allmybestdev/shopbuddy-backend-api.git
cd shopbuddy-backend-api
```

2. Poetry를 사용하여 의존성 설치
```bash
poetry install
```

3. 환경 변수 설정
`.env` 파일을 생성하고 다음 변수들을 설정하세요:
```
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
```

## 실행 방법
```bash
poetry run python app.py
```

서버는 기본적으로 `http://127.0.0.1:8080`에서 실행됩니다.