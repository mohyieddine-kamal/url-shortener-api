from fastapi import FastAPI

from database import Base, engine
from routers import urls

app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(urls.router)
app.include_router(urls.public_router)