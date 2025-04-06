from models import ma
from models.product import Product

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'stock')
        model = Product

# 단일 상품 스키마 인스턴스
product_schema = ProductSchema()
# 여러 상품 스키마 인스턴스
products_schema = ProductSchema(many=True) 