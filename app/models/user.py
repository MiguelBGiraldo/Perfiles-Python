from pydantic import BaseModel, Field
from typing import Optional, List

class UserProfile(BaseModel):
    user_id: str
    personal_url: Optional[str]
    nickname: Optional[str]
    public_contact_info: Optional[bool] = False
    state: Optional[bool] = True
    address: Optional[str]
    biography: Optional[str]
    organization: Optional[str]
    country: Optional[str]
    social_links: Optional[List[str]] = []

    class Config:
        orm_mode = True
