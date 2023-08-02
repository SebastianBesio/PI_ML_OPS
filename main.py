from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"My own": "API"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
"""
You already created an API that:
    Receives HTTP requests in the paths / and /items/{item_id}.
    Both paths take GET operations (also known as HTTP methods).
    The path /items/{item_id} has a path parameter item_id that should be an int.
    The path /items/{item_id} has an optional str query parameter q.
"""

# STARTING HERE, Take this to another .py?
import pandas as pd
def read_steam_games_data():
    """
    Reads steam_games_format_ok.json and returns a dataframe.
    """
    return pd.read_json("datasets/steam_games_format_ok.json")


@app.get("/genero/{Year}")
def genero(Year: str): 
    """
    Se ingresa un año y devuelve un diccionario con los 5 géneros más vendidos en el orden correspondiente.
    
    return DICTIONARY?
    """
    # Read data
    df = read_steam_games_data()
    # Since the genres column are list we need to explode it to count each genre.
    df = df.explode('genres')
    # Filter by the parameter year.
    df = df[df['release_date'].str.contains(Year, na=False)]
    # Get top 5 
    top5 = df['genres'].value_counts()[0:5].to_dict()

    return top5



# DECORADOR????????
# def juegos( Año: str ):
#     """
#     Se ingresa un año y devuelve un diccionario con los juegos lanzados en el año.
#     """
#     return 0

# def specs( Año: str ):
#     """
#     Se ingresa un año y devuelve un diccionario con los 5 specs que más se repiten en el mismo en el orden correspondiente.
#     """
#     return 0

# def earlyacces( Año: str ):
#     """
#     Cantidad de juegos lanzados en un año con early access.
#     """
#     return 0

# def sentiment( Año: str ):
#     """
#     Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

#     Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}
#     """
#     return 0
         
# def metascore( Año: str ):
#     """
#     Top 5 juegos según año con mayor metascore.
#     """
#     return 0



# def predicción(genero, earlyaccess = True, ): #  ( + Variables que elijas)
#     """
#     Ingresando estos parámetros, deberíamos recibir el precio y RMC.
#     """
#     return 0
