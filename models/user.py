import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from datetime import datetime

from core.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String(120), default='')
    first_name = Column(String(60))
    password = Column(String(500))
    date_register = Column(DateTime, default=datetime.utcnow())
    timezone = Column(Integer,)

    pressures = relationship("StatisticsPressure", back_populates="user")
