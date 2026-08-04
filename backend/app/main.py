from fastapi import FastAPI
from app.routes.schedule import router as schedule_router

app = FastAPI()


app.include_router(schedule_router)

@app.get("/")
def root():
    return {"status": "ok"}
