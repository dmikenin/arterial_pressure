from api.v1.serializers.add_pressure import AddPressureSerializer
from models.statistics_pressure import StatisticsPressure
from datetime import datetime

class AddPressureService:
    def add(self, data: AddPressureSerializer, db, user_id):
        try:
            item = StatisticsPressure(
                upper = data.upper,
                down = data.down,
                heartbeat = data.heartbeat,
                date_added = datetime.utcnow(),
                timezone=data.timezone,
                user_id = user_id)
            db.add(item)
            db.commit()
            return {
                'result': {"status": 'Success', "message": "Data added"},
                "code": 200
            }
        except:
            return {
                'result': {"status": 'Success', "message": "Problem with server"},
                "code": 500
            }