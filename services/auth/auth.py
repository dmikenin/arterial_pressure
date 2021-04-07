import bcrypt
from sqlalchemy import exists

from api.v1.serializers.auth.user import UserLoginSerializer, UserRegisterSerializer
from models.user import User
from services.auth.genereate_jwt import generate_jwt
from validate_email import validate_email
from datetime import datetime

class AuthService:

    def check_user(self, email: str, db):
        isExistUSer = db.query(exists().where(User.email == email)).scalar()
        if isExistUSer:
            return True
        return False

    def _hash_password(self, password: str) -> str:
       return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()).decode('utf8')

    def _check_password(self, user_password, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf8'), user_password.encode())

    def register(self, user: UserRegisterSerializer, db):
        try:

            if self.check_user(user.email, db):
                return {
                    "result": {'message': 'User exist in DB', 'status': 'Failed'}, "code": 400
                }

            user = User(
                email=user.email,
                first_name=user.first_name,
                password=self._hash_password(user.password),
                date_register=datetime.utcnow(),
                timezone=user.timezone
            )
            db.add(user)
            db.commit()

            token = generate_jwt(user.id)

            return {
                'result': {
                    "access_token": token,
                    "status": "Success",
                    "message": "User register",
                },
                "code": 200
            }
        except:
            return {
                "result": {
                    "access_token": "",
                    "status": "Failed",
                    "message": "User not register",
                },
                "code": 500
            }


    def login(self, user: UserLoginSerializer, db):
        try:

            if not self.check_user(user.email, db):
                return {
                    "result": {'message': 'User not exist in DB', 'status': 'Failed'}, "code": 400
                }

            user_db = db.query(User).filter(User.email == user.email).first()

            if validate_email(user.email) is not True:
                return {
                    "result": {'message': 'Wrong email', 'status': 'Failed'}, "code": 400
                }

            if self._check_password(user_db.password, user.password) is not True:
                return {
                    "result": { 'message': 'Wrong password', 'status': 'Failed'}, "code": 400
                }

            token = generate_jwt(user_db.id)

            return {
                'result': {
                    "access_token": token,
                    "status": "Success",
                    "message": "User login",
                },
                "code": 200
            }
        except:
            return {
                "result": {
                    "access_token": "",
                    "status": "Failed",
                    "message": "User not logged",
                },
                "code": 500
            }