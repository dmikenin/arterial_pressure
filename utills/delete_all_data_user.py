from core.db import get_db, SessionLocal
from models.statistics_pressure import StatisticsPressure
from models.user import User


def delete_all_data_user(email: str):
    try:
        db = SessionLocal()
        user = db.query(User).filter(
            User.email == email).first()

        user_id = user.id

        db.query(StatisticsPressure).filter(
            StatisticsPressure.user_id == user_id).delete()

        db.commit()

        db.query(User).filter(
            User.id == user_id).delete()

        db.commit()
    except Exception as e:
        print(e)

