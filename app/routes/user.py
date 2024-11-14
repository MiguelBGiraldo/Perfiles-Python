from fastapi import APIRouter, Depends, HTTPException
from ..models.user import UserProfile
from ..database import db  # Asegúrate de que `db` esté conectado a la colección de MongoDB
from ..controllers.user_controller import UserController

router = APIRouter()
user_controller = UserController(db["user_profiles"])

# Crear un perfil de usuario
@router.post("/api/profiles", response_model=UserProfile)
async def create_user_profile(profile: UserProfile):
    return await user_controller.create_user_profile(profile)

# Obtener un perfil de usuario por ID
@router.get("/api/profiles/{user_id}", response_model=UserProfile)
async def get_user_profile(user_id: str):
    return await user_controller.get_user_profile(user_id)

# Obtener todos los perfiles de usuario
@router.get("/api/profiles", response_model=list[UserProfile])
async def get_all_user_profiles():
    return await user_controller.get_all_user_profiles()

# Actualizar un perfil de usuario
@router.put("/api/profiles/{user_id}", response_model=UserProfile)
async def update_user_profile(user_id: str, profile: UserProfile):
    return await user_controller.update_user_profile(user_id, profile)

# Eliminar un perfil de usuario
@router.delete("/api/profiles/{user_id}")
async def delete_user_profile(user_id: str):
    return await user_controller.delete_user_profile(user_id)
