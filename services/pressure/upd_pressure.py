from api.v1.serializers.add_pressure import AddPressureSerializer
from models.statistics_pressure import StatisticsPressure


class UpdatePressureService:

    def update(self, data: AddPressureSerializer,db, user_id: str, id: str) -> dict:
        try:
            pressure = db.query(StatisticsPressure).filter(
                StatisticsPressure.user_id == user_id, StatisticsPressure.id == id).first()

            if not pressure:
                return {
                    'result': {
                        "status": "Failed",
                        "message": "Not data yet",
                    },
                    "code": 400
                }

            pressure.upper = data.upper
            pressure.down = data.down
            pressure.heartbeat = data.heartbeat

            db.add(pressure)
            db.commit()

            return {
                'result': {
                    "status": "Success",
                    "message": "Success update record",
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