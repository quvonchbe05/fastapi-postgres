from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from .models import Ad
from core.utils import get_db

router = APIRouter(
    prefix='/ad',
    tags=["Ad actions"]
)

@router.get('/list')
async def ad_list(session: AsyncSession = Depends(get_db)):
    stmt = select(Ad).order_by(desc(Ad.id))
    result = session.execute(stmt)
    return {}