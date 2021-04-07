from pydantic import BaseModel

class ResponseAuthSerializer(BaseModel):
    status: str
    message: str
    access_token: str
