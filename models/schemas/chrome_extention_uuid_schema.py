from models import ma
from models.chrome_extention_uuid import ChromeExtentionUuid

class ChromeExtentionUuidSchema(ma.Schema):
    class Meta:
        fields = ('id', 'uuid', 'client_info', 'createdAt')
        model = ChromeExtentionUuid

# 단일 인스턴스 스키마
chrome_extention_uuid_schema = ChromeExtentionUuidSchema()
# 여러 인스턴스 스키마
chrome_extention_uuids_schema = ChromeExtentionUuidSchema(many=True) 