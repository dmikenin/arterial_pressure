from models.statistics_pressure import StatisticsPressure


class DelPressureService:

    def delete(self, db, user_id: str, id: str) -> dict:
        try:
            pressure = db.query(StatisticsPressure).filter(
                StatisticsPressure.user_id == user_id, StatisticsPressure.id == id)

            if not pressure:
                return {
                    'result': {
                        "status": "Failed",
                        "message": "Not data yet",
                    },
                    "code": 400
                }

            db.query(StatisticsPressure).filter(
                StatisticsPressure.user_id == user_id, StatisticsPressure.id == id).delete()

            db.commit()

            return {
                'result': {
                    "status": "Success",
                    "message": "Success delete record",
                },
                "code": 200
            }
        except:
            return {
                "result": {
                    "status": "Failed",
                    "message": "Problem with server",
                },
                "code": 500
            }