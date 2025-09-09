from .base import SessionLocal
from .models import User, Schedule, Deadline, Attendance
import datetime


def get_session():
    return SessionLocal()


def safe_remove(objects: iter, session: SessionLocal) -> bool:
    try:
        for entry in objects:
            session.delete(entry)

        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False
    finally:
        session.close()

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


def increment_user_score(user_id: int, score: int) -> User:
    session = get_session()
    user = session.query(User).filter(User.user_id == user_id).first()
    user.score += score
    session.commit()
    session.refresh(user)
    session.close()
    return user


def decrement_user_score(user_id: int, score: int) -> User:
    session = get_session()
    user = session.query(User).filter(User.user_id == user_id).first()
    user.score -= score
    session.commit()
    session.refresh(user)
    session.close()
    return user

# CRUD for managing schedule


def add_new_to_schedule(title: str, description: str, day: str, lesson_type: str, start_time: str, end_time: str, link: str = None, hidden: bool = False) -> Schedule:
    session = get_session()
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    end_time = datetime.datetime.strptime(end_time, "%H:%M")
    subject = Schedule(title=title, description=description, day=day, lesson_type=lesson_type, start_time=start_time, end_time=end_time, link=link, hidden=hidden)
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
    session.close()
    return schedule


def get_schedule() -> list:
    session = get_session()
    schedule = session.query(Schedule).all()
    session.close()
    return schedule


def remove_subject_by_start_time_and_day(start_time: str, day: str) -> bool:
    session = get_session()
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    subject_to_remove = session.query(Schedule).filter(Schedule.start_time == start_time, Schedule.day == day).all()

    return safe_remove(subject_to_remove, session)


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


def get_deadlines_by_end_date(end_date: str) -> list:
    session = get_session()
    end_date = datetime.datetime.strptime(end_date, "%d.%m.%y %H:%M")
    deadlines = session.query(Deadline).filter(Deadline.ending_date == end_date).all()
    session.close()
    return deadlines


def remove_deadlines_by_name_and_end_date(name: str, end_date: str) -> bool:
    session = get_session()
    end_date = datetime.datetime.strptime(end_date, "%d.%m.%y %H:%M")
    deadlines_to_remove = session.query(Deadline).filter(Deadline.event_name == name, Deadline.ending_date == end_date).all()

    return safe_remove(deadlines_to_remove, session)


