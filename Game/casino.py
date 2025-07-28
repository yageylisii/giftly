import asyncio

from aiogram.fsm.state import StatesGroup, State

from bot.utils import constants
from bot.config import bot
from bot.utils.upgrade_balance import upgrade_balance


class GameStateCasino(StatesGroup):
    playing = State()

async def Game_create(state, mode):
    existing_data = await state.get_data()

    if existing_data:
        return {'status': False, 'description': "Игра уже создана"}

    emoji = constants.game_emodji.get(mode)
    if not emoji:
        return {'status': False, 'description': "Неверный режим игры"}

    await state.set_state(GameStateCasino.playing)
    await asyncio.sleep(4)
    await state.update_data(
        moves_bot=[],
        moves_player=[],
        mode=constants.game_emodji[mode],
        is_bot=True,
        round=0,
        name = mode
    )

    return {'status': True, 'description': 'Игра создана'}

async def step_bot(state, player, user_id, result = None):
    data = await state.get_data()
    if player == 'bot':
        casinores = await bot.send_dice(
            chat_id=user_id,
            emoji=data['mode']
        )
        data['moves_bot'].append(casinores.dice.value)
        is_bot = False
        result = casinores
        await asyncio.sleep(4)
    else:
        data['moves_player'].append(result.dice.value)
        data['round'] += 1
        is_bot = True

    new_state = await state.update_data(
        moves_bot=data['moves_bot'],
        moves_player=data['moves_player'],
        mode=data['mode'],
        is_bot=is_bot,
        round=data['round']
    )
    if is_bot: await asyncio.sleep(4)
    return {'status': True, 'info_field': new_state, 'description': result.dice.value}

async def game_result(data:dict, user_data, profit):
    mode = data['mode']
    sum_bot = sum(constants.point_and_value[mode][x][0] for x in data['moves_bot'])
    sum_player= sum(constants.point_and_value[mode][x][0] for x in data['moves_player'])
    textik = f'💥 Счет: {sum_bot} : {sum_player} 💥\n\n'
    if sum_player > sum_bot:
        await upgrade_balance(user_data, profit*2)
        textik += f'💜 Вы выиграли 💜\n(+{user_data.bet_casino})'
        result = 'win'
    elif sum_player < sum_bot:
        textik += '💔 Вы проиграли'
        result = 'lose'
    else:
        await upgrade_balance(user_data, profit)
        textik += 'Ничья! Ставка возвращена!'
        result = 'draw'
    return textik, result
