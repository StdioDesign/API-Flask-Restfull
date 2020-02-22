from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, ListaHabilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0,
        'nome': 'Marlon',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id': 1,
        'nome': 'Galleani',
        'habilidades': ['Python', 'Django']}
]

# Devolve um desenvolvedor pelo ID, tambem altera e deleta
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'Desenvolvedor de ID {id} não existe'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'Erro desconhecido. Procure o administrador da API'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(ListaHabilidades, '/habilidades/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')



if __name__ == '__main__':
    app.run(debug=True)