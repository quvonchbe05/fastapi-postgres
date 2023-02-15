from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, desc
from .models import Ad
from core.utils import get_db
from .service import get_ad_list, create_ad as create_ad_schema
from fastapi.exceptions import HTTPException
from .schemas import CreateAd

router = APIRouter(
    prefix='/ad',
    tags=["Ad actions"]
)

@router.get('/list')
async def ad_list(db: Session = Depends(get_db)):
    try:
        ads = get_ad_list(db)
        return {
            'status':'success!',
            'ads':ads
        }
    except:
        raise HTTPException(
            status_code=500,
            detail="Qandaydir xato bor!"
        )
        
        
@router.post('/create')
def create_ad(new_ad: CreateAd, db: Session = Depends(get_db)):
    try:
        new_ad = create_ad_schema(db, new_ad)
        return {
            'status':'success!',
            'new_ad':new_ad
        }
    except:
        raise HTTPException(
            status_code=500,
            detail="Qandaydir xato bor!"
        )