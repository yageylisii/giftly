from datetime import datetime, timezone
from Gamee import constants
gift_id_by_emoji = {
    "💝": "5170145012310081615",
    "🧸": "5170233102089322756",
    "🎁": "5170250947678437525",
    "🌹": "5168103777563050263",
    "🎂": "5170144170496491616",
    "💐": "5170314324215857265",
    "🚀": "5170564780938756245",
    "🍾": "6028601630662853006",
    "🏆": "5168043875654172773",
    "💍": "5170690322832818290",
    "💎": "5170521118301225164",
}

def hello():
    return '''
Салам Брат, это бот-подарки
крутишь рулетку - забираешь подарки

Переl началом использовавния ознакомься с правилами и нажми на кнопку, если согласен.

Наш канал @giftly_ton
    
    
    '''
def menu(user_id, name, balance, referals, wins, time, doxod):
    dt = datetime.fromtimestamp(time, tz=timezone.utc)
    formatted_date = dt.strftime('%d %B %Y')
    return f'''
🪙 Баланс: {balance}⭐

🎁 Выиграно всего:  {wins}
⏰ Дата регистрации:\n{formatted_date}

👥 Рефералы: {referals}
⭐ Доход от рефералов: {doxod}
'''
def boxes():
    return '''
🔮Что может выпасть из боксов?

‼️ Перед началом игры\nОБЯЗАТЕЛЬНО напиши\n@helper_giftly, чтобы бот\nмог отправлять выигрыши‼️
    '''
def open_box(name):
    if name.lower() == 'box_default':
        return '''
Только неуникальные подарки
💝# 15
🧸# 15
🎁# 25
🌹# 25
🎂# 50
💐# 50
🚀# 50
🍾# 50
🏆 # 100
💍# 100
💎           
'''
    if name.lower() == 'box_lolpop':
        return f'''
🍭 LolPop Box

Цена открытия: {constants.price_box[name.lower().split("_")[1]]}⭐

❔ Может выпасть:

💙НEуникальные подарки (40%)
💜Lol pop (15%)
💙Desk Calendar (15%) 
💜Candy Cane (15%)    
        '''
    if name.lower() == 'box_sword':
        return f'''
⚔️ Sword Box

Цена открытия: {constants.price_box[name.lower().split("_")[1]]}⭐

Может выпасть:

Неуникальные подарки (50%)
Lol pop/Desk Calendar (20%)
Sword/Spy Agaric/Witch Hat (10%)    
                '''
    else:
        return f'''
LovePotion Box.

Цена открытия: {constants.price_box[name.lower().split("_")[1]]} ⭐
Может выпасть:

Неуникальные подарки (30%)
Lol pop (20%)
Desk Calendar (20%)
Sword (7%)
Jelly Bunny (7%)
Love Potion (3%)
Record Ring (3%)
   
            '''

def cong_win(item):
    return f'''
💜 Поздравляем! 💜

Под ячейкой было: {item.split('_')[1]} ({constants.gift_price_by_id[item.split("_")[1]]} ⭐)

Вы можете вывести этот подарок себе в профиль ИЛИ обменять на звезды в боте на 20% больше.   
    
    '''
def support_text():
    return  '''
Что-то осталось непонятным или возникли проблемы? Пишите нам — поддержка всегда на связи: Техподдержка
Правила проекта доступны тут: Правила
'''
def default_win_choice():
    return  '''
💙 Тебе выпал неуникальный подарок.

В ячейках спрятаны подарки разной стоимости (15⭐ - 100⭐). Выбери ячейку, чтобы получить ИЛИ обменять подарок.
'''

def nft_win(result):
    return f'''  
💜💜 Поздравляем! 💜💜\n\nВ боксе был NFT подарок <a href="t.me/nft/{result.name}">{result.name}</a> — он уже отправлен на ваш аккаунт. Наслаждайтесь!
    '''

def lbomb_info():
    return '''
1️⃣ Выбирайте клетку на поле (5x5)
2️⃣ Если там 🎁 — заберите приз или продолжайте игру
3️⃣ Если найдёте 🖼️ NFT-подарок — получите редкий NFT
4️⃣ Если попадёте на 💥 бомбу — теряете ставку    
    '''

def lbomb_info():
    return '''
🔹 Выбирайте по 1 ячейке в каждом ряду.
🔹 Если не попали на бомбу — идёте дальше и получаете подарок 🎁
🔹 Пройдите все 5 рядов — забирайте свой NFT! 🎉
🔹 Попали на бомбу — игра заканчивается. 
    '''

# 💜 Ваша Реферальная ссылка:\nhttps://t.me/giftlyTON_bot?start=ref{user_id}
