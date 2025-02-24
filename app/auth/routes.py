from app.auth import blueprint

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    pass