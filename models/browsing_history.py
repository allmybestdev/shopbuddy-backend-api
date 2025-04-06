from models import db
from datetime import datetime, UTC

class BrowsingHistory(db.Model):
    __tablename__ = 'browsing_history'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    site_nm = db.Column(db.String(50), nullable=False)
    site_url = db.Column(db.String(1000), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now(UTC))
    chrome_extention_uuid = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    
    # 관계 설정
    user = db.relationship('Users', backref='browsing_histories')
    
    def __init__(self, site_nm, site_url, chrome_extention_uuid, user_id):
        self.site_nm = site_nm
        self.site_url = site_url
        self.chrome_extention_uuid = chrome_extention_uuid
        self.user_id = user_id
        self.createdAt = datetime.now(UTC) 