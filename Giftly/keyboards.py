from itertools import count

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
    builder.button(text = '💙 Пополнить 💙', callback_data='deposit')
    builder.button(text='💜 Топы 💜', callback_data='tops')
    builder.button(text='⁉️ FAQ', callback_data='support')
    builder.button(text='📃 Задания', callback_data='tasks')
    builder.button(text='Реферальная программа', callback_data='referlls')
    builder.adjust(2,1,1,2,1)
    return builder.as_markup()

def boxes():
    builder = InlineKeyboardBuilder()
    builder.button(text='🧸Default Box(15⭐)', callback_data='Box_default')
    builder.button(text='🍭LolPop Box(45⭐)', callback_data = 'Box_LolPop')
    builder.button(text='⚔️Sword Box(100⭐)', callback_data='Box_Sword')
    builder.button(text='💜LovePotion Box(350⭐)', callback_data='Box_LovePotion')
    builder.button(text='💎TG Premium Box(150⭐)', callback_data='Box_TGPrem')
    builder.button(text='Назад', callback_data='back_to_menu')
    builder.adjust(1)
    return builder.as_markup()

def open_box(name):
    builder = InlineKeyboardBuilder()
    name1 = name.split('_')
    builder.button(text=f'Открыть {name1[1]} {name1[0]}', callback_data=f'open_{name}')
    builder.button(text=f'Назад', callback_data='back_to_box')
    builder.adjust(1)
    return builder.as_markup()

def open_after(name):
    builder = InlineKeyboardBuilder()
    if name == 'open_Box_default':
        count = 15
    elif name == 'open_Box_LolPop':
        count = 45
    elif name == 'open_Box_Sword':
        count = 150
    elif name == 'open_Box_LovePotion':
        count = 350
    builder.button(text=f'💜 Открыть еще ({count} ⭐)', callback_data=name)
    builder.button(text=f'Назад', callback_data='back_to_box')
    builder.adjust(1)
    return builder.as_markup()

def tops():
    builder = InlineKeyboardBuilder()
    builder.button(text=f'Топ по выигрышу', callback_data='top_win')
    builder.button(text=f'Топ рефералам', callback_data='top_referals')
    builder.button(text='Назад', callback_data='back_to_menu')
    builder.adjust(1)
    return builder.as_markup()
def back(when):
    back = InlineKeyboardBuilder()
    back.button(text=f'Назад', callback_data=f'back_to_{when}')
    back.adjust(1)
    return back.as_markup()
def default_gift_choice(choice, view = False, owned_id = 0):
    builder = InlineKeyboardBuilder()
    print(choice)
    if not view:
        for x in choice:
            builder.button(text=f' ', callback_data=f'cell_{x}')
    else:
        for x in choice:
            builder.button(text=x.split('_')[1], callback_data=x)
        builder.button(text=f'Обменять', callback_data=f'replace_gift_{owned_id}')
        builder.button(text=f'Забрать', callback_data=f'take_gift_{owned_id}')
    builder.adjust(3)
    return builder.as_markup()
def tonorstars():
    builder = InlineKeyboardBuilder()
    builder.button(text=f'💜 TG Stars', callback_data='deposit_star')
    builder.button(text=f'💙 Toncoin', callback_data='deposit_TON')
    builder.button(text='Назад', callback_data='back_to_menu')
    builder.adjust(2, 1)
    return builder.as_markup()

def proverka_depa():
    builder = InlineKeyboardBuilder()
    builder.button(text=f'✅ Оплатил', callback_data='dep_true')
    builder.button(text=f'Отмена', callback_data='cancel')
    builder.adjust(1)
    return builder.as_markup()