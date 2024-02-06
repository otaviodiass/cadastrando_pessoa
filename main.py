from fastapi import FastAPI
from pessoa import Pessoa

app = FastAPI()


PESSOAS = [
    {
        'nome': 'Jose',
        'idade': 32,
        'altura': 1.78,
        'email': 'jose@email',
        'id': 1
    },
    {
        'nome': 'Pedro',
        'idade': 44,
        'altura': 1.80,
        'email': 'pedro@email',
        'id': 2
    }
]


@app.get("/")
def read_root():
    return {'mensagem': 'ativo'}


# Lista todas as Pessoas
@app.get("/pessoa")
def listar_pessoas():
    return PESSOAS


# Busca uma Pessoa por email
@app.get("/pessoa-email/{email}")
def buscar_por_email(email: str):
    for pessoa in PESSOAS:
        if pessoa['email'] == email:
            return pessoa
    return {'mensagem': 'pessoa não encontrada!'}


# Busca uma Pessoa por id
@app.get("/pessoa-id/{id}")
def buscar_por_id(id: int):
    for pessoa in PESSOAS:
        if pessoa['id'] == id:
            return pessoa
    return {'mensagem': 'pessoa não encontrada!'}


# Adiciona uma Pessoa
@app.post("/pessoa")
def adicionar_pessoa(pessoa: Pessoa):
    variavel = PESSOAS[-1]['id']
    pessoa = pessoa.model_dump()
    pessoa['id'] = variavel + 1
    PESSOAS.append(pessoa)
    return pessoa


# Altera os dados de uma Pessoa
@app.put("/pessoa-altera/{id}")
def alterar_dados_pessoa(id: int, up_pessoa: Pessoa):
    for pessoa in PESSOAS:
        if pessoa['id'] == id:
            pessoa['nome'] = up_pessoa.nome
            pessoa['idade'] = up_pessoa.idade
            pessoa['altura'] = up_pessoa.altura
            pessoa['email'] = up_pessoa.email
            return pessoa
    return {'mensagem': 'pessoa não encontrada!'}


# Deletar uma Pessoa
@app.delete("/pessoa-delete/{id}")
def deletar_pessoa(id: int):
    for pessoa in PESSOAS:
        if pessoa['id'] == id:
            PESSOAS.remove(pessoa)
            return {'mensagem': 'pessoa deletada!'}
    return {'mensagem': 'pessoa não encontrada!'}
