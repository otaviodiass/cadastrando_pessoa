from pydantic import BaseModel

class Pessoa(BaseModel):
    nome: str
    idade: int
    altura: float
    email: str
