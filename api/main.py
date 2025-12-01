from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="PIIShield")
app.include_router(router)
