from flask import Blueprint, request, jsonify
from models import db, ChromeExtentionUuid, chrome_extention_uuid_schema, chrome_extention_uuids_schema
import uuid as uuid_module
import json
from datetime import datetime

uuid = Blueprint('uuid', __name__)


@uuid.route('/api/uuid', methods=['POST'])
def add_uuid():
    # UUID 자동 생성
    generated_uuid = str(uuid_module.uuid4())
    
    # 클라이언트 정보 가져오기 (요청에 포함된 경우)
    client_info = request.json.get('client_info', {})
    
    # 클라이언트 정보가 없으면 요청의 모든 정보를 수집
    if not client_info:
        # 요청 헤더 정보 수집
        headers = dict(request.headers)
        
        # 요청 환경 변수 중 일부 수집
        env_info = {
            "remote_addr": request.remote_addr,
            "remote_user": request.remote_user,
            "method": request.method,
            "scheme": request.scheme,
            "path": request.path,
            "full_path": request.full_path,
            "url": request.url,
            "base_url": request.base_url,
            "url_root": request.url_root,
            "is_secure": request.is_secure,
            "accept_languages": list(request.accept_languages.values()),
            "accept_charsets": list(request.accept_charsets.values()),
            "accept_encodings": list(request.accept_encodings.values()),
            "accept_mimetypes": list(request.accept_mimetypes.values())
        }
        
        # 요청 쿠키 정보 수집
        cookies = dict(request.cookies)
        
        # 요청 폼 데이터 수집 (있는 경우)
        form_data = dict(request.form) if request.form else {}
        
        # 요청 쿼리 파라미터 수집
        args = dict(request.args)
        
        # 요청 JSON 데이터 수집 (있는 경우)
        json_data = request.get_json(silent=True) or {}
        
        # 모든 정보를 하나의 딕셔너리로 통합
        client_info = {
            "headers": headers,
            "env_info": env_info,
            "cookies": cookies,
            "form_data": form_data,
            "query_params": args,
            "json_data": json_data,
            "timestamp": str(datetime.now())
        }
    
    # JSON 문자열로 변환 (필요한 경우)
    # if not isinstance(client_info, str):
    #     client_info = json.dumps(client_info)
    
    
    # 새 UUID 객체 생성
    new_ce_uuid = ChromeExtentionUuid(
        uuid=generated_uuid,
        client_info=client_info
    )
    
    # 데이터베이스에 저장
    db.session.add(new_ce_uuid)
    db.session.commit()
    
    # 응답 반환
    return chrome_extention_uuid_schema.jsonify(new_ce_uuid)

@uuid.route('/api/uuid/<uuid_string>', methods=['GET'])
def get_uuid(uuid_string):
    # UUID로 데이터베이스에서 조회
    ce_uuid = ChromeExtentionUuid.query.filter_by(uuid=uuid_string).first()
    
    if ce_uuid:
        return chrome_extention_uuid_schema.jsonify(ce_uuid)
    return jsonify({"message": "UUID를 찾을 수 없습니다"}), 404 