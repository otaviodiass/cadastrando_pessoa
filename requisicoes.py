import requests
from typing import List, Dict

class Requisicoes():

    def __init__(self) -> None:
        self.URL = "http://127.0.0.1:8000/"

    def requisitar_todas_pessoas(self) -> Dict:
        resposta = requests.get(self.URL + "pessoa")
        if resposta.status_code:
            dados = resposta.json()
            return dados
    
    def requisitar_pessoa_por_email(self, email: str) -> Dict:
        resposta = requests.get(self.URL + f"pessoa/{email}")
        if resposta.status_code:
            dados = resposta.json()
            return dados
