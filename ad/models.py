from core.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Numeric, ForeignKey, Text
from sqlalchemy.orm import relationship
from user.models import User
from datetime import datetime

class Ad(Base):
    __tablename__ = "ads"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    price = Column(Numeric, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship(User)