import requests
from typing import Dict

class Requisicoes():

    def __init__(self) -> None:
        self.URL = "http://127.0.0.1:8000/"

    def requisitar_todas_pessoas(self) -> Dict:
        resposta = requests.get(self.URL + "pessoa")
        if resposta.status_code:
            resp = resposta.json()
            return resp
    
    def requisitar_pessoa_por_email(self, email: str) -> Dict:
        resposta = requests.get(self.URL + f"pessoa/{email}")
        if resposta.status_code:
            resp = resposta.json()
            return resp

    def requisitar_adicionar_pessoa(self, dados: Dict) -> None:
        resposta = requests.post(self.URL + "pessoa", json=dados)
        if resposta.status_code:
            resp = resposta.json()
            return resp
    
    def requisitar_alterar_dados(self, email: str, dados: Dict) -> None:
        resposta = requests.put(self.URL + f"pessoa-altera/{email}", json=dados)
        if resposta.status_code:
            resp = resposta.json()
            return resp
    
    # função para deletar pessoa
    def requisitar_deletar_pessoa(self, email: str) -> None:
        resposta = requests.delete(self.URL + f"pessoa-delete/{email}")
        if resposta.status_code:
            resp = resposta.json()
            return resp
