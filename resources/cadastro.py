from models.conta import ContaModel
from flask_restful import Resource,reqparse
atributos = reqparse.RequestParser()
atributos.add_argument('user_ip', type=str, required=True, help="o campo 'user_ip' nao deve estar vazio")
atributos.add_argument('user_resoluction', type=str, required=True, help="o campo 'user_resoluction' nao deve estar vazio")

class UserRegister(Resource):

    def get(self):
        pass
    def post(self):
        global atributos;
        print("aqui")
        dados = atributos.parse_args()
        print(dados['user_ip'])
        if ContaModel.seach(dados['user_ip']):
            return {'message': 'Conta already exists'}, 409
        else:
            print("dados: ", dados['user_ip'], dados['user_resoluction'])
            user = ContaModel(dados['user_ip'], dados['user_resoluction'], 1)
            try:
                user.save_user()
                return {'message': 'Conta {} created'.format(dados['user_ip'])}, 201
            except:
                print("error")
                return {'message': 'error ao salvar'}, 500

class UserUpdate(Resource):
    pass
'''class UserLogin(Resource):
    def get(self):
        response = make_response(render_template('login.html', foo=42))
        response.headers['X-Parachutes'] = 'parachutes are cool'
        return response
    @classmethod
    def post(cls):
        global atributos
        min = timedelta(seconds=10)
        print(min)
        dados = atributos.parse_args()

        user = ContaModel.seach_by_login(dados['login'])
        if user and safe_str_cmp(user.password, dados['password']):
            token_de_acesso = create_access_token(identity=user.user_id, user_claims=user.login, expires_delta=min)
            resp = jsonify({'refresh': True})
            set_access_cookies(resp, token_de_acesso)
            session['user_id'] = user.login
            print(session['user_id'])
            return redirect('/user')
        response = make_response(render_template('login.html', foo=42))
        response.headers['X-Parachutes'] = 'parachutes are cool'
        return response


class UserLogout(Resource):
    def get(self):
        global resp
        if(resp==0):
            resp=0
            self.post()
        resp = {'logout': True}
        session['user_id'] = None
        respo=resp
        return respo


    def post(self):
        global resp
        print('logout')
        resp = {'logout': True}
        session['user_id'] = None
        self.get()
        #jwt_id = get_raw_jwt()['jti']
        #print(jwt_id)# JWT token identify
        #BLACKLIST.add(jwt_id)
        return resp, 200'''
