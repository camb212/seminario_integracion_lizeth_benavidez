from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def bienvenida() -> dict[str, str]:
    return {
        "mensaje": "Bienvenido al sistema de gestión de biblioteca (FastAPI + uv)",
        "paso": "1",
    }