import random

from aiogram import F
from aiogram.fsm.state import StatesGroup, State

from Game import lucky_bomb
from bot import keyboards
from bot.config import dp
from bot.utils.constants import price_box
from bot.utils.upgrade_balance import upgrade_balance
from databases.database import select_user, select_gift
from bot.utils import text_game, send_gifts



class GameStateBomb(StatesGroup):
    playing = State()

@dp.callback_query(F.data == 'play_luckybomb')
async def luckybomb_mode_start(data, state):

    _, mode = data.data.split('_')
    user_id = data.from_user.id
    info_pole = await state.get_data()
    user_data = await select_user(user_id)

    if user_data.balance_star >= price_box[mode]:
        if info_pole == {}:
            if await send_gifts.gift_checker(['middle']):

                await upgrade_balance(user_data, price_box[mode] * -1)

                field = lucky_bomb.Game_super()
                await state.set_state(GameStateBomb.playing)
                await state.update_data(
                    cells=field,
                    use_already=[],
                    mode = mode
                    )

                text = '💥 Новое поле — будь осторожен! NFT и подарки уже ждут тебя 💜'
                keyboard = keyboards.pole_bomb(field)

                if data.message.photo != None:
                    await data.message.delete()
                    await data.message.answer(
                        text = text,
                        reply_markup = keyboard
                    )
                else:
                    await data.message.edit_text(
                        text = text,
                        reply_markup = keyboard
                    )
            else:
                await data.answer('‼️ Кажется закончились NFT подарки')
        else:
            await data.answer('⚠️ Сначала закончи предыдущую игру ⚠️')
    else:
        await data.answer('⚠️ Не хватает баланса ⚠️')
        await data.message.delete()
        await data.message.answer(
            text='💜💙 Выбери способ оплаты 💙💜',
            reply_markup=keyboards.tonorstars()
        )

@dp.callback_query(F.data.startswith('bomb'), GameStateBomb.playing)
async def luckybomb_mode(data, state):

    info_pole = await state.get_data()
    com, num_cell = data.data.split("_")
    info_cell = info_pole['cells'][int(num_cell)]

    if info_cell["status"] == 0:
        await state.clear()
        text = text_game.bomb_game('lose', info_cell)
    elif info_cell["status"] == 1:
        text = text_game.bomb_game('default', info_cell)
    else:
        await state.clear()
        text = 'NFT! Игра завершена'
        gift_nft = random.choice(await select_gift('middle'))
        await send_gifts.send_nft_gift(gift_nft, data.from_user.id, mode = 'bombs')

    if info_cell["status"] in [0, 2]:
        await data.message.edit_text(
            text=text,
            reply_markup=keyboards.pole_bomb(
                pole=info_pole['cells'],
                use_already=info_pole['use_already'],
                lost=True,
                mode='luckybomb'
            )
        )

    else:
        info_pole['use_already'].append(info_cell["num"])
        await state.update_data(use_already=info_pole['use_already'])

        await data.message.edit_text(
            text=text,
            reply_markup=keyboards.pole_bomb(
                pole=info_pole['cells'],
                use_already=info_pole['use_already'],
                mode='luckybomb'
            )
        )

