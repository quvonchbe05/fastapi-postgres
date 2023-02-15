from pydantic import BaseModel, Field

class Ad(BaseModel):
    name: str = Field(max_length=250)
    text: str
    price: int = Field(ge=0)
    
class CreateAd(Ad):
    user_id: int