from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.models.user import User
from db.session import get_db
from schemas.collections import CollectionCreate
# from db.repository.collections import synchronize_collection
from db.repository.users import retrieve_users_by_id
from apis.version_1.route_login import get_current_user_from_token


router = APIRouter()


# @router.post("/collection")
# def retrieve_collection(data: CollectionCreate,
#                         db: Session = Depends(get_db),
#                         current_user: User = Depends(get_current_user_from_token)):
#     response = {}
#     if data.bgg_user == retrieve_users_by_id(current_user.id, db=db).bgg_user or\
#             current_user.superuser or current_user.administrator:
#         if not synchronize_collection(data=data, db=db, user_id=current_user.id):
#             raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
#         return {"detail": f"Successfully synchronized '{data.bgg_user}' collection"}
#     else:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
