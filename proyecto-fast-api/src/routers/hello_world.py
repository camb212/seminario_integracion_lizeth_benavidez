from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str 

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "autor":"Andres Jurado",
            "version" : "0.1.0"}

@router.get("/christian")
def endpoint_andres() -> Mensaje:
    return Mensaje(texto="Hola Andres", campo_interno= "desde andres link")

@router.get("/jurado", response_model=Mensaje)
def endpoint_jurado():
    return {"texto": "Hola Jurado", 
            "prioridad": 5, 
            "campo_interno": "imprime desde endpoint jurado"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Jurado", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo", 
            "campo_extra":"no deberia salir"}