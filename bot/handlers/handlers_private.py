from bot.config import dp, bot
from aiogram.filters import Command
from aiogram.types import FSInputFile, ReplyKeyboardRemove
from aiogram import F
from bot import keyboards
from bot.utils import text_game
from databases import database
import asyncio

@dp.message(F.text == 'Я соглaсен ✅')
@dp.message(Command('cancel'))
@dp.message(Command('start'))
async def start(message, state):
    user_id = message.from_user.id
    info = await database.select_user(user_id)
    if not info:
        await database.insert_data(
            user_id = user_id,
            name = message.from_user.first_name,
            referer_id = int((message.text)[10:]) if 'ref' in message.text else 0,
            user_name = message.from_user.username
        )
        await bot.send_photo(message.from_user.id, photo =  FSInputFile('bot/photo/profile.png'), caption = text_game.hello(), reply_markup = keyboards.hello())
    else:
        print(message)
        if message.text == 'Я соглaсен ✅':

            info_ref = await database.select_user(info.referer_id)
            await bot.send_message(info.referer_id, f'💜 Новый реферал! @{info.referer_id}')
            await database.update_user(user_id=info.referer_id,column='referals',value=info_ref.referals + 1)
            await message.answer('💙 Отлично! Приятной игры! 💜', reply_markup= ReplyKeyboardRemove())

        await message.answer_photo(
            photo=FSInputFile('bot/photo/profile.png'),
            caption=await text_game.menu(user_id),
            reply_markup=keyboards.menu(),
            parse_mode="HTML"

        )

@dp.pre_checkout_query()
async def test(query):
    info_old = await database.select_user(query.from_user.id)
    await database.update_user(user_id = query.from_user.id, column = 'balance_star', value= info_old.balance_star + query.total_amount)
    await query.answer(ok=True, text= '💙 Баланс пополнен 💜')
    await asyncio.sleep(1)
    await bot.send_message(query.from_user.id, text_game.menu(info_old), reply_markup = keyboards.menu(), parse_mode="HTML")
