from aiogram import F
from aiogram.fsm.state import State, StatesGroup

from Gamee import tower
from bot import keyboards
from bot.config import bot, dp


class GameStateTower(StatesGroup):
    playing = State()

@dp.callback_query(F.data.in_(['play_tower', 'play_towerA']))
async def tower_super(data, state):
    info = data.data
    print(info)
    com, mode = info.split('_')
    info_pole = await state.get_data()
    print(info_pole)
    if info_pole == {}:
        pole = tower.Game_tower()
        await state.set_state(GameStateTower.playing)
        await state.update_data(cells=pole)
        await state.update_data(use_already=[])
        await state.update_data(row=0)
        if mode == 'tower':
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