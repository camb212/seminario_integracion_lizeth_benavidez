# app/routers/paso1_task_create_body.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

task_router = APIRouter()

class TaskCreate(BaseModel):
    """Lo que el cliente envía para crear una tarea. Sin id: lo asigna el servidor."""
    title: str = Field(min_length=3, max_length=100)
    description: str | None = None
    priority: str = "medium"
    tags: list[str] = Field(default_factory=list)


class TaskRead(BaseModel):
    """Lo que el servidor expone al leer una tarea. Incluye campos calculados por el servidor."""
    id: int
    title: str
    description: str | None
    priority: str
    tags: list[str]
    is_completed: bool


class TaskUpdate(BaseModel):
    """Lo que el cliente envía para actualizar. TODOS los campos son opcionales."""
    title: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = None
    priority: str | None = None
    tags: list[str] | None = None
    is_completed: bool | None = None


TASKS: list[dict] = [
    {"id": 1, "title": "Comprar leche", "description": None, "priority": "medium", "tags": ["fastapi", "tasks"], "is_completed": False},
    {"id": 2, "title": "Pagar el internet", "description": None, "priority": "high", "tags": ["fastapi", "tasks"], "is_completed": False},
]
NEXT_ID = len(TASKS) + 1


@task_router.post("/tasks", response_model=TaskRead)
def create_task(task: TaskCreate) -> dict:
    global NEXT_ID
    new_task = {
        "id": NEXT_ID,
        "is_completed": False,
        "internal_notes": "creado desde la API",
        **task.model_dump(),
    }
    TASKS.append(new_task)
    NEXT_ID += 1
    return new_task


@task_router.get("/tasks", response_model=list[TaskRead])
def list_tasks() -> list[dict]:
    return TASKS


@task_router.patch("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            changes = update.model_dump(exclude_unset=True)
            task.update(changes)
            return task
    return {"error": "Tarea no encontrada"}

@task_router.post("/tasks/from-model")
def create_from_model(task: TaskCreate) -> dict:
    # model_dump(): instancia de Pydantic -> dict plano de Python
    data = task.model_dump()
    new_task = {"id": len(TASKS) + 1, "is_completed": False, **data}
    TASKS.append(new_task)

    # model_validate(): dict de Python -> instancia validada de Pydantic
    validated = TaskRead.model_validate(new_task)
    return validated.model_dump()

@task_router.get("/tasks/{task_id}/raw-vs-validated")
def compare_raw_validated(task_id: int) -> dict:
    raw = next((t for t in TASKS if t["id"] == task_id), None)
    if raw is None:
        return {"error": "no encontrada"}

    # model_validate lanza una excepción si el dict no cumple el schema de TaskRead
    validated = TaskRead.model_validate(raw)

    return {
        "raw_dict": raw,
        "validated_model_dump": validated.model_dump(),
        "validated_model_dump_json": validated.model_dump_json(),
    }

@task_router.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> dict:
    for index, task in enumerate(TASKS):
        if task["id"] == task_id:
            deleted_task = TASKS.pop(index)

            return {
                "message": "Tarea eliminada correctamente",
                "deleted_task": deleted_task
            }

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )

@task_router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task_by_id(task_id: int) -> dict:
    for task in TASKS:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )