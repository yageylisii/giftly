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

🧸 Default Box
<blockquote>Обычные
подарки
</blockquote>
🍭 LolPop Box
<blockquote>Lol Pop
Desk Calendar
Candy Cane
</blockquote>
⚔️ Sword Box
<blockquote>Sword
Spy Agaric
Witch Hat
</blockquote>
💜 LovePotion Box
<blockquote>Love Potion
Record Ring
</blockquote>
💎 TG Premium Box
<blockquote>3 месяца
6 месяцев
</blockquote>
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
        return '''
🍭 LolPop Box

Цена открытия: 45⭐

❔ Может выпасть:

💙НEуникальные подарки (40%)
💜Lol pop (15%)
💙Desk Calendar (15%) 
💜Candy Cane (15%)    
        '''
    if name.lower() == 'box_sword':
        return '''
⚔️ Sword Box

Цена открытия: 150⭐

Может выпасть:

Неуникальные подарки (50%)
Lol pop/Desk Calendar (20%)
Sword/Spy Agaric/Witch Hat (10%)    
                '''
    else:
        return '''
Это box gold.

Цена открытия: 500
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

Под ячейкой было: {item.split('_')[2]} ({constants.gift_price_by_id[item.split("_")[1]]} ⭐)

Вы можете вывести этот подарок себе в профиль ИЛИ обменять на звезды в боте.

‼️ ВАЖНО! Подарок нельзя конвертировать в звезды из-за особенности телеграмма ‼️   
    
    
    '''

# 💜 Ваша Реферальная ссылка:\nhttps://t.me/giftlyTON_bot?start=ref{user_id}
