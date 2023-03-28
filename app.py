import asyncio
import os
import sys

from aiogram import executor

from loader import dp, bot



async def on_startup(dp):
    pass
    # Устанавливаем дефолтные команды
    # await set_default_commands(dp)
    # await create_db()
    #
    # # Уведомляет про запуск
    # await on_startup_notify(dp)


if __name__ == '__main__':
    if (sys.platform.startswith('win')
            and sys.version_info[0] == 3
            and sys.version_info[1] >= 8):
        policy = asyncio.WindowsSelectorEventLoopPolicy()
        asyncio.set_event_loop_policy(policy)

    executor.start_polling(dp, on_startup=on_startup)
