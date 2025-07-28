from aiogram import F
from aiogram.enums import ChatMemberStatus
from aiogram.types import CallbackQuery

from bot.config import dp, channel


@dp.callback_query(F.data.startswith('check'))
async def check_subscription(callback: CallbackQuery):
    user_id = callback.from_user.id
    print(callback.data)
    # try:
    #     member = await callback.bot.get_chat_member(channel, user_id)
    # except Exception:
    #     await callback.answer("🚫 Не удалось проверить подписку", show_alert=True)
    #     return
    #
    # if member.status == ChatMemberStatus.MEMBER:
    #     await callback.message.edit_text("✅ Вы подписаны! Добро пожаловать 🎉")
    # else:
    #     await callback.answer("❌ Вы не подписаны на канал", show_alert=True)