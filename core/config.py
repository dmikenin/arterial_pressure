from fastapi.security import OAuth2PasswordBearer

JWT_SECRET = "efkhbdVLHKwhvbi3fbKADJDVBidjvbf"
JWT_ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")