from bot.utils.constants import *
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def hello():
    return ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Я соглaсен ✅")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
def menu():
    builder = InlineKeyboardBuilder()
    builder.button(text = '🎁 Gift Boxes', callback_data='boxes')
    builder.button(text='💣 Lucky Bomb', callback_data='lucky_bomb')
    builder.button(text='🎰 Casino Sport', callback_data='cas_sport')
    builder.button(text='🗼 Tower', callback_data='tower')
    builder.button(text = '💙 Пополнить 💙', callback_data='deposit')
    builder.button(text='💜 Топы 💜', callback_data='tops')
    builder.button(text='⁉️ FAQ', callback_data='support')
    builder.button(text='📃 Задания', callback_data='tasks')
    builder.button(text='👥 Реферальная программа', callback_data='referals')
    builder.adjust(2,2,1,1,2,1)
    return builder.as_markup()

def boxes():
    builder = InlineKeyboardBuilder()
    builder.button(text=f'🧸Default Box({price_box["default"]}⭐)', callback_data='Box_default')
    builder.button(text=f'🍭LolPop Box({price_box["lolpop"]}⭐)', callback_data = 'Box_LolPop')
    builder.button(text=f'⚔️Sword Box({price_box["sword"]}⭐)', callback_data='Box_Sword')
    builder.button(text=f'💜LovePotion Box({price_box["lovepotion"]}⭐)', callback_data='Box_LovePotion')
    builder.button(text=f'💎TG Premium Box({price_box["tgprem"]}⭐)', callback_data='Box_TGPrem')
    builder.button(text='Назад', callback_data='back_to_menu')
    builder.adjust(1)
    return builder.as_markup()

def open_box(namee):
    builder = InlineKeyboardBuilder()
    box, name = namee.split('_')
    builder.button(text=f'💜 Открыть {name} {box}', callback_data=f'open_{namee}')
    builder.button(text=f'Назад', callback_data='back_to_box')
    builder.adjust(1)
    return builder.as_markup()

def open_after(name):
    builder = InlineKeyboardBuilder()
    builder.button(text=f'💜 Открыть еще ({price_box[name.split("_")[2].lower()]}⭐)', callback_data=name)
    builder.button(text=f'Назад', callback_data='back_to_box')
    builder.adjust(1)
    return builder.as_markup()

def tops():
    builder = InlineKeyboardBuilder()
    builder.button(text=f'💜 Топ по выигрышу', callback_data='top_win')
    builder.button(text=f'💙 Топ по рефералам', callback_data='top_referals')
    builder.button(text='Назад', callback_data='back_to_menu')
    builder.adjust(1)
    return builder.as_markup()

def back(when):
    back = InlineKeyboardBuilder()
    back.button(text=f'Назад', callback_data=f'back_to_{when}')
    back.adjust(1)
    return back.as_markup()

def default_gift_choice(choice, view = False, owned_id = 0, mode = 'default'):
    builder = InlineKeyboardBuilder()
    if not view:
        for x in choice:
            builder.button(text=f' ', callback_data=f'cell_{x}_{mode}')
    else:
        for x in choice:
            builder.button(text=x.split('_')[0], callback_data=x)
        builder.button(text=f'💜 Обменять', callback_data=f'replacegift_["{owned_id}"]_{mode}')
        builder.button(text=f'💙 В профиль', callback_data=f'takegift_["{owned_id}"]_{mode}')
    builder.adjust(3)
    return builder.as_markup()

def tonorstars():
    builder = InlineKeyboardBuilder()
    builder.button(text=f'💜 TG Stars', callback_data='deposit_star')
    builder.button(text=f'💙 Toncoin', callback_data='deposit_TON')
    builder.button(text='Назад', callback_data='back_to_menu')
    builder.adjust(2, 1)
    return builder.as_markup()

def dep_btn(hash):
    builder = InlineKeyboardBuilder()
    builder.button(text=f'✅ Пополнить', callback_data='dep_btn', url= f'ton://transfer/UQB9_Ff2ROi58ihBkgechWFA5cZDkj2KfkIzIwhwM0IsfkjY?text={hash.decode()}')
    builder.adjust(1)
    return builder.as_markup()

def play(mode, bet_player = None):
    builder = InlineKeyboardBuilder()

    if mode in ['basketball', 'football', 'darts', 'bouling']: bet = bet_player.bet_casino
    else: bet = price_box[mode]

    builder.button(text=f'Играть ({bet} ⭐)', callback_data=f'play_{mode}')
    builder.button(text='Назад', callback_data='back_to_menu')
    builder.adjust(1)

    return builder.as_markup()

def pole_bomb(pole, use_already:list = list(), lost = False, mode = 'luckybomb'):
    builder = InlineKeyboardBuilder()

    if mode == 'luckybomb': command = 'bomb'
    else: command = 'door'

    if not lost:
        for x in pole:
            if x["num"] not in use_already:
                builder.button(text=' ' if mode == 'luckybomb' else '🚪', callback_data=f'{command}_{x["num"]}')
            else:
                builder.button(text=x["emodji"], callback_data='usew')
            builder.button(text=str(x['row'] + 1), callback_data=f'floor_{x["row"]}') if x['num'] in [4, 9, 14, 19, 24] and mode == 'tower' else None
        builder.button(text='Забрать приз', callback_data='get_gifts') if use_already != [] else None
    else:
        for x in pole:
            builder.button(text=x["emodji"], callback_data='use')
            builder.button(text=str(x['row'] + 1), callback_data=f'floor_{x["row"]}') if x['num'] in [4, 9, 14, 19, 24] and mode == 'tower' else None
        builder.button(text=f'Назад', callback_data=f'back_to_{mode}')
        builder.button(text=f'Играть еще ({price_box[mode]} ⭐)', callback_data=f'play_{mode}')
    builder.adjust(5 if mode == 'luckybomb' else 6)
    return builder.as_markup()

def repl_take(owned_id: list, mode:str):
    builder = InlineKeyboardBuilder()
    builder.button(text=f'💜 Обменять', callback_data=f'replacegift_{owned_id}_{mode}')
    builder.button(text=f'💙 В профиль', callback_data=f'takegift_{owned_id}_{mode}')
    builder.adjust(1)
    return builder.as_markup()

def casino_sport(bet):
    builder = InlineKeyboardBuilder()
    builder.button(text=f'🏀 Баскетбол', callback_data='casino_basketball')
    builder.button(text=f'⚽ Футбол', callback_data='casino_football')
    builder.button(text=f'🎯 Дартс', callback_data='casino_darts')
    builder.button(text=f'🎳 Боулинг', callback_data='casino_bouling')
    builder.button(text=f'Изменить ставку ({bet} ⭐)', callback_data='bet_replace')
    builder.button(text=f'Назад', callback_data='back_to_menu')

    builder.adjust(2, 2, 1, 1)
    return builder.as_markup()

def task(tasks):
    builder = InlineKeyboardBuilder()
    for x in tasks:
        builder.button(text=f"{x.id}", callback_data=f'check_{x.official_name}')
    builder.button(text=f'Назад', callback_data='back_to_menu')
    builder.adjust(3)
    return builder.as_markup()