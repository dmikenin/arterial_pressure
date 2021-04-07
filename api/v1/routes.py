from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.v1.serializers.add_pressure import AddPressureSerializer
from api.v1.serializers.response.responseAuth import ResponseAuthSerializer
from api.v1.serializers.auth.user import UserLoginSerializer, UserRegisterSerializer
from api.v1.serializers.response.responsePressue import ResponseAddPressue, ResponseGetListPressue, \
    ResponseGetOnePressue
from core.config import oauth2_scheme
from core.db import get_db
from services.auth.auth import AuthService
from services.auth.auth_bearer import JWTBearer
from services.auth.decode_jwt import decodeJWT
from services.pressure.add_pressure import AddPressureService
from services.pressure.del_pressure import DelPressureService
from services.pressure.get_pressure import GetPressureService
from services.pressure.upd_pressure import UpdatePressureService

router = APIRouter(
    prefix="/v1",
)



@router.post("/user/signup", tags=["user"], response_model=ResponseAuthSerializer)
async def create_user(user: UserRegisterSerializer = Body(...), db: Session = Depends(get_db)):
    auth = AuthService()
    result = auth.register(user, db)
    return JSONResponse(status_code=result["code"], content=result["result"])


@router.post("/user/login", tags=["user"], response_model=ResponseAuthSerializer)
async def user_login(user: UserLoginSerializer = Body(...), db: Session = Depends(get_db)):
    auth = AuthService()
    result = auth.login(user, db)
    return JSONResponse(status_code=result["code"], content=result["result"])


@router.post("/pressure/add", tags=["pressure"], response_model=ResponseAddPressue,
             dependencies=[Depends(JWTBearer())])
async def add_pressure(request_data: AddPressureSerializer,
                       token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = decodeJWT(token)
    addPressure = AddPressureService()
    result = addPressure.add(data=request_data, db=db, user_id=user['user_id'])
    return JSONResponse(status_code=result["code"], content=result["result"])


@router.get("/pressure", tags=["pressure"], response_model=ResponseGetListPressue,
            dependencies=[Depends(JWTBearer())])
async def get_list_pressure(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = decodeJWT(token)
    getPressure = GetPressureService()
    result = getPressure.get_list(db=db, user_id=user['user_id'])
    return JSONResponse(status_code=result["code"], content=result["result"])


@router.get("/pressure/{item_id}", tags=["pressure"], response_model=ResponseGetOnePressue,
            dependencies=[Depends(JWTBearer())])
async def get_one_pressure(item_id: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = decodeJWT(token)
    getPressure = GetPressureService()
    result = getPressure.get_one(db=db, user_id=user['user_id'], id=item_id)
    return JSONResponse(status_code=result["code"], content=result["result"])


@router.delete("/pressure/{item_id}", tags=["pressure"], response_model=ResponseAddPressue,
               dependencies=[Depends(JWTBearer())])
async def del_pressure(item_id: str, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = decodeJWT(token)
    delPressure = DelPressureService()
    result = delPressure.delete(db=db, user_id=user['user_id'], id=item_id)
    return JSONResponse(status_code=result["code"], content=result["result"])


@router.put("/pressure/{item_id}", tags=["pressure"], response_model=ResponseAddPressue,
            dependencies=[Depends(JWTBearer())])
async def upd_pressure(request_data: AddPressureSerializer, item_id: str, token: str = Depends(oauth2_scheme),
                       db: Session = Depends(get_db)):
    user = decodeJWT(token)
    updPressure = UpdatePressureService()
    result = updPressure.update(data=request_data, db=db, user_id=user['user_id'], id=item_id)
    return JSONResponse(status_code=result["code"], content=result["result"])
