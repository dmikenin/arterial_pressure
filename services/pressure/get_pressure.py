from api.v1.serializers.get_pressure import GetPressureSerializer
from models.statistics_pressure import StatisticsPressure


class GetPressureService:

    def get_list(self, db, user_id):
        try:
            pressure_list = db.query(StatisticsPressure).filter(
                StatisticsPressure.user_id == user_id)

            if not pressure_list:
                return {
                    'result': {
                        "pressure": [],
                        "status": "Success",
                        "message": "Not data yet",
                    },
                    "code": 200
                }

            processed_pressue = GetPressureSerializer()
            result_pressure = processed_pressue.serialize_many_row(pressure_list.all())

            return {
                'result': {
                    "pressure": result_pressure,
                    "status": "Success",
                    "message": "Success getting list data",
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

    def get_one(self, db, user_id, id):
        try:
            pressure = db.query(StatisticsPressure).filter(
                StatisticsPressure.user_id == user_id, StatisticsPressure.id == id).first()

            if not pressure:
                return {
                    'result': {
                        "pressure": [],
                        "status": "Success",
                        "message": "Not data yet",
                    },
                    "code": 200
                }

            processed_pressue = GetPressureSerializer()
            result_pressure = processed_pressue.serialize_one_row(pressure)


            return {
                'result': {
                    "pressure": result_pressure,
                    "status": "Success",
                    "message": "Success getting one data",
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