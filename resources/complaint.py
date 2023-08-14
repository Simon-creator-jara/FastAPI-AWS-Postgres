from typing import List
from managers.auth import is_approver
from managers.auth import is_admin
from managers.auth import is_complainer
from schemas.response.complaint import ComplaintOut
from schemas.request.complaint import ComplaintIn
from managers.complaint import ComplaintManager
from fastapi import APIRouter, Depends, Request
from managers.auth import oauth2_scheme


router = APIRouter(tags=["Complaints"])

@router.get("/complaints/", dependencies=[Depends(oauth2_scheme)],response_model=List[ComplaintOut])
async def get_complaints(request: Request):
    user = request.state.user
    return await ComplaintManager.get_complaints(user)


@router.post("/complaints/", dependencies=[Depends(oauth2_scheme),Depends(is_complainer)],response_model=ComplaintOut)
async def create_complaint(request: Request,complaint: ComplaintIn):
    user=request.state.user
    return await ComplaintManager.create_complaint(complaint.dict(),user)

@router.delete("/complaints/{complaint_id}/",dependencies=[Depends(oauth2_scheme),Depends(is_admin)], status_code=204)
async def delete_complaint(complaint_id:int):
    await ComplaintManager.delete(complaint_id)

@router.put("/complaints/{complaint_id}/approve",dependencies=[Depends(oauth2_scheme),Depends(is_approver)], status_code=204)
async def approve_complaint(complaint_id: int):
    await ComplaintManager.approve(complaint_id)

@router.put("/complaints/{complaint_id}/reject",dependencies=[Depends(oauth2_scheme),Depends(is_approver)], status_code=204)
async def reject_complaint(complaint_id: int):
    await ComplaintManager.reject(complaint_id)


