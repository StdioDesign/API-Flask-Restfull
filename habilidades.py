from flask import request
from flask_restful import  Resource
import json

lista_habilidades = [{
        'id': 0,
        'habilidades': 'Python'
     },
    {
        'id': 1,
        'habilidades': 'Flask'
    },
    {
        'id': 2,
        'habilidades': 'Java'
    },
    {
        'id': 3,
        'habilidades': 'PHP'
    }

]

class ListaHabilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]

class Habilidades(Resource):
    def get(self, id):
        try:
            response = lista_habilidades[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'Habilidade de ID {id} não existe'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'Erro desconhecido. Procure o administrador da API'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}