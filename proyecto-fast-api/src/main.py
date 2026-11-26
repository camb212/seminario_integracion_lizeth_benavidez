from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_world import router
from routers.task_router import task_router
from routers.hello_world_mp import router as hello_world_mp_router
from routers.paso1_bienvenida_mp import router as paso1_bienvenida_mp_router
from routers.libro_router_mp import libro_router as libro_router_mp

app = FastAPI(title="Curso FastAPI + uv")

app.include_router(router)
app.include_router(task_router)
app.include_router(hello_world_mp_router, tags=["Biblioteca - General"])
app.include_router(paso1_bienvenida_mp_router, prefix="/bienvenida", tags=["Biblioteca - Bienvenida"])
app.include_router(libro_router_mp, tags=["Biblioteca - Libros"])
