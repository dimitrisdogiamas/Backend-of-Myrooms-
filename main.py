from fastapi import FastAPI
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from models.room import Room
from schemas.room import RoomResponse
app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello World"}

@app.get("/db")
def read_db(db: Session = Depends(get_db)):
  return {"message": "Database connected"}

# endpoint for getting all rooms
@app.get("/rooms", response_model=list[RoomResponse])
def get_rooms(db: Session = Depends(get_db)):
  rooms = db.query(Room).all()
  # this is the query to get all rooms from the database
  return rooms # this is the response to the client
