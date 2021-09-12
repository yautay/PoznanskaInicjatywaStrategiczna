from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.pis_user import PisUser as User
from db.session import get_db
from schemas.collections import CollectionCreate
from db.repository.pis_users import retrieve_users_by_id
from apis.version_1.route_login import get_current_user_from_token
from apis.version_1.wrapers.wrapper_route_bgg import WrapperRouteBgg
import logging

logger = logging.getLogger('RouteBgg')


router = APIRouter()


@router.post("/collection")
def retrieve_collection(data: CollectionCreate,
                        db: Session = Depends(get_db),
                        current_user: User = Depends(get_current_user_from_token)):
    logger.info("DDDDDDDDDD")
    response = {}
    authorized = data.bgg_user == retrieve_users_by_id(current_user.id, db=db).bgg_user or \
        current_user.superuser or current_user.administrator

    if not authorized:
        logger.warning("User not authorized")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

    interface = WrapperRouteBgg(db=db, bgg_user=data.bgg_user)
    if not interface.synchronize():
        logger.warning("Synchronization unsuccessful")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"detail": f"Successfully synchronized '{data.bgg_user}' collection"}

