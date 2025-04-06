from models import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_nm = db.Column(db.String(1000), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    chrome_extention_uuid_id = db.Column(db.Integer, db.ForeignKey('chrome_extention_uuid.id'), nullable=True)
    
    # 관계 설정
    chrome_extention = db.relationship('ChromeExtentionUuid', backref='users', lazy=True)
    
    def __init__(self, user_nm, chrome_extention_uuid_id=None):
        self.user_nm = user_nm
        self.chrome_extention_uuid_id = chrome_extention_uuid_id
        self.createdAt = datetime.now()
        self.updatedAt = datetime.now() 