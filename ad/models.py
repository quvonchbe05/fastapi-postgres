from core.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from user.models import User

class Ads(Base):
    __tablename__ = "ads"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)