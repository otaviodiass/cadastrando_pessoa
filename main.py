from fastapi import FastAPI
import rota.pessoa as pessoa

app = FastAPI()

app.include_router(pessoa.router)


@app.get("/")
def read_root():
    return {'mensagem': 'ativo'}
