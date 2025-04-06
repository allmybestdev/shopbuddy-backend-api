from models import ma
from models.users import Users

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_nm', 'createdAt', 'updatedAt', 'chrome_extention_uuid_id')
        model = Users

# 단일 사용자 스키마
users_schema = UsersSchema()
