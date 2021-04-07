from datetime import datetime
import uuid

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from core.db import Base


class StatisticsPressure(Base):
    __tablename__ = "statistics_pressures"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    upper = Column(Integer)
    down = Column(Integer)
    heartbeat = Column(Integer, nullable=True)
    date_added = Column(DateTime, default=datetime.utcnow())
    timezone = Column(Integer, )

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    user = relationship("User", back_populates="pressures")




