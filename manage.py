from aiogram.webhook.aiohttp_server import (
    SimpleRequestHandler,
    setup_application,
)
from aiohttp.web import run_app
from aiohttp.web_app import Application
from config import conf
from db import db
from utils.tables import create_tables
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from main import main_router

async def on_startup(dispatcher: Dispatcher, bot: Bot):
    await db.connect()
    await create_tables()
    await bot.set_webhook(f"{conf.bot.BASE_URL}{conf.bot.BOT_PATH}")


def main():
    session = AiohttpSession()
    bot = Bot(conf.bot.TOKEN, session=session, parse_mode="HTML")

    dp = Dispatcher()  # noqa
    dp.include_router(main_router) # noqa
    dp.startup.register(on_startup) # noqa
    dp.shutdown.register(db.close) # noqa

    app = Application()

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(
        app, path=conf.bot.BOT_PATH
    )

    setup_application(app, dp, bot=bot)

    run_app(app, host=conf.bot.WEB_SERVER_HOST, port=conf.bot.WEB_SERVER_PORT)


if __name__ == '__main__':
    main()