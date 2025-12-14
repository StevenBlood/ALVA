from fastapi import FastAPI
from backend.api.routes import router
from backend.database import Base, engine
from backend.scheduler import start_scheduler

app = FastAPI(title="Game Database API")

Base.metadata.create_all(bind=engine)

start_scheduler()

app.include_router(router)


@app.get("/")
def root():
    return {"status": "GameDB backend fut"}
