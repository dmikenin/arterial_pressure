import time

import jwt

from core.config import JWT_SECRET, JWT_ALGORITHM


def generate_jwt(user_id: str):
    payload = {
        "user_id": str(user_id),
        "expires": time.time() + 8600
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM).decode("utf-8")
