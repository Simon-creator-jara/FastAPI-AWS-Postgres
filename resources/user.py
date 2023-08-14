from typing import List, Optional
from models.enums import RoleType
from schemas.response.user import UserOut
from managers.user import UserManager
from managers.auth import is_admin
from fastapi import APIRouter, Depends
from managers.auth import oauth2_scheme

router = APIRouter(tags=["Users"])

@router.get("/users/",dependencies=[Depends(oauth2_scheme), Depends(is_admin)], response_model=List[UserOut])
async def get_users(email: Optional[str]=None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_all_users()

@router.put("/users/{user_id}/make-admin",dependencies=[Depends(oauth2_scheme), Depends(is_admin)],status_code=204)
async def make_admin(user_id:int):
    await UserManager.change_role(RoleType.admin, user_id)

@router.put("/users/{user_id}/make-approver",dependencies=[Depends(oauth2_scheme), Depends(is_admin)],status_code=204)
async def make_approver(user_id:int):
    await UserManager.change_role(RoleType.approver, user_id)

    