from aiogram import F
from aiogram.fsm.state import State, StatesGroup

from Game import tower
from bot import keyboards
from bot.config import bot, dp
from bot.utils.constants import gift_price_by_id, price_box
from bot.utils.upgrade_balance import upgrade_balance
from databases.database import select_user


class GameStateTower(StatesGroup):
    playing = State()

@dp.callback_query(F.data == 'play_tower')
async def tower_super(data, state):

    info = data.data
    user_id = data.from_user.id
    com, mode = info.split('_')
    info_pole = await state.get_data()
    user_data = await select_user(user_id)

    if user_data.balance_star >= price_box[mode]:
        if info_pole == {}:

            await upgrade_balance(user_data, price_box[mode] * -1)

            field = tower.Game_tower()

            await state.set_state(GameStateTower.playing)
            await state.update_data(
                cells=field,
                use_already=[],
                row=0,
                mode = mode
            )

            text = '💥 Пройди 5 этажей ! NFT и подарки уже ждут тебя 💜'
            keyboard = keyboards.pole_bomb(field, mode = mode)

            if data.message.photo != None:
                await data.message.delete()
                await data.message.answer(text, keyboard)
            else:
                await data.message.edit_text(text = text, reply_markup=keyboard)
        else:
            await data.answer('⚠️ Сначала закончи предыдущую игру ⚠️')
    else:
        await data.answer('⚠️ Не хватает баланса ⚠️')
        await data.message.answer(
            text='💜💙 Выбери способ оплаты 💙💜',
            reply_markup=keyboards.tonorstars()
        )

@dp.callback_query(F.data.startswith('door'), GameStateTower.playing)
async def tower_super(data, state):

    info_pole = await state.get_data()
    com, num_cell = data.data.split("_")
    info_cell = info_pole['cells'][int(num_cell)]
    row_now = info_pole['row']

    if row_now == info_cell['row']:
        if info_cell['status'] == 0:
            text = '💀 Не повезло! Мина прямо под ногами\n\n 🎁 Подарки не достаются тем, кто спешит. Попробуешь снова?'
            info_pole['use_already'].append(int(num_cell))
            await data.message.edit_text(text, reply_markup=keyboards.pole_bomb(info_pole['cells'],
                                                                                info_pole['use_already'], True, mode = 'tower'))
            await state.clear()
        elif info_cell['status'] == 1:
            info_pole['use_already'].append(int(num_cell))
            if info_cell['row'] != 4:
                text = f'{info_cell["emodji"]} ({gift_price_by_id[info_cell["emodji"]]} ⭐) продолжим?3333333333333333333333333333333'
                await state.update_data(row = row_now + 1, use_already = info_pole['use_already'])
                await data.message.edit_text(text, reply_markup=keyboards.pole_bomb(info_pole['cells'],
                                                                                info_pole['use_already'], False, mode = 'tower'))
            else:
                text = f'бля как ты это сделал сука. нфт твой бля'
                await state.update_data(use_already=info_pole['use_already'])
                await data.message.edit_text(text, reply_markup=keyboards.pole_bomb(info_pole['cells'],
                                                                                    info_pole['use_already'], True,
                                                                                    mode='tower'))
    else:
        await data.answer(f'⚠️ Выбери ячейку на {row_now + 1} этаже ⚠️')