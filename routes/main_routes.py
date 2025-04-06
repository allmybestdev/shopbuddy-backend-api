from flask import Blueprint, render_template, jsonify
from models import db

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return "Hello World";
    # return render_template("chatBot.html")

# @main.route('/setup-db')
# def setup_db():
#     db.create_all()
#     return jsonify({"message": "데이터베이스가 생성되었습니다"}) 