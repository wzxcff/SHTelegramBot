from .base import SessionLocal
from .models import User, Schedule, Deadline, Attendance, Subject, Admin
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


def add_admin(user_id: int) -> bool:
    session = get_session()
    user = session.query(User).filter(User.user_id == user_id).first()
    admin = Admin(user_id=user.id)
    session.add(admin)
    session.commit()
    session.refresh(admin)
    session.close()
    return True

# CRUD Subjects


def get_subject_by_id(subject_id: int) -> Subject:
    session = get_session()
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    session.close()
    return subject


def create_new_subject(name: str, teacher: str, lesson_type: str, start_time: str, end_time: str, link: str, hidden: bool = False) -> Subject:
    session = get_session()
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    end_time = datetime.datetime.strptime(end_time, "%H:%M")
    subject = Subject(name=name, teacher=teacher, lesson_type=lesson_type, start_time=start_time, end_time=end_time, link=link, hidden=hidden)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    session.close()
    return subject


def edit_subject_by_id(subject_id: int, name: str, teacher: str, lesson_type: str, start_time: str, end_time: str, link: str, hidden: bool = False) -> Subject:
    session = get_session()
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    subject.name = name
    subject.teacher = teacher
    subject.lesson_type = lesson_type
    subject.start_time = datetime.datetime.strptime(start_time, "%H:%M")
    subject.end_time = datetime.datetime.strptime(end_time, "%H:%M")
    subject.link = link
    subject.hidden = hidden
    session.commit()
    session.refresh(subject)
    session.close()
    return subject


def visibility_change_by_subject_id(subject_id: int, hidden: bool = False) -> Subject:
    session = get_session()
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    subject.hidden = hidden
    session.commit()
    session.refresh(subject)
    session.close()
    return subject


def delete_subject_by_id(subject_id: int) -> bool:
    session = get_session()
    subject = session.query(Subject).filter(Subject.id == subject_id).first()
    return safe_remove(subject, session)


# CRUD Schedule


def get_schedule_by_day(day: str) -> Schedule:
    session = get_session()
    schedule_for_day = session.query(Schedule).filter(Schedule.day == day).all()
    session.close()
    return schedule_for_day


def add_subject_to_schedule(subject_id: int, day: str) -> Schedule:
    session = get_session()
    schedule = Schedule(subject_id=subject_id, day=day)
    session.add(schedule)
    session.commit()
    session.refresh(schedule)
    session.close()
    return schedule


def delete_schedule_by_day_and_subject_id(day: str, subject_id: int) -> bool:
    session = get_session()
    schedule = session.query(Schedule).filter(Schedule.day == day, Subject.id == subject_id).all()
    return safe_remove(schedule, session)


def is_user_admin(user_id: int) -> bool:
    session = get_session()
    user = get_user_by_user_id(user_id)
    admin = session.query(Admin).filter(Admin.user_id == user.id).first()
    session.close()
    if admin:
        return True
    return False
