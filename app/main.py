from fastapi import FastAPI
from dataframes import df_final
from starlette.responses import RedirectResponse

app= FastAPI(title="Proyecto Individual 1 - Henry",
             description="Luz Mayte Estrada Torvisco",
             version="1.0.1")


@app.get("/")
async def raiz():
    return RedirectResponse(url="/docs/")


@app.get("/get_max_duration/{anio},{plataforma},{um}")
async def get_max_duration(anio:int, plataforma:str, um:str):
    df_consul_1= df_final[["plataform","release_year","um","duration_3"]]
    df_consul_1=df_consul_1[(df_consul_1["um"]==um)&(df_consul_1["release_year"]==anio)&(df_consul_1["plataform"]==plataforma)].groupby("release_year").max()
    return df_consul_1

@app.get("/get_count_platform/{plataforma}")
async def get_count_platform(plataforma:str):
    df_consul_2= df_final[["plataform","title"]]
    df_consul_2=df_consul_2[df_consul_2["plataform"]==plataforma]
    df_consul_2=df_consul_2["plataform"].count()
    return df_consul_2
    
@app.get("/get_listedin/{genero}")
async def get_listedin(genero:str):
    df_consul_3= df_final[["plataform","listed_in"]]
    df_consul_3=df_consul_3[df_consul_3["listed_in"].str.contains(genero, regex=False)].groupby("plataform").count()
    return df_consul_3
    
@app.get("/get_actor/{actor}{anio}")
async def get_actor(actor:str, anio:float):
    df_consul_4=df_final[["plataform","cast","year_added"]]
    df_consul_4= df_consul_4.dropna(axis=0, how="all", subset=["cast"])
    df_consul_4=df_consul_4[df_consul_4["cast"].str.contains(actor, regex=False)]
    df_consul_4= df_consul_4[df_consul_4["year_added"]==anio]
    df_consul_4=df_consul_4["cast"].count()
    return df_consul_4
