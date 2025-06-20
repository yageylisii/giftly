import keyboards, text
from Gamee import game, constants
from config import dp, bot
from aiogram.types import LabeledPrice, FSInputFile
from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
import asyncio
from databases import database
import ton_dep


class Input(StatesGroup):
    count_star = State()
class Deposit_TON(StatesGroup):
    deposit = State()
class GameState(StatesGroup):
    playing = State()

@dp.callback_query(F.data.in_(["boxes", "tops", "support"]) | F.data.startswith("Box") | F.data.startswith("back") | F.data.startswith("deposit"))
async def handling(data, state):
    info = data.data
    if info == 'deposit':
        await bot.send_message(
            data.from_user.id,
            '💜💙 Выбери способ оплаты 💙💜',
            reply_markup=keyboards.tonorstars()
        )
        await data.answer()
    elif info == 'deposit_star':
        await data.message.edit_text(text =  '⭐⭐ Введите количество звезд для покупки (Н. 1000, 1к, 10) ⭐⭐')
        await state.set_state(Input.count_star)
    elif info == 'deposit_TON':
        wallet_free = await database.select_wallet('select')
        user = await database.select_wallet('check', data.from_user.id)
        if user == []:
            await data.message.edit_text(text = f'‼️ Переведите ТОНЫ на адрес в течение 10 МИНУТ, в противном случае коины не поступят на баланс‼️\n\n{wallet_free[0].wallet_name}\n\nПосле оплаты дождитесь подтверждения на блокчейне и нажмите на кнопку "Оплатил"\n\nКурс конвертации: 1 TON = 200⭐\n\nЕсли коины все же не пришли обращайтесь в техподдержку @aidzensolo', reply_markup=keyboards.proverka_depa())
            await database.update_wallet(wallet_free[0].wallet_name, 1, data.from_user.id)
            await asyncio.sleep(300)
            await database.update_wallet(wallet_free[0].wallet_name, 0, 0)
            await data.message.edit_text(text = 'Кошелек оплаты устарел, для оплаты вызови новый', reply_markup=keyboards.tonorstars())
        else:
            await data.answer('❌ Заверши предыдущую оплату')
    elif info == 'back_to_menu':
        info_1 = await database.select_user(data.from_user.id)
        await bot.edit_message_media(media=types.InputMediaPhoto(media=FSInputFile('photo/giftly.png')),
                                     chat_id=data.message.chat.id,
                                     message_id=data.message.message_id)
        await bot.edit_message_caption(chat_id=data.message.chat.id, message_id=data.message.message_id,
                                       caption=text.menu(info_1.user_id, info_1.name, info_1.balance_star, info_1.referals, info_1.play_win, info_1.time_register, info_1.referal_amount),
                                       reply_markup=keyboards.menu(),
                                       parse_mode="HTML")
    elif info == 'boxes' or info == 'back_to_box':
        await bot.edit_message_media(media=types.InputMediaPhoto(media=FSInputFile('photo/menu.png')), chat_id=data.message.chat.id,
                                              message_id=data.message.message_id)
        await bot.edit_message_caption(chat_id=data.message.chat.id, message_id=data.message.message_id,
                                                caption=text.boxes(),
                                                reply_markup=keyboards.boxes())
    elif info == 'tops' or info == 'back_to_top':
        await data.message.edit_text(
            text='Выбери',
            reply_markup=keyboards.tops()
        )
    elif info == 'support':
        await data.message.edit_text(
            text='Выбери',
            reply_markup=keyboards.tops()
        )
    elif info.startswith('Box'):
        await bot.edit_media(
            caption=text.open_box(info),
            reply_markup=keyboards.open_box(info)
        )
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
@dp.callback_query(F.data == 'dep_true')
async def dep_true(data):
    answer = await ton_dep.checker(data.from_user.id)
    if answer != 'dep_unknown':
        info_old = await database.select_user(data.from_user.id)
        await database.update_user(user_id=data.from_user.id, column='balance_star',
                                   value=info_old.balance_star + sum(answer)*200)
        text = f'💜 Нашли платеж {sum(answer)} TON.\n\n{sum(answer)*200} ⭐ зачислены на баланс\n\nБаланс: {info_old.balance_star + sum(answer)*200} ⭐'
        await data.message.edit_text(
            text=text,
            reply_markup=keyboards.tonorstars())
        await data.answer()
    else:
        text = '💔 Перевод не найден'
        await data.answer(text=text)

@dp.callback_query(F.data.startswith('replace_gift')) #ВАЖНО
@dp.callback_query(F.data.startswith('take_gift'))
async def open_box(data):
    info = data.data
    if info.startswith('take_gift'):
        text = '💜 Подарок отправлен. Хорошей игры 💜'
        await game.send_default_gift(data.from_user.id, info.split('_')[2])
    else:
        price = constants.gift_price_by_id[info.split('_')[2]]
        text = f'Подарок обменян на {price} ⭐'
    await data.message.edit_text(
        text=text,
        reply_markup=keyboards.open_box('box_default'))

@dp.callback_query(F.data.startswith('cell'))
async def open_box(data, state):
    info_pole = await state.get_data()
    cells = info_pole.get("cells")
    text1 = text.cong_win(data.data)
    await data.message.edit_text(
        text=text1,
        reply_markup=keyboards.default_gift_choice(cells, True, data.data.split('_')[1]))
    await data.answer()
    await state.clear()

@dp.callback_query(F.data.startswith('open'))
async def open_box(data, state):
    name_box = data.data.split('_')[2].lower()
    result = await game.Game(data.from_user.id, name_box)
    if result == 'gifts_end':
        await data.message.edit_text(
            text=f'‼️ Кажется закончились NFT подарки в боте, админ уже оповещен о проблеме. Загляни чуть позже',
            reply_markup=keyboards.back('box'))
        return
    await data.message.edit_text(text = '💜 Открываем...')
    await asyncio.sleep(1)
    if not result:
        await data.message.edit_text(text=f'💔 На этот раз в боксе ничего не оказалось.Но не расстраивайся — удача уже рядом! Попробуй открыть следующий! 💜',reply_markup=keyboards.open_after(data.data))
    elif result == 'default':
        res = game.random_default_gift()
        await state.set_state(GameState.playing)
        await state.update_data(cells=res)
        await data.message.edit_text(
            text=f'💙 Тебе выпал неуникальный подарок, в ячейках спрятаны подарки разной стоимости (15⭐ - 100⭐). Выбери ячейку, чтобы получить ИЛИ обменять подарок.',
            reply_markup=keyboards.default_gift_choice(res))
    else:
        if name_box == 'default':
            await data.message.edit_text(text= f'💙💙 Поздравляем! 💙💙\n\nВ боксе был {result}\n\n‼️ ВАЖНО! Подарок нельзя конвертировать в звезды из-за особенности телеграма ‼️  ',reply_markup=keyboards.default_gift_choice([], True, result[1]))
        else:
            await data.message.edit_text(text = f'💜💜 Поздравляем! 💜💜\n\nВ боксе был NFT подарок <a href="t.me/nft/{result.name}">{result.name}</a> — он уже отправлен на ваш аккаунт. Наслаждайтесь!', parse_mode="HTML")
            await asyncio.sleep(1.5)
            await bot.send_message(
                data.from_user.id,
                text=text.open_box(data.data[4:]),
                reply_markup=keyboards.open_box(data.data[4:])
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