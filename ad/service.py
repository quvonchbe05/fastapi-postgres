from sqlalchemy.orm import Session
from .models import Ad
from .schemas import CreateAd

def get_ad_list(db: Session):
    return db.query(Ad).all()

def create_ad(db: Session, new_ad: CreateAd):
    new_ad = Ad(**new_ad.dict())
    db.add(new_ad)
    db.commit()
    db.refresh(new_ad)
    return new_ad