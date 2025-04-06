from flask import Blueprint, request, jsonify
from models import db, Product, product_schema, products_schema
from models.browsing_history import BrowsingHistory
from models.schemas.browsing_history_schema import browsing_history_schema

product = Blueprint('product', __name__)

@product.route('/api/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

@product.route('/api/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    if product:
        return product_schema.jsonify(product)
    return jsonify({"message": "상품을 찾을 수 없습니다"}), 404

@product.route('/api/products', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    stock = request.json['stock']
    
    new_product = Product(name, description, price, stock)
    
    db.session.add(new_product)
    db.session.commit()
    
    return product_schema.jsonify(new_product)


@product.route('/api/browsing-history', methods=['POST'])
def add_browsing_history():
    try:
        site_url = request.json['site_url']
        user_id = request.json.get('user_id') or None
        chrome_extention_uuid = request.json.get('chrome_extention_uuid') or None
        site_nm = 'test'

                
        # 새로운 기록 생성
        new_view = BrowsingHistory(
            site_url=site_url,
            user_id=user_id,
            chrome_extention_uuid=chrome_extention_uuid,
            site_nm=site_nm
        )
        
        db.session.add(new_view)
        db.session.commit()
        
        return browsing_history_schema.jsonify(new_view), 201
        
    except KeyError:
        return jsonify({'error': '필수 필드가 누락되었습니다'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500 
