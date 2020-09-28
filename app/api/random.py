from app.api import bp

@bp.route('/quotes/<int:id>', methods=['GET'])
def get_quote(id):
    pass

@bp.route('/quotes', methods=['GET'])
def get_random():
    pass


