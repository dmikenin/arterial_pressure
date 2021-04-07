from datetime import timedelta, datetime
from typing import List


class GetPressureSerializer:

    def _forma_date(self, date_db, timezone):
        date = date_db + timedelta(hours=timezone)
        return date.strftime('%m.%d.%Y'), date.strftime('%H:%M')

    def _serialize(self, item) -> dict:
        date, time = self._forma_date(item.date_added, item.timezone)
        return {
                    "id": str(item.id),
                    "upper": item.upper,
                    "down": item.down,
                    "heartbeat": item.heartbeat,
                    "date": date,
                    "time": time,
                }

    def serialize_many_row(self, data) -> List[dict]:
        total_result = list()
        for item in data:
            total_result.append(self._serialize(item))
        return total_result

    def serialize_one_row(self, data) -> dict:
        return self._serialize(data)