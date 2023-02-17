from sqlalchemy import Column, String, Integer
from core.db import Base
from fastapi_users.db import SQLAlchemyBaseUserTable

class User(Base,SQLAlchemyBaseUserTable):
    name = Column(String, nullable=False)