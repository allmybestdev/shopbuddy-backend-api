from models import db
from datetime import datetime

class ChromeExtentionUuid(db.Model):
    __tablename__ = 'chrome_extention_uuid'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(1000), nullable=False)
    client_info = db.Column(db.JSON, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    # 관계 설정 - 외래 키가 변경되었으므로 관계도 제거 또는 수정
    # product_view_histories = db.relationship('ProductViewHistory', backref='chrome_extention', lazy=True)
    
    def __init__(self, uuid, client_info):
        self.uuid = uuid
        self.client_info = client_info
        self.createdAt = datetime.now() 