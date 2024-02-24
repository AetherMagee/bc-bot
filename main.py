from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from static.tokens import *
from handlers import *


async def main():
    bot = Bot(TELEGRAM_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.message.register(alo, Command("alo"))
    dp.message.register(cum, Command("cum"))
    dp.message.register(exchange, Command("exchange"))
    dp.message.register(layout_command, Command("layout"))
    dp.message.register(stats, Command("stats"))

    @dp.callback_query(F.data.in_({'back', 'week', 'month'}))
    async def stats_callback_(call: CallbackQuery) -> None:
        await stats_callback(call)

    @dp.callback_query(F.data == "delete")
    async def delete_currency_message_(call: CallbackQuery) -> None:
        await delete_currency_message(call)

    @dp.message()
    async def non_command(message: Message) -> None:
        await log_message(message)
        await convert_currency(message)

    # Schedule removing old stats database records
    scheduler = AsyncIOScheduler()
    scheduler.add_job(delete_old_records, trigger="interval", days=1)
    scheduler.start()

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
