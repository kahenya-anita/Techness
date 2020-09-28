from flask import jsonify
from app.models import User

@bp.route('/quotes/<int:id>', methods=['GET'])
def get_quote(id):
    return jsonify(User.query.get_or_404(id).to_dict())

@bp.route('/quotes', methods=['GET'])
def get_random():
    pass


