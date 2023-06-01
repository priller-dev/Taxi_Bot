from states import AuthState
from aiogram import Router
from aiogram.filters import Text
from aiogram.types import FSInputFile
from aiogram.types import Message

auth_router = Router()

# @auth_router.message()