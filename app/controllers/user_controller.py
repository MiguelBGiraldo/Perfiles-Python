from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection
from ..models.user import UserProfile
from ..services.log_service import send_log_to_api
from ..services.log_service import LogRequest

class UserController:
    def __init__(self, db: AsyncIOMotorCollection):
        self.collection = db

    async def create_user_profile(self, profile: UserProfile):
        await self.collection.insert_one(profile.dict())
        return profile

    async def get_user_profile(self, user_id: str):
        profile = await self.collection.find_one({"user_id": user_id, "state": True})
        if not profile:
            log = LogRequest (
                application="Perfiles",
                level="high",
                className= "get_user_profile",
                summary="No fue posible obtener el perfil",
                description="Error 404, User profile not found or deleted"
            )
            send_log_to_api(log)
            raise HTTPException(status_code=404, detail="User profile not found or deleted")
        return UserProfile(**profile)


    async def get_all_user_profiles(self):
        profiles = []
        async for profile in self.collection.find({"state": True}):  # Filtra solo los perfiles activos
            profiles.append(UserProfile(**profile))
        return profiles

    async def update_user_profile(self, user_id: str, profile: UserProfile):
        result = await self.collection.update_one(
            {"user_id": user_id, "state": True},  # Solo permite actualizar si el estado es True
            {"$set": profile.dict(exclude_unset=True)}  # Actualiza solo los campos proporcionados
        )
        if result.matched_count == 0:
            log = LogRequest (
                application="Perfiles",
                level="high",
                className= "update_user_profile",
                summary="No fue posible Actualiza el perfil",
                description="Error 404, User profile not found or deleted"
            )
            send_log_to_api(log)
            raise HTTPException(status_code=404, detail="User profile not found or deleted")
        return profile


    async def delete_user_profile(self, user_id: str):
        result = await self.collection.update_one(
            {"user_id": user_id, "state": True},  # Solo permite eliminar si el estado es True
            {"$set": {"state": False}}  # Marca el perfil como eliminado (estado False)
        )
        if result.matched_count == 0:
            log = LogRequest (
                application="Perfiles",
                level="high",
                className= "delete_user_profile",
                summary="No fue posible Eliminar el perfil",
                description="Error 404, User profile not found or already deleted"
            )
            send_log_to_api(log)
            raise HTTPException(status_code=404, detail="User profile not found or already deleted")
        
        return {"message": "User profile marked as deleted successfully"}

