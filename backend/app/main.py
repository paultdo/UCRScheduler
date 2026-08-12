from fastapi import FastAPI
from app.routes.schedule import router as schedule_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(schedule_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://ucr-scheduler.vercel.app"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

