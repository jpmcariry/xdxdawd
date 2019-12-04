from flask import Flask, jsonify
from flask_restful import Api
from resources.cadastro import UserRegister, UserUpdate
from resources.match import Match
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json'])
UPLOAD_FOLDER = 'static//img//'
#template_dir = os.path.join(os.path.dirname(__file__), 'templates')

app = Flask(__name__)
app.config['DOWNLOAD_FOLDER'] = 'static//img//'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['SECRET_KEY'] = 'dawdwadwa'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:+pymysql//username:password@localhost/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DonTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True

api = Api(app)
jwt = JWTManager(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserUpdate,'/update')
api.add_resource(Match, '/match')



# @app.route('/login')
# fazer a autenticaçao = request autorizado
@app.before_first_request
def cria_banco():
    banco.create_all()


@jwt.token_in_blacklist_loader
def verify_blacklist(token):
    return token['jti'] in BLACKLIST

@jwt.revoked_token_loaderc
def token_de_acesso_invalidado():
    return jsonify({'message': 'You have been logged out'})
def cadastro():
    pass
if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(host='0.0.0.0', port=5000,debug=True)