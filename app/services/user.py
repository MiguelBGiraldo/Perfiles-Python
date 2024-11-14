from ..database import db
from ..models.user import UserProfile

async def update_user_profile(user_id: str, profile_data: UserProfile):
    result = await db.user_profiles.find_one_and_update(
        {"user_id": user_id},
        {"$set": profile_data.dict(exclude_unset=True)},
        return_document=True
    )
    return result
