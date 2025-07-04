
from bot.config import dp, bot
from aiogram.filters import Command
from aiogram.types import FSInputFile, ReplyKeyboardRemove
from aiogram import F
from bot import keyboards
from bot.utilits import text
from databases import database
import asyncio

@dp.message(F.text == 'Я соглaсен ✅')
@dp.message(Command('cancel'))
@dp.message(Command('start'))
async def start(message, state):
    await state.clear()
    info = await database.select_user(message.from_user.id)
    if not info:
        photo = FSInputFile('photo/giftly.png')
        await database.insert_data(message.from_user.id, message.from_user.first_name,int((message.text)[10:]) if 'ref' in message.text else 0, message.from_user.username)
        await bot.send_photo(message.from_user.id, photo =  photo, caption = text.hello(), reply_markup = keyboards.hello())
        if 'ref' in message.text:
            info_ref = await database.select_user(int((message.text)[10:]))
            await bot.send_message(int((message.text)[10:]), f'💜 Новый реферал! @{message.from_user.username}')
            await database.update_user(user_id = int((message.text)[10:]),
                                  column = 'referals',
                                  value = info_ref.referals + 1
            )
    else:
        photo = FSInputFile('photo/menu.png')
        if message.text == 'Я соглaсен ✅':
            await message.answer('💙 Отлично! Приятной игры! 💜', reply_markup= ReplyKeyboardRemove())
        await bot.send_photo(message.from_user.id, photo=photo, caption=text.menu(info.user_id, info.name, info.balance_star, info.referals, info.play_win, info.time_register, info.referal_amount), reply_markup=keyboards.menu(), parse_mode='HTML')

@dp.pre_checkout_query()
async def test(query):
    info_old = await database.select_user(query.from_user.id)
    await database.update_user(user_id = query.from_user.id, column = 'balance_star', value= info_old.balance_star + query.total_amount)
    await query.answer(ok=True, text= '💙 Баланс пополнен 💜')
    await asyncio.sleep(1)
    await bot.send_message(query.from_user.id, text.menu(info_old.user_id, info_old.name, info_old.balance_star + query.total_amount, info_old.referals, info_old.play_win, info_old.time_register, info_old.referal_amount), reply_markup = keyboards.menu(), parse_mode="HTML")