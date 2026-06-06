from fastapi import FastAPI
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello World"}

@app.get("/db")
def read_db(db: Session = Depends(get_db)):
  return {"message": "Database connected"}
