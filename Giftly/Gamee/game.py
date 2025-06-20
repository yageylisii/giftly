import random
from databases.database import select_gift, delete_gift
from config import bot, BUSINESS_ID
from Gamee.constants import *

async def send_nft_gift(owned_id, user_to):
    try:
        await bot.transfer_gift(
                business_connection_id=BUSINESS_ID,
                owned_gift_id=owned_id,
                new_owner_chat_id=int(user_to),
            star_count=25
            )
    except Exception as e:
        print(e)

async def send_default_gift(user_to, owned_id):
    await bot.send_gift(owned_id, user_to, text = 'Gift from Giftly 💜')

async def Game(user_id, type): #ВАЖНО
    if type == 'default':
        result = random.choices(list(gift_default_wh_none.keys()), weights=list(gift_default_wh_none.values()), k=1)[0]
        result1 = result.split('_')
        if result != 'None':

            return result1[1], result1[0]
        else:
            return False
    elif type == 'lolpop':
        info_gifts = await select_gift('default')
        if info_gifts != []:
            result = random.choices(list(lolpop_box.keys()), weights=list(lolpop_box.values()), k=1)[0]
            if result == 'nft_default':
                await send_nft_gift(info_gifts[0].owned_id, user_id)
                await delete_gift(info_gifts[0].owned_id)
                return info_gifts[0]
            elif result == 'default':
                return 'default'
            else:
                return False
        else:
            return 'gifts_end'
    elif type == 'sword':
        info_gifts1 = await select_gift('middle')
        info_gifts = await select_gift('default')
        if info_gifts != [] and info_gifts1 != []:
            result = random.choices(list(sword_box.keys()), weights=list(sword_box.values()), k=1)[0]
            if result == 'nft_default':
                await send_nft_gift(info_gifts[0].owned_id, user_id)
                await delete_gift(info_gifts[0].owned_id)
                return info_gifts[0]
            elif result == 'nft_middle':
                await send_nft_gift(info_gifts1[0].owned_id, user_id)
                await delete_gift(info_gifts1[0].owned_id)
                return info_gifts1[0]
            elif result == 'default':
                return 'default'
            else:
                return False
        else:
            return 'gifts_end'

def random_default_gift():
    res = random.choices(list(gift_default.keys()), weights = list(gift_default.values()), k = 9)
    res_1 = [x + f'_{n}' for n, x in enumerate(res)]
    return res_1
