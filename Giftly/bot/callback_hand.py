from bot import keyboards
from bot.utilits import text
from bot.send_gifts import sender
from Gamee import boxes, constants, lucky_bomb
from bot.config import dp, bot
from aiogram.types import LabeledPrice, FSInputFile
from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
import asyncio
from databases import database
from bot.utilits.hasher import *

class Input(StatesGroup):
    count_star = State()

@dp.callback_query(F.data.in_(["boxes", "tops", "support", "lucky_bomb", "use", "usew", "tower"]) | F.data.startswith("Box") | F.data.startswith("back") | F.data.startswith("deposit"))
async def handling(data, state):
    info = data.data
    if info == 'deposit':
        await bot.send_message(
            data.from_user.id,
            '💜💙 Выбери способ оплаты 💙💜',
            reply_markup=keyboards.tonorstars()
        )
    elif info == 'deposit_star':
        await data.message.edit_text(text =  '⭐⭐ Введите количество звезд для покупки (1к = 1 000) ⭐⭐')
        await state.set_state(Input.count_star)
    elif info == 'deposit_TON':
        hashik = encoder(str(data.from_user.id))
        await data.message.edit_text(text = 'Курс конвертации: 1 TON = 200⭐\n\nЕсли звезды не пришли обращайтесь в техподдержку @aidzensolo', reply_markup=keyboards.dep_btn(hashik))
    elif info == 'back_to_menu':
        info_1 = await database.select_user(data.from_user.id)
        await bot.edit_message_media(media=types.InputMediaPhoto(media=FSInputFile(r'C:\Users\Admin\Desktop\Giftly\photo\giftly.png')),
                                     chat_id=data.message.chat.id,
                                     message_id=data.message.message_id)
        await bot.edit_message_caption(chat_id=data.message.chat.id, message_id=data.message.message_id,
                                       caption=text.menu(info_1.user_id, info_1.name, info_1.balance_star, info_1.referals, info_1.play_win, info_1.time_register, info_1.referal_amount),
                                       reply_markup=keyboards.menu(),
                                       parse_mode="HTML")
    elif info == 'boxes' or info == 'back_to_box':
        await bot.edit_message_media(media=types.InputMediaPhoto(media=FSInputFile(r'C:\Users\Admin\Desktop\Giftly\photo\menu.png')), chat_id=data.message.chat.id,
                                     message_id=data.message.message_id)
        await bot.edit_message_caption(chat_id=data.message.chat.id, message_id=data.message.message_id,
                                       caption=text.boxes(),
                                       reply_markup=keyboards.boxes())
    elif info == 'lucky_bomb' or info == 'back_to_bomb':
        await bot.edit_message_caption(chat_id=data.message.chat.id, message_id=data.message.message_id,
                                       caption=text.lbomb_info(),
                                       reply_markup=keyboards.play('luckybomb'))
    elif info == 'tower' or info == 'back_to_tower':
        await bot.edit_message_caption(chat_id=data.message.chat.id, message_id=data.message.message_id,
                                       caption=text.lbomb_info(),
                                       reply_markup=keyboards.play('tower'))
    elif info == 'tops' or info == 'back_to_top':
        await data.message.edit_text(
            text='Выбери',
            reply_markup=keyboards.tops()
        )
    elif info == 'use':
        await data.answer('😐 Игра завершена 😐')
    elif info == 'usew':
        await data.answer('😐 Ячейка уже выбрана 😐')
    elif info == 'support':
        await data.message.edit_text(
            text=text.support_text(),
            reply_markup=keyboards.tops()
        )
    elif info.startswith('Box'):
        await bot.edit_message_media(
            media=types.InputMediaPhoto(media=FSInputFile(r'C:\Users\Admin\Desktop\Giftly\photo\giftly.png')),
            chat_id=data.message.chat.id,
            message_id=data.message.message_id)
        await bot.edit_message_caption(chat_id=data.message.chat.id, message_id=data.message.message_id,
                                       caption=text.open_box(info),
                                       reply_markup=keyboards.open_box(info),
                                       parse_mode="HTML")
    await data.answer()

@dp.callback_query(F.data == 'get_gifts')
async def get_gifts(data, state):
    info_pole = await state.get_data()
    gift_wins = [info_pole['cells'][x].split('_')[1] for x in info_pole['use_already']]
    await data.message.edit_text(
        text=f'Что будем делать {gift_wins}',
        reply_markup=keyboards.repl_take(gift_wins, 'luckybomb')
    )
    await state.clear()

@dp.callback_query(F.data.startswith('top'))
async def top(data):
    info = data.data
    info1 = info.split('_')[1]
    result = await database.top_users(info1)
    text_ans = f'Топ по {info1}\n\n'
    for num, user in enumerate(result):
        text_ans += f"{num + 1}. {user.user_name} - {user.play_win}\n"
    await data.message.edit_text(
        text=text_ans,
        reply_markup=keyboards.back('top')
    )

@dp.message(Input.count_star)
async def star_dep(message, state):
    if message.text.isdigit():
        prices = [LabeledPrice(label="XTR", amount=int(message.text))]
        await bot.send_invoice(
            chat_id = message.from_user.id,
            title = f'💜 Пополнение баланса',
            description = '⭐ После успешной оплаты кнопка внизу поменятся на чек. Для отмены нажми /cancel',
            payload = 'test',
            currency = 'XTR',
            prices = prices,
            start_parameter='vip1'
        )
        await state.clear()