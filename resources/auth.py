from managers.user import UserManager
from fastapi import APIRouter
from schemas.request.user import UserRegisterIn,UserLoginIn

router = APIRouter(tags=["Auth"])

@router.post("/register/",status_code=201)
async def register(user_data: UserRegisterIn):
    token = await UserManager.register(user_data.dict())
    return {"token":token}

@router.post("/login/")
async def login(user_data: UserLoginIn):
    token = await UserManager.login(user_data.dict())
    return {"token":token}
