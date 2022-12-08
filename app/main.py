from fastapi import FastAPI
from dataframes import df_final
from starlette.responses import RedirectResponse

app= FastAPI(title="API de Luz",
             description="Estamos en una prueba de una API",
             version="1.0.1")


@app.get("/")
async def raiz():
    return RedirectResponse(url="/docs/")


@app.get("/get_max_duration/{anio},{plataforma},{um}")
async def get_max_duration(anio:int, plataforma:str, um:str):
    respuesta=df_final["type"]
    return respuesta

@app.get("/get_count_platform/{plataforma}")
async def validar_capicua(plataforma:str):
    plataforma=" No es capicúa"
    
@app.get("/get_listedin/{genero}")
async def validar_capicua(genero:str):
    respuesta=" No es capicúa"
    
@app.get("/get_actor/{plataforma}{año}")
async def validar_capicua(plataforma:str, año:int):
    respuesta=" No es capicúa"
