import asyncio, ast

from aiogram import types

from aiogram import F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import FSInputFile

from Game import boxes
from bot import keyboards
from bot.config import dp, bot
from bot.utils import text_game, send_gifts, constants
from bot.utils.constants import price_box
from bot.utils.upgrade_balance import upgrade_balance
from databases.database import select_user


class GameState(StatesGroup):
    playing = State()

@dp.callback_query(F.data.startswith('replacegift'))
@dp.callback_query(F.data.startswith('takegift'))
async def repl_and_take(data):
    info = data.data
    command, giftc, mode = info.split('_')
    gifts = ast.literal_eval(giftc)
    if command == 'takegift':
        for gift in gifts:
            await send_gifts.default_gift(data.from_user.id, constants.gift_default[gift])
        text = '💜 Подарок отправлен. Хорошей игры 💜'
    else:
        prices = 0
        for gift in gifts:
            price = constants.gift_price_by_id[gift]
            prices += price

        user_data = await select_user(data.from_user.id)
        await upgrade_balance(user_data, prices*1.2)

        text = f'✅ Подарок обменян на {prices*1.2} ⭐'
    await data.message.edit_text(
        text=text,
        reply_markup=keyboards.open_box(f'box_{mode}') if mode not in ['luckybomb', 'tower']  else keyboards.play(mode)
    )

@dp.callback_query(F.data.startswith('cell'))
async def open_cell(data, state):
    info_pole = await state.get_data()
    cells = info_pole.get("cells")
    text = text_game.cong_win(data.data)
    command, gift, num, mode = data.data.split('_')
    await data.message.edit_text(
        text=text,
        reply_markup=keyboards.default_gift_choice(cells, True, gift,mode))
    await data.answer()
    await state.clear()

@dp.callback_query(F.data.startswith('open'))
async def open_box(data, state):

    name_box = data.data.split('_')[2].lower()
    user_id = data.from_user.id
    user_data = await select_user(user_id)

    if user_data.balance_star >= price_box[name_box]:
        result = await boxes.Game_NFT(user_id, name_box)
        if result == 'gifts_end':
            await bot.edit_message_media(
                media=types.InputMediaPhoto(media=FSInputFile('bot/photo/lost_gift.png')),
                chat_id=data.message.chat.id,
                message_id=data.message.message_id)
            return await bot.edit_message_caption(
                chat_id=data.from_user.id,
                message_id=data.message.message_id,
                caption=f'‼️ Кажется закончились NFT подарки, которые могут быть в боксе. Админ уже оповещен о проблеме. Загляни чуть позже',
                reply_markup=keyboards.open_after(data.data))

        await upgrade_balance(user_data, price_box[name_box]*-1)

        if data.message.photo != None:
            await data.message.delete()
            new_mes=await data.message.answer(text = '💜 Открываем...')
        else:
            await data.message.edit_text(text='💜 Открываем...')
            new_mes = data.message

        await asyncio.sleep(1.5)

        if result[1] == 'game_lose':
            new_text = text_game.cong_win_box(result[1],result[0])
            keyboard = keyboards.open_after(data.data)
        elif result[1] == 'game_win_def':
            new_text = text_game.cong_win_box(result[1], result[0])
            keyboard = keyboards.default_gift_choice([], True, result[0], name_box)
        elif result[1] == 'game_win_prem':
            new_text = text_game.cong_win_box(result[1], result[0])
            keyboard = keyboards.open_after(data.data)
        elif result[1] == 'game_win_list':

            await state.set_state(GameState.playing)
            await state.update_data(cells=result[0])

            new_text = text_game.cong_win_box(result[1], result[0])
            keyboard = keyboards.default_gift_choice(result[0], mode = name_box)
        elif result[1] == 'game_win':
            new_text = text_game.cong_win_box(result[1], result[0])
            keyboard = None
            await bot.send_message(
                    chat_id = user_id,
                    text='Продолжим?',
                    reply_markup=keyboards.open_after(data.data)
                )

        await new_mes.edit_text(
            text= new_text,
            reply_markup=keyboard,
            parse_mode='HTML'
        )

        await data.answer()
    else:
        await data.answer('⚠️ Не хватает баланса ⚠️')
        await data.message.delete()
        await data.message.answer(
            text='💜💙 Выбери способ оплаты 💙💜',
            reply_markup=keyboards.tonorstars()
        )