from aiogram import Router
from handlers import main_router

start_router = Router()

start_router.include_routers(
    main_router,
)
