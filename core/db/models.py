from sqlalchemy import Column, BIGINT, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
import datetime
from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)

    added_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    attendances = relationship("Attendance", back_populates="user")
    alerts = relationship("Alert", back_populates="user")
    whitelists = relationship("Whitelist", back_populates="user")


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(BIGINT, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    day = Column(String, nullable=False)
    lesson_type = Column(String, nullable=False)
    hidden = Column(Boolean, nullable=False, default=False)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    link = Column(String, nullable=True)

    attendances = relationship("Attendance", back_populates="subject")


class Deadline(Base):
    __tablename__ = 'deadlines'

    id = Column(BIGINT, primary_key=True, index=True)
    event_name = Column(String, nullable=False)
    event_description = Column(String, nullable=True)
    ending_date = Column(DateTime, nullable=True)

    added_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))


class Attendance(Base):
    __tablename__ = 'attendances'

    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, ForeignKey('users.id'), nullable=False)
    schedule_id = Column(BIGINT, ForeignKey('schedules.id'), nullable=False)

    added_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    user = relationship("User", back_populates="attendances")
    subject = relationship("Schedule", back_populates="attendances")


class Alert(Base):
    __tablename__ = 'alerts'

    id = Column(BIGINT, primary_key=True, index=True)
    text = Column(String, nullable=False)

    added_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))


class Whitelist(Base):
    __tablename__ = 'whitelist'

    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="whitelists")


