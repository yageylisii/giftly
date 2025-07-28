import asyncio

from aiogram.types import LabeledPrice, FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram import F, types

from bot import keyboards
from bot.config import dp, bot
from databases import database
from bot.utils.hasher import *
from bot.utils import text_game

class Input(StatesGroup):
    count_star = State()
    casino_bet = State()

@dp.callback_query(F.data.in_(["use", "usew"]) | F.data.startswith("floor"))
async def handling_1(data):
    info = data.data
    if info == 'use':
        await data.answer('⚠️ Игра завершена ⚠️')
    elif info == 'usew':
        await data.answer('⚠️ Ячейка уже выбрана ⚠️')
    elif info.startswith('floor'):
        com, floor = info.split('_')
        ans = text_game.flour(floor)
        await data.answer(ans)

@dp.callback_query(F.data.in_(["boxes", "tops", "support", "lucky_bomb", "tower", "cas_sport", "tasks", "referals", "bet_replace"]) | F.data.startswith("Box") | F.data.startswith("back") | F.data.startswith("deposit"))
async def handling_2(data, state):

    info = data.data
    user_id = data.from_user.id

    if info == 'deposit':
        await data.message.delete()
        await data.message.answer(
            text = '💜💙 Выбери способ оплаты 💙💜',
            reply_markup=keyboards.tonorstars()
        )
    elif info == 'deposit_star':
        await data.message.edit_text(
            text = '⭐⭐ Введите количество звезд для покупки (1к = 1 000) ⭐⭐',
            reply_markup=keyboards.tonorstars()
        )
        await state.set_state(Input.count_star)
    elif info == 'deposit_TON':
        hashik = encoder(str(data.from_user.id))
        await data.message.edit_text(
            text = 'Курс конвертации: 1 TON = 200⭐\n\nЕсли звезды не пришли обращайтесь в техподдержку @aidzensolo',
            reply_markup=keyboards.dep_btn(hashik)
        )
    elif info == 'back_to_menu':
        await data.message.delete()
        await data.message.answer_photo(
            photo = FSInputFile('bot/photo/profile.png'),
            caption=await text_game.menu(user_id),
            reply_markup=keyboards.menu(),
        )
    elif info == 'boxes' or info == 'back_to_box':
        await data.message.edit_media(media=types.InputMediaPhoto(media=FSInputFile('bot/photo/gift_boxes.png')))
        await data.message.edit_caption(
            caption=text_game.boxes(),
            reply_markup=keyboards.boxes(),
        )
    elif info == 'lucky_bomb':
        # await data.message.edit_media(media=types.InputMediaPhoto(media=FSInputFile('bot/photo/gift_boxes.png')))
        await data.message.edit_caption(
            caption=text_game.lbomb_info(),
            reply_markup=keyboards.play('luckybomb'),
        )
    elif info == 'back_to_luckybomb':
        await data.message.delete()
        await data.message.answer_photo(
            photo=FSInputFile('bot/photo/profile.png'),
            caption=text_game.lbomb_info(),
            reply_markup=keyboards.play('luckybomb'),
        )

    elif info == 'tower' or info == 'back_to_tower':
        await data.message.delete()
        await data.message.answer(
            text=text_game.tower_info(),
            reply_markup=keyboards.play('tower')
        )

    elif info == 'tops':
        await data.message.delete()
        await data.message.answer(
            text=text_game.top_choice(),
            reply_markup=keyboards.tops()
        )
    elif info == 'back_to_top':
        await data.message.edit_text(
            text=text_game.top_choice(),
            reply_markup=keyboards.tops()
        )
    elif info == 'cas_sport' or info == 'back_to_casinosport':
        user = await database.select_user(user_id)
        await data.message.edit_media(media=types.InputMediaPhoto(media=FSInputFile('bot/photo/casino_sport.png')))
        await data.message.edit_caption(
            caption=text_game.choice_casino(),
            reply_markup=keyboards.casino_sport(user.bet_casino),
        )
    elif info == 'support':
        await data.message.edit_media(media=types.InputMediaPhoto(media=FSInputFile('bot/photo/support.png')))
        await data.message.edit_caption(
            caption=text_game.support_text(),
            reply_markup=keyboards.back('menu'),
        )

    elif info == 'referals':
        user = await database.select_user(user_id)
        await data.message.edit_media(media=types.InputMediaPhoto(media=FSInputFile('bot/photo/referal_programm.png')))
        await data.message.edit_caption(
            caption=text_game.referal_program(user_id, user),
            reply_markup=keyboards.back('menu'),
        )
    elif info == 'tasks':
        await data.message.delete()
        tasks = await database.select_tasks()
        user = await database.select_user(user_id)
        text = f'📋 <b>Задания</b>\n'
        for x in tasks:
            text += text_game.task_info(x, user)
        await bot.send_message(
            chat_id=user_id,
            text=text,
            reply_markup=keyboards.task(tasks),
        )
    elif info == 'bet_replace':
        await data.message.edit_caption(
            caption='Напиши ставку',
            reply_markup=keyboards.back('casinosport'),
        )
        await state.set_state(Input.casino_bet)
        await state.update_data(message_id = data.message.message_id)
        await asyncio.sleep(180)
        await state.set_state(None)
    elif info.startswith('Box'):
        await data.message.edit_caption(
            caption=text_game.open_box(info),
            reply_markup=keyboards.open_box(info),
        )
@dp.callback_query(F.data == 'get_gifts')
async def get_gifts(data, state):
    info_pole = await state.get_data()
    gift_wins = [info_pole['cells'][x]['gift'] for x in info_pole['use_already']]
    await data.message.edit_text(
        text=f'Что будем делать {gift_wins}',
        reply_markup=keyboards.repl_take(gift_wins, info_pole['mode'])
    )
    await state.clear()

@dp.callback_query(F.data.startswith('top'))
async def top(data):
    info = data.data
    _, info1 = info.split('_')
    result = await database.top_users(info1)
    if info1 == 'win':
        text_ans = '🏆 Самые везучие\n\n'
        for num, user in enumerate(result):
            text_ans += f"{num + 1}. {user.user_name} - {user.play_win} ⭐\n"
    elif info1 == 'referals':
        text_ans = '💜 Самые общительные\n\n'
        for num, user in enumerate(result):
            text_ans += f"{num + 1}. {user.user_name} - {user.referals}\n"
    await data.message.edit_text(
        text=text_ans,
        reply_markup=keyboards.back('top')
    )
@dp.message(Input.casino_bet)
async def casino_bet(message, state):

    user_data = await state.get_data()
    user_id = message.from_user.id

    if message.text.isdigit():
        if int(message.text) > 10:
            await bot.edit_message_caption(
                chat_id = message.from_user.id,
                message_id = user_data['message_id'],
                caption = f'💜 Ставки для режима Casino Sport изменены на {message.text} ⭐',
                reply_markup = keyboards.casino_sport(message.text),
            )
            await database.update_user(user_id, 'bet_casino', int(message.text))
            await state.clear()

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