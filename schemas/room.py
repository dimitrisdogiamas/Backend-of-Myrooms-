from pydantic import BaseModel
from decimal import Decimal

class RoomResponse(BaseModel):
  id: int
  title: str
  price_per_night: Decimal
  max_guests: int

  model_config = {'from_attributes': True} # Read from SQLAlchemy model

  # this lets you do RoomRead.model_validate(room) 
