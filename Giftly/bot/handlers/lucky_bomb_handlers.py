from aiogram import F
from aiogram.fsm.state import StatesGroup, State

from Gamee import lucky_bomb
from bot import keyboards
from bot.config import bot, dp
from Gamee.constants import gift_price_by_id

class GameStateBomb(StatesGroup):
    playing = State()

@dp.callback_query(F.data.in_(['play_luckybomb', 'play_luckybombA']))
async def tower_super(data, state):
    info = data.data
    com, mode = info.split('_')
    info_pole = await state.get_data()
    if info_pole == {}:
        pole = lucky_bomb.Game_super()
        await state.set_state(GameStateBomb.playing)
        await state.update_data(
            cells=pole,
            use_already=[],
            mode = 'luckybomb'
            )
        if mode == 'luckybomb':
            await bot.send_message(
                data.from_user.id,
                text='Выбери33333333333333333333333333333333333333',
                reply_markup=keyboards.pole_bomb(pole)
            )
        else:
            await data.message.edit_text(text='Выбери33333333333333333333333333333333333333',
                reply_markup=keyboards.pole_bomb(pole))
    else:
        await data.answer('😐 Сначала закончи предыдущую игру 😐')

@dp.callback_query(F.data.startswith('bomb'))
async def tower_super(data, state):
    info_pole = await state.get_data()
    if info_pole["mode"] == 'luckybomb':
        com, num_cell = data.data.split("_")
        info_cell = info_pole['cells'][int(num_cell)]
        print(info_cell)
        if info_cell["status"] == 0:
            text = 'You lose3333333333333333333333333'
            info_pole['use_already'].append(info_cell["num"])
            await data.message.edit_text(text,reply_markup=keyboards.pole_bomb(info_pole['cells'], info_pole['use_already'], True))
            await state.clear()
            return
        if info_cell["status"] == 1:
            text = f'{info_cell["emodji"]} ({gift_price_by_id[info_cell["emodji"]]} ⭐) продолжим?3333333333333333333333333333333'
        elif info_cell["status"] == 2:
            text = f'You win a nft gift33333333333333333333333333333333'
        info_pole['use_already'].append(info_cell["num"])
        await state.update_data(use_already=info_pole['use_already'])
        await data.message.edit_text(text, reply_markup=keyboards.pole_bomb(info_pole['cells'], info_pole['use_already'], False))
    # else:
    #     com, cell, gift,row, num_cell = data.data.split('_')
    #     row_now = info_pole['row']
    #     if row_now == int(row):
    #         print(data.data.split('_'))
    #         if int(cell) == 0:
    #             text = 'You lose3333333333333333333333333'
    #             info_pole['use_already'].append(int(num_cell))
    #             await data.message.edit_text(text, reply_markup=keyboards.pole_bomb(info_pole['cells'],
    #                                                                                 info_pole['use_already'], True, 'play_towerA'))
    #             await state.clear()
    #             return
    #         if int(cell) == 1:
    #             text = f'{gift} ({gift_price_by_id[gift]} ⭐) продолжим?3333333333333333333333333333333'
    #             info_pole['use_already'].append(int(num_cell))
    #             await state.update_data(row = row_now + 1, use_already = info_pole['use_already'])
    #             await data.message.edit_text(text, reply_markup=keyboards.pole_bomb(info_pole['cells'],
    #                                                                                 info_pole['use_already'], False, 'play_towerA'))
    #     else:
    #         await data.answer(f'выбери ячейку на {row_now + 1} этаже')