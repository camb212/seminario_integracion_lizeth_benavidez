from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AvisoBiblioteca(BaseModel):
    mensaje: str
    prioridad: int = 1
    nota_interna: str


@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "mensaje": "API de Gestión de Biblioteca con FastAPI + uv",
        "autor": "Andres Jurado",
        "version": "0.1.0",
    }


@router.get("/recepcion")
def endpoint_recepcion() -> AvisoBiblioteca:
    return AvisoBiblioteca(
        mensaje="Mostrador de préstamos abierto",
        nota_interna="turno mañana activo",
    )


@router.get("/catalogacion", response_model=AvisoBiblioteca)
def endpoint_catalogacion():
    return {
        "mensaje": "Ingreso de nuevos volúmenes al catálogo",
        "prioridad": 5,
        "nota_interna": "revisión de códigos ISBN pendiente",
    }


@router.get("/campo-extra", response_model=AvisoBiblioteca)
def endpoint_campo_extra():
    return {
        "mensaje": "Recordatorio de devolución",
        "prioridad": 5,
        "nota_interna": "debe aparecer porque está en el modelo",
        "campo_extra": "filtrado automáticamente por response_model",
    }