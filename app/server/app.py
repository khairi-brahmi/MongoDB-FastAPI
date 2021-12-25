from fastapi import FastAPI
from .routes.student import router as StudentRouter
from .routes.section import router as SectionRouter
app = FastAPI()

app.include_router(StudentRouter, tags=["Students"], prefix="/student")
app.include_router(SectionRouter, tags=["Sections"], prefix="/section")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}