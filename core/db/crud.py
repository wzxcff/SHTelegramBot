from .base import SessionLocal
from .models import User, Schedule, Deadline, Attendance
import datetime


def get_session():
    return SessionLocal()

# CRUD for managing users


def create_user(user_id: int, username: str = None, first_name: str = None, last_name: str = None) -> User:
    session = get_session()
    user = User(user_id=user_id, username=username, first_name=first_name, last_name=last_name)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return user


def get_user_by_user_id(user_id: int) -> User:
    session = get_session()
    user = session.query(User).filter(User.user_id == user_id).first()
    session.close()
    return user

# CRUD for managing schedule


def add_new_to_schedule(title: str, description: str, day: str, start_time: str, end_time: str, link: str = None, hidden: bool = False) -> Schedule:
    session = get_session()
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    end_time = datetime.datetime.strptime(end_time, "%H:%M")
    subject = Schedule(title=title, description=description, day=day, start_time=start_time, end_time=end_time, link=link, hidden=hidden)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    session.close()
    return subject


def get_subject_by_id(subject_id: int) -> Schedule:
    session = get_session()
    subject = session.query(Schedule).filter(Schedule.id == subject_id).first()
    session.close()
    return subject


def get_subjects_by_day(day: str) -> list:
    session = get_session()
    schedule = session.query(Schedule).filter(Schedule.day == day).all()
    return schedule


# CRUD for managing deadlines


def add_new_deadline(name: str, description: str, end_date: str) -> Deadline:
    session = get_session()
    end_date = datetime.datetime.strptime(end_date, "%d.%m.%y %H:%M")
    deadline = Deadline(event_name=name, event_description=description, ending_date=end_date)
    session.add(deadline)
    session.commit()
    session.refresh(deadline)
    session.close()
    return deadline


