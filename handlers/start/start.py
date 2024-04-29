from aiogram.types import Message


async def start(message: Message) -> None:
    await message.reply(
        "<b>привет!</b> я няшный бкшный фемботик, немножко умный и полезный\n\n"
        "<b>список доступных команд:</b>\n"
        "/stats — статистика сообщений за день, неделю и месяц\n"
        "/exchange — получает актуальный на текущий момент курс доллара/евро относительно рубля, или указанной вами пары, например: <i>\"/еxchange USD EUR\"</i>\n"
        "/remind [<i>время</i>] [<i>текст</i>] — устанавливает напоминание для вас. сообщение будет отправлено по истечении заданного вами времени, например: <i>\"/rеmind 5h пополнить баланс аéзы\"</i>\n"
        "/layout — меняет раскладку текста в сообщении между английским и русским языком\n\n"
        "проверить, что бот в онлайне можно с помощью команды /alo\n"
        "<b>made with ❤️ by ki</b>"
    )
