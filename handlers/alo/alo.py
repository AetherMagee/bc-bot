from aiogram import types


async def alo(message: types.Message) -> None:
    await message.answer('📞 Alo, я на связи')
