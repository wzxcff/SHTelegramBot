from sqlalchemy import Column, BIGINT, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    score = Column(Integer, nullable=False, default=0)

    added_at = Column(DateTime(timezone=True), server_default=func.now())

    attendances = relationship("Attendance", back_populates="user")
    whitelists = relationship("Whitelist", back_populates="user")
    admins = relationship("Admin", back_populates="user")


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="admins")

    added_at = Column(DateTime(timezone=True), server_default=func.now())


class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(BIGINT, primary_key=True, index=True)
    subject_id = Column(BIGINT, ForeignKey('subjects.id'), nullable=False)
    subject = relationship("Subject", back_populates="schedule")
    day = Column(String, nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher = Column(String, nullable=False)
    lesson_type = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    link = Column(String, nullable=True)
    hidden = Column(Boolean, nullable=False, default=False)

    added_at = Column(DateTime(timezone=True), server_default=func.now())

    schedules = relationship("Schedule", back_populates="subject")
    attendances = relationship("Attendance", back_populates="subject")


class Deadline(Base):
    __tablename__ = 'deadlines'

    id = Column(BIGINT, primary_key=True, index=True)
    event_name = Column(String, nullable=False)
    event_description = Column(String, nullable=True)
    ending_date = Column(DateTime, nullable=True)

    added_at = Column(DateTime(timezone=True), server_default=func.now())


class Attendance(Base):
    __tablename__ = 'attendances'

    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, ForeignKey('users.id'), nullable=False)
    subject_id = Column(BIGINT, ForeignKey('subjects.id'), nullable=False)

    added_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="attendances")
    subject = relationship("Subject", back_populates="attendances")


class Alert(Base):
    __tablename__ = 'alerts'

    id = Column(BIGINT, primary_key=True, index=True)
    text = Column(String, nullable=False)

    added_at = Column(DateTime(timezone=True), server_default=func.now())


class Whitelist(Base):
    __tablename__ = 'whitelist'

    id = Column(BIGINT, primary_key=True, index=True)
    user_id = Column(BIGINT, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="whitelists")


