from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# 모델 임포트
from models.product import Product
from models.chrome_extention_uuid import ChromeExtentionUuid
from models.users import Users
from models.browsing_history import BrowsingHistory

# 스키마 임포트
from models.schemas.product_schema import ProductSchema, product_schema, products_schema
from models.schemas.chrome_extention_uuid_schema import ChromeExtentionUuidSchema, chrome_extention_uuid_schema, chrome_extention_uuids_schema
from models.schemas.users_schema import UsersSchema, users_schema, users_schema
from models.schemas.browsing_history_schema import BrowsingHistorySchema, browsing_history_schema, browsing_histories_schema 