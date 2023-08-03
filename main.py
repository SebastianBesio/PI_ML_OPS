from typing import Union
from fastapi import FastAPI
import json

app = FastAPI()

########################################
## TODO: Add validations
########################################

@app.get("/")
def read_root(): 
    return {"PI_ML_OPS": "Sebastian Besio"}

@app.get("/genero/{Year}")
def genero(Year: str): 
    """
    Se ingresa un año y devuelve un diccionario con los 5 géneros más vendidos en el orden correspondiente.
    """
    # Read data
    with open("datasets/steam_games_endpoint_1_genero.json") as json_file:
        genres_dict = json.load(json_file)

    # TODO Add validation

    # Since data is already sorted, get the first 5 as top 5.
    top5 = dict(list(genres_dict[Year].items())[0:5])
    return top5


@app.get("/juegos/{Year}")
def juegos( Year: str ):
    """
    Se ingresa un año y devuelve un diccionario con los juegos lanzados en el año.
    """
    # Read data
    with open("datasets/steam_games_endpoint_2_juegos.json") as json_file:
        juegos_list = json.load(json_file)

    # TODO Add validation

    return {"Año": Year, "Juegos": juegos_list[Year]}


@app.get("/specs/{Year}")
def specs( Year: str ):
    """
    Se ingresa un año y devuelve un diccionario con los 5 specs que más se repiten en el mismo en el orden correspondiente.
    """
    # Read data
    with open("datasets/steam_games_endpoint_3_specs.json") as json_file:
        specs_dict = json.load(json_file)

    # TODO Add validation

    # Since data is already sorted, get the first 5 as top 5.
    top5 = dict(list(specs_dict[Year].items())[0:5])
    return top5


@app.get("/earlyacces/{Year}")
def earlyacces( Year: str ):
    """
    Cantidad de juegos lanzados en un año con early access.
    """
    # Read data
    with open("datasets/steam_games_endpoint_4_earlyaccess.json") as json_file:
        earlyaccess_dict = json.load(json_file)

    # TODO Add validation, Top5 si teine al menos 5
    
    return {"Año": Year, "Early Access": earlyaccess_dict['early_access'][Year]}


@app.get("/sentiment/{Year}")
def sentiment( Year: str ):
    """
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

    Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}
    """
    # Read data
    with open("datasets/steam_games_endpoint_5_sentiment.json") as json_file:
        sentiment_dict = json.load(json_file)

    # TODO Add validation

    return {"Año": Year, "Sentiment": sentiment_dict[Year]}

@app.get("/metascore/{Year}")
def metascore( Year: str ):
    """
    Top 5 juegos según año con mayor metascore.
    """
    # Read data
    with open("datasets/steam_games_endpoint_6_metascore.json") as json_file:
        metascore_dict = json.load(json_file)

    # TODO Add validation, ademas de cantidad menor 5.

    # Since data is already sorted, get the first 5 as top 5.
    top5 = dict(list(metascore_dict[Year].items())[0:5])
    return top5


# def predicción(genero, earlyaccess = True, ): #  ( + Variables que elijas)
#     """
#     Ingresando estos parámetros, deberíamos recibir el precio y RMC.
#     """
#     return 0
