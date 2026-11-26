from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def bienvenida() -> dict[str, str]:
    return {"mensaje": "Bienvenido al curso de FastAPI + uv", "paso": "1"}