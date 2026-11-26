from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

libro_router = APIRouter()


class LibroCreate(BaseModel):
    """Datos que envía el cliente para registrar un libro. Sin id: lo asigna el servidor."""
    titulo: str = Field(min_length=3, max_length=100)
    autor: str | None = None
    seccion: str = "general"
    etiquetas: list[str] = Field(default_factory=list)


class LibroRead(BaseModel):
    """Datos que expone el servidor al consultar un libro."""
    id: int
    titulo: str
    autor: str | None
    seccion: str
    etiquetas: list[str]
    prestado: bool


class LibroUpdate(BaseModel):
    """Datos opcionales para actualizar un libro en el catálogo."""
    titulo: str | None = Field(default=None, min_length=3, max_length=100)
    autor: str | None = None
    seccion: str | None = None
    etiquetas: list[str] | None = None
    prestado: bool | None = None


LIBROS: list[dict] = [
    {
        "id": 1,
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "seccion": "literatura",
        "etiquetas": ["biblioteca", "novela"],
        "prestado": False,
    },
    {
        "id": 2,
        "titulo": "Clean Code",
        "autor": "Robert C. Martin",
        "seccion": "tecnologia",
        "etiquetas": ["biblioteca", "software"],
        "prestado": False,
    },
]
NEXT_ID = len(LIBROS) + 1


@libro_router.post("/libros", response_model=LibroRead)
def crear_libro(libro: LibroCreate) -> dict:
    global NEXT_ID
    nuevo_libro = {
        "id": NEXT_ID,
        "prestado": False,
        "notas_catalogacion": "registrado desde la API de biblioteca",
        **libro.model_dump(),
    }
    LIBROS.append(nuevo_libro)
    NEXT_ID += 1
    return nuevo_libro


@libro_router.get("/libros", response_model=list[LibroRead])
def listar_libros() -> list[dict]:
    return LIBROS


@libro_router.patch("/libros/{libro_id}")
def actualizar_libro(libro_id: int, update: LibroUpdate) -> dict:
    for libro in LIBROS:
        if libro["id"] == libro_id:
            cambios = update.model_dump(exclude_unset=True)
            libro.update(cambios)
            return libro
    return {"error": "Libro no encontrado"}


@libro_router.post("/libros/from-model")
def crear_desde_modelo(libro: LibroCreate) -> dict:
    data = libro.model_dump()
    nuevo_libro = {"id": len(LIBROS) + 1, "prestado": False, **data}
    LIBROS.append(nuevo_libro)

    validado = LibroRead.model_validate(nuevo_libro)
    return validado.model_dump()


@libro_router.get("/libros/{libro_id}/raw-vs-validated")
def comparar_raw_validado(libro_id: int) -> dict:
    raw = next((l for l in LIBROS if l["id"] == libro_id), None)
    if raw is None:
        return {"error": "no encontrado"}

    validado = LibroRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validado.model_dump(),
        "validated_model_dump_json": validado.model_dump_json(),
    }


@libro_router.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int) -> dict:
    for index, libro in enumerate(LIBROS):
        if libro["id"] == libro_id:
            libro_eliminado = LIBROS.pop(index)
            return {
                "message": "Libro eliminado del catálogo correctamente",
                "deleted_libro": libro_eliminado,
            }

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado",
    )


@libro_router.get("/libros/{libro_id}", response_model=LibroRead)
def obtener_libro_por_id(libro_id: int) -> dict:
    for libro in LIBROS:
        if libro["id"] == libro_id:
            return libro

    raise HTTPException(
        status_code=404,
        detail="Libro no encontrado",
    )