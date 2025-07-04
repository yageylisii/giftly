import asyncio, ast

from aiogram import types

from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile

from Gamee import constants, boxes
from bot import keyboards
from bot.config import dp, bot
from bot.send_gifts import sender
from bot.utilits import text

class GameState(StatesGroup):
    playing = State()

@dp.callback_query(F.data.startswith('replacegift'))
@dp.callback_query(F.data.startswith('takegift'))
async def open_box(data):
    info = data.data
    print(info)
    command, giftc, mode = info.split('_')
    print(giftc)
    gifts = ast.literal_eval(giftc)
    if command == 'takegift':
        for gift in gifts:
            await sender.default_gift(data.from_user.id, constants.gift_default[gift])
        text = '💜 Подарок отправлен. Хорошей игры 💜'
    else:
        prices = 0
        for gift in gifts:
            price = constants.gift_price_by_id[gift]
            prices += price
        text = f'✅ Подарок обменян на {prices*1.2} ⭐'
    await data.message.edit_text(
        text=text,
        reply_markup=keyboards.open_box(f'box_{mode}') if mode not in ['luckybomb','luckybombA']  else keyboards.play('luckybombA'))

@dp.callback_query(F.data.startswith('cell'))
async def open_box(data, state):
    info_pole = await state.get_data()
    cells = info_pole.get("cells")
    text1 = text.cong_win(data.data)
    command, gift, num, mode = data.data.split('_')
    await data.message.edit_text(
        text=text1,
        reply_markup=keyboards.default_gift_choice(cells, True, gift,mode))
    await data.answer()
    await state.clear()

@dp.callback_query(F.data.startswith('open'))
async def open_box(data, state):
    name_box = data.data.split('_')[2].lower()
    result = await boxes.Game_NFT(data.from_user.id, name_box)
    print(result)
    if result == 'gifts_end':
        await bot.edit_message_media(
            media=types.InputMediaPhoto(media=FSInputFile(r'C:\Users\Admin\Desktop\Giftly\photo\lost_gift.png')),
            chat_id=data.message.chat.id,
            message_id=data.message.message_id)
        await bot.edit_message_caption(
            chat_id=data.from_user.id,
            message_id=data.message.message_id,
            caption=f'‼️ Кажется закончились NFT подарки, которые могут быть в боксе. Админ уже оповещен о проблеме. Загляни чуть позже',
            reply_markup=keyboards.open_box(data.data))
        return
    if data.message.photo != None:
        new_mes = await bot.send_message(data.from_user.id, text = '💜 Открываем...')
    else:
        await data.message.edit_text(text='💜 Открываем...')
        new_mes = data.message
    await asyncio.sleep(1.5)
    if result == 'game_lose':
        await bot.edit_message_text(
            chat_id = data.from_user.id,
            message_id=new_mes.message_id,
            text=f'💔 На этот раз в боксе ничего не оказалось. Но не расстраивайся — удача уже рядом! Попробуй открыть следующий! 💜',
            reply_markup=keyboards.open_after(data.data))
    elif result[1] == 'gifts_win_def':
        await new_mes.edit_text(
         text= f'💙💙 Поздравляем! 💙💙\n\nВ боксе был {result[0]} ({constants.gift_price_by_id[result[0]]} ⭐)\n\nВы можете вывести этот подарок себе в профиль ИЛИ обменять на звезды в боте на 20% больше.   ',
                reply_markup=keyboards.default_gift_choice([], True, result[0], name_box))
    elif result[1] == 'game_win':
        if type(result[0]) == list:
            await state.set_state(GameState.playing)
            await state.update_data(cells=result[0])
            textik = text.default_win_choice()
            keyboard = keyboards.default_gift_choice(result[0], mode = name_box)
            mode = None
            await new_mes.edit_text(text=textik, reply_markup=keyboard, parse_mode=mode)
        else:
            textik = text.nft_win(result[0])
            keyboard = None
            mode = "HTML"
            await new_mes.edit_text(text = textik, reply_markup=keyboard, parse_mode=mode)
            await asyncio.sleep(1.5)
            await bot.send_message(
                data.from_user.id,
                text=text.open_box(data.data[4:]),
                reply_markup=keyboards.open_box(data.data[4:])
            )
    await data.answer()