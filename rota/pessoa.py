from fastapi import APIRouter
from dados import PESSOAS
from model import Pessoa

router = APIRouter(prefix='/pessoa', tags=['pessoa'])

# Lista todas as Pessoas
@router.get("/")
def listar_pessoas():
    return PESSOAS

# Busca uma Pessoa por email
@router.get("/{email}")
def buscar_por_email(email: str):
    for pessoa in PESSOAS:
        if pessoa['email'] == email:
            return {'dados': pessoa, 'status': True}
    return {'mensagem': 'Pessoa não encontrada!', 'status': False}

# Adiciona uma Pessoa
@router.post("/")
def adicionar_pessoa(pessoa: Pessoa):
    variavel = PESSOAS[-1]['id']
    pessoa = pessoa.model_dump()
    pessoa['id'] = variavel + 1
    PESSOAS.append(pessoa)
    return pessoa

# Altera os dados de uma Pessoa
@router.put("/altera/{email}")
def alterar_dados_pessoa(email: str, up_pessoa: Pessoa):
    for pessoa in PESSOAS:
        if pessoa['email'] == email:
            pessoa['nome'] = up_pessoa.nome
            pessoa['idade'] = up_pessoa.idade
            pessoa['altura'] = up_pessoa.altura
            pessoa['email'] = up_pessoa.email
            return {'dados': pessoa, 'status': True}
    return {'mensagem': 'Pessoa não encontrada!', 'status': False}

# Deletar uma Pessoa
@router.delete("/deleta/{email}")
def deletar_pessoa(email: str):
    for pessoa in PESSOAS:
        if pessoa['email'] == email:
            PESSOAS.remove(pessoa)
            return {'mensagem': 'Pessoa deletada!', 'status': True}
    return {'mensagem': 'Pessoa não encontrada!', 'status': False}
