from fastapi import FastAPI
from src.api.routers import all_routers
from starlette.responses import Response

app = FastAPI(title="ChronoManager", version="1.0.0")


[app.include_router(r) for r in all_routers]


@app.get("/")
def health_check():
    return Response(status_code=200)
