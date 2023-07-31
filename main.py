from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def genero( Año: str ): 
    """
    Se ingresa un año y devuelve un diccionario con los 5 géneros más vendidos en el orden correspondiente.
    
    return DICTIONARY?
    """
    return 0

def juegos( Año: str ):
    """
    Se ingresa un año y devuelve un diccionario con los juegos lanzados en el año.
    """
    return 0

def specs( Año: str ):
    """
    Se ingresa un año y devuelve un diccionario con los 5 specs que más se repiten en el mismo en el orden correspondiente.
    """
    return 0

def earlyacces( Año: str ):
    """
    Cantidad de juegos lanzados en un año con early access.
    """
    return 0

def sentiment( Año: str ):
    """
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

    Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}
    """
    return 0
         
def metascore( Año: str ):
    """
    Top 5 juegos según año con mayor metascore.
    """
    return 0

def predicción(genero, earlyaccess = True, ): #  ( + Variables que elijas)
    """
    Ingresando estos parámetros, deberíamos recibir el precio y RMC.
    """
    return 0
