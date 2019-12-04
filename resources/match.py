from flask_restful import Resource, reqparse
from models.conta import UsernameModel as UserModel

atributos = reqparse.RequestParser()
atributos.add_argument('user_ip', type=str, required=True, help="o campo 'user_ip' nao deve estar vazio")
atributos.add_argument('server', type=str, help="o campo 'user_resoluction' nao deve estar vazio")
atributos.add_argument('user_name', type=str, required=True, help="o campo 'user_name' nao deve estar vazio")
atributos.add_argument('personagem', type=str, help="o campo 'personagem' nao deve estar vazio")

class Match(Resource):
    def get(self):
        return {"voce": "deuget"}
    def post(self):
        global atributos;
        dados = atributos.parse_args()
        if dados["personagem"] is None:
            print("check")
            user=UserModel.seach(dados['user_name'])
            if user:
                if(user.user_ip==dados['user_ip']):
                    return {'message': 'User é seu'}, 200
                else:
                    return {'message': 'User já existe'}, 409
            else:
                print("dados: ", dados['user_ip'], dados['user_name'])
                user = UserModel(dados['user_ip'], dados['user_name'])
                try:
                    user.save_user()
                    return {'message': 'User {} reservado'.format(dados['user_name'])}, 201
                except:
                    print("error")
                    return {'message': 'error ao salvar'}, 500
        else:
            print(dados)
            return

