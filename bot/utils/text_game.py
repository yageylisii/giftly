from datetime import datetime, timezone
from bot.utils import constants
from bot.utils.constants import gift_price_by_id
from databases import database

def formarter(var:int):
    return '{:,}'.format(var).replace(",", " ")

def hello():
    return '''
💜💙 Добро пожаловать в Giftly 💙💜
🎰 Здесь ты крутишь рулетку и получаешь подарки.
🎮 Доступно несколько игровых режимов — каждый со своими сюрпризами.

📘 Ознакомься с правилами и нажимай «Я согласен» — подарки уже ждут!
🔔 Наш канал: @giftly_ton
    '''
async def menu(user_id):
    info = await database.select_user(user_id)
    dt = datetime.fromtimestamp(info.time_register, tz=timezone.utc)
    formatted_date = dt.strftime('%d %B %Y')
    return f'''
<blockquote><b>💰 Баланс:</b> {formarter(info.balance_star)}⭐ 

<b>🎁 Выиграно всего</b>: {formarter(info.play_win)}⭐
<b>🎁 Игр сыграно</b>: {info.count_win}
<b>⏰ Дата регистрации</b>:\n{formatted_date}

<b>👥 Рефералы</b>: {info.referals}
<b>⭐ Доход от рефералов</b>: {info.referal_amount}
</blockquote>
'''

def boxes():
    return '''
‼️ Перед началом игры
ОБЯЗАТЕЛЬНО напиши
@helper_giftly, чтобы бот
мог отправлять выигрыши‼️
    '''
def open_box(name):
    if name.lower() == 'box_default':
        return f'''
🎁 Default Box 🎁

Цена открытия: {constants.price_box[name.lower().split("_")[1]]}⭐

❔ Может выпасть:

💝 15⭐    🧸 15⭐
🎁 25⭐    🌹 25⭐
🎂 50⭐   💐 50⭐
🚀 50⭐   🍾 50⭐
🏆 100⭐  💍 100⭐
💎 100⭐
'''
    if name.lower() == 'box_lolpop':
        return f'''
🍭 LolPop Box 🍭

Цена открытия: {constants.price_box[name.lower().split("_")[1]]}⭐

❔ Может выпасть:

💙НEуникальные подарки (40%)
💜Lol pop (15%)
💙Desk Calendar (15%) 
💜Candy Cane (15%)    
        '''

    if name.lower() == 'box_sword':
        return f'''
⚔️ Sword Box ⚔️

Цена открытия: {constants.price_box[name.lower().split("_")[1]]}⭐

❔ Может выпасть:

💙 Неуникальные подарки (50%)
💜 Lol Pop (10%)
💙 Desk Calendar (10%)
💜 Sword (4%)
💙 Spy Agaric (3%)
💜 Witch Hat (3%)  
                '''
    else:
        return f'''
💘 LovePotion Box 💘

Цена открытия: {constants.price_box[name.lower().split("_")[1]]} ⭐

❔ Может выпасть:

💙 Неуникальные подарки (30%)
💜 Lol Pop (20%)
💙 Desk Calendar (20%)
💜 Sword (7%)
💙 Jelly Bunny (7%)
💜 Love Potion (3%)
💙 Record Ring (3%)
'''
def cong_win_box(result, gift):
    if result == 'game_lose':
        text = '💔 На этот раз в боксе ничего не оказалось. Но не расстраивайся — удача уже рядом! Попробуй открыть следующий! 💔'
    elif result == 'game_win_def':
        text = f'''
<b>💙💙 Поздравляем!💙💙</b>

В боксе был {gift[0]} ({constants.gift_price_by_id[gift[0]]} ⭐)

Что дальше?
💙 Вывести подарок в профиль
💜 Обменять на звезды — и получить +20% бонусом! ✨  '''
    elif result == 'game_win_prem':
        text = f'''
<b>💎 Поздравляем! Тебе выпал Telegram Premium! 💜💙</b>

🎁 Тебе выпал Telegram Premium на {gift} месяцев — никакой рекламы, суперскорость и эксклюзивные фишки!
        '''
    elif result == 'game_win_list':
        text =     f'''
<b>💙 Тебе выпал неуникальный подарок! 💙</b>

В ячейках спрятаны подарки разной стоимости — от <b>15</b>⭐ до <b>100</b>⭐ 🎁
Выбери одну ячейку, чтобы забрать подарок или обменять его на звёзды ✨'''
    elif result == 'game_win':
        text =  f'''
💜💜 Поздравляем! 💜💜

В боксе был NFT подарок <a href="t.me/nft/{gift.name}">{gift.name}</a> — он уже отправлен на ваш аккаунт. Наслаждайтесь!'''

    return text
def bomb_game(result, info_cell = None, NFT = None):
    if result == 'lose':
        return  '''
💀 Не повезло! Мина прямо под ногами 💀
        
🎁 Подарки не достаются тем, кто спешит. Попробуешь снова? 🎁
'''
    elif result == 'default':
        return f'Под ячейкой был подарок {info_cell["emodji"]} ({gift_price_by_id[info_cell["emodji"]]} ⭐) продолжим?'
    elif result == 'nft':
        return f'''
💜NFT подарок <a href="t.me/nft/{NFT.name}">{NFT.name}</a> уже отправлен на ваш аккаунт. Наслаждайтесь!💜
'''
def cong_win(item):
    return f'''
💙 Поздравляем! 💙

Под ячейкой было: {item.split('_')[1]} ({constants.gift_price_by_id[item.split("_")[1]]} ⭐)

Что дальше?
💙 Вывести подарок в профиль
💜 Обменять на звезды — и получить +20% бонусом! ✨  
    '''
def cong_win(item):
    return f'''
💙 Поздравляем! 💙

Под ячейкой было: {item.split('_')[1]} ({constants.gift_price_by_id[item.split("_")[1]]} ⭐)

Что дальше?
💙 Вывести подарок в профиль
💜 Обменять на звезды — и получить +20% бонусом! ✨  
    '''
def support_text():
    return  '''
📩 Остались вопросы?
Пиши — поддержка всегда на связи: Техподдержка

📘 С правилами проекта можно ознакомиться здесь: Правила

💙 Мы рядом, если что-то пойдёт не так 💜
'''

def top_choice():
    return '''
🏆 Топы Giftly 🏆

Выбери, что хочешь посмотреть:

💜 По выигрышам
💙 По рефералам

👇 Нажми на кнопку ниже, чтобы выбрать категорию рейтинга!  
'''

def referal_program(user_id, user_info):
    ref_count = user_info.referals
    ref_earned = user_info.referal_amount
    return \
f'''
<b>💜 Расскажи о Giftly — забери свой процент! 💙</b>

Поделись ботом с друзьями и <b>забирай 15%</b> со всех их донатов 💸
Они крутят рулетки — а тебе капают ⭐ автоматически!

<b>👥 Твоих рефералов: {ref_count}</b>
<b>💰 Заработано с них: {ref_earned} ⭐</b>

🔗 Твоя ссылка:
https://t.me/giftlyTON_bot?start=ref{user_id}
'''

def flour(num):
    text = [
        'Это начальный этаж: 1 бомба',
        'Это второй этаж: 2 бомбы',
        'Это третий этаж: 3 бомбы',
        'Это четвертый этаж: 3 бомбы',
        'Это последний этаж, пройди его и получи NFT'
    ]
    return text[int(num)]

def choice_casino():
    return '''
<b>🎮 Выбери режим игры</b>

<b>🏀 Баскетбол</b> — броски в кольцо
<b>⚽ Футбол</b> — удары по воротам
<b>🎯 Дартс</b> — меткие попадания
<b>🎳 Боулинг</b> — сбей максимум кеглей     

💙 <b>Играй против бота</b> — у каждого по 3 попытки.
💜 Если ты наберёшь больше очков, чем бот — <b>💰 удвоишь свою ставку!</b>
    '''

def lbomb_info():
    return '''
1️⃣ Выбирайте клетку на поле (5x5)
2️⃣ Если там 🎁 — заберите приз или продолжайте игру
3️⃣ Если найдёте 🖼️ NFT-подарок — получите редкий NFT
4️⃣ Если попадёте на 💥 бомбу — теряете ставку    
    '''
def task_info(x, user):
    id_task = x.id
    desc_task = x.description
    name_task = x.name
    bonus = x.bonus
    uniq_text = {
        1: '',
        2: f'({user.referals}/1)',
        3: f'({user.referals}/10)'
    }
    return f'''
<b>№{id_task} | {name_task} ({bonus}⭐)</b>
{'✅' if x.id in user.tasks else f'❌ {desc_task} {uniq_text.get(id_task, '')}'}
    '''

def tower_info():
    return '''
💙 В каждом ряду спрятаны подарки
💜 Выбирай по 1 ячейке в каждом ряду
💙 Не попал на бомбу — идёшь дальше
💜 Пройди все 5 рядов — и получи NFT
💙 Попал на бомбу — игра заканчивается
    '''

def casino_plays(mode):
    data = {
        'basketball': (
            "🏀 <b>Баскетбол</b>\n"
            "У тебя 3 броска в кольцо.\n"
            "💙 Очки:\n"
            "▫️ Мимо — 0\n"
            "▫️ Кольцо — 2\n"
            "Набери больше очков, чем бот, чтобы <b>удвоить ставку</b>!"
        ),
        'football': (
            "⚽ <b>Футбол</b>\n"
            "3 удара по воротам — покажи точность и силу удара!\n"
            "💜 Очки:\n"
            "▫️ Мимо — 0\n"
            "▫️ Гол — 1\n"
            "Обгони бота по сумме — и <b>забери х2</b> от ставки!"
        ),
        'darts': (
            "🎯 <b>Дартс</b>\n"
            "Метни 3 стрелы и постарайся попасть в центр.\n"
            "💙 Очки:\n"
            "▫️ Внешнее кольцо — 1\n"
            "▫️ Среднее кольцо — в зависимости от расстояния до центра (2-4)\n"
            "▫️ Центр — 5\n"
            "Собери больше очков, чем бот — <b>и получи удвоенную награду</b>!"
        ),
        'bouling': (
            "🎳 <b>Боулинг</b>\n"
            "3 броска шаром — сбей как можно больше кеглей!\n"
            "💜 Очки = сбитые кегли (максимум — 6 за бросок)\n"
            "Суммарно можно набрать до 18 очков.\n"
            "<b>Сбей больше, чем бот — и забери х2!</b>"
        )
    }
    return data.get(mode, 'Эммм')
