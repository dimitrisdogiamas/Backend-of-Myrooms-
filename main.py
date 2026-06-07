from fastapi import FastAPI
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from models.room import Room
from schemas.room import RoomResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
app = FastAPI()



# cors configuration for expo app
app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "*",
    ],
  allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)

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

@app.get("/rooms/{room_id}", response_model=RoomResponse)
def get_room_by_id(room_id: int, db: Session = Depends(get_db)):
  room = db.query(Room).filter(Room.id == room_id).first()
  if not room:
    raise HTTPException(status_code=404, detail="Room not found")
  return room




