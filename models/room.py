from sqlalchemy import Column, Integer, Numeric, String
from database import Base

class Room(Base):
  __tablename__ = "Rooms"
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  price_per_night = Column(Numeric(10,2), nullable=False)
  max_guests = Column(Integer, nullable=False)
