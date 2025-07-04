import random
from databases.database import select_gift, delete_gift
from Gamee.constants import *
from bot.send_gifts.sender import *
import asyncio

async def Game_NFT(user_id, type):
    if type == 'default':
        box = gift_default_wh_none
        result = random.choices(list(box.keys()), weights=list(box.values()), k=1)[0]
        if result == None: return 'game_lose'
        return result, 'gifts_win_def'
    gift_middle = await select_gift('middle')
    gift_default = await select_gift('default')
    if type == 'lolpop':
        if gift_default == []: return 'gifts_end'
        box = lolpop_box
    elif type == 'sword':
        if gift_middle == [] and gift_default == []: return 'gifts_end'
        box = sword_box
    result = random.choices(list(box.keys()), weights=list(box.values()), k=1)[0]
    if result == 'nft_default':
        gift_id = random.randint(0, len(gift_middle) - 1) if len(gift_middle) > 1 else 0
        await send_nft_gift(gift_default[gift_id].owned_id, user_id)
        return gift_default[gift_id], 'game_win'
    elif result == 'nft_middle':
        gift_id = random.randint(0, len(gift_middle) - 1 )
        await send_nft_gift(gift_middle[gift_id].owned_id, user_id)
        return gift_middle[gift_id], 'game_win'
    elif result == 'default':
        return random_default_gift(), 'game_win'
    else: return 'game_lose'
    # elif type == 'lolpop':
    #     info_gifts = await select_gift('default')
    #     if info_gifts != []: return 'gifts_end'
    #     result = random.choices(list(lolpop_box.keys()), weights=list(lolpop_box.values()), k=1)[0]
    #     if result == 'nft_default':
    #         await send_nft_gift(info_gifts[0].owned_id, user_id)
    #         await delete_gift(info_gifts[0].owned_id)
    #         return info_gifts[0]
    #     elif result == 'default':
    #         return 'default'
    #     else:
    #         return False
    # elif type == 'sword':
    #     info_gifts1 = await select_gift('middle')
    #     info_gifts = await select_gift('default')
    #     if info_gifts != [] and info_gifts1 != []: return 'gifts_end'
    #     result = random.choices(list(sword_box.keys()), weights=list(sword_box.values()), k=1)[0]
    #     if result == 'nft_default':
    #         await send_nft_gift(info_gifts[0].owned_id, user_id)
    #         await delete_gift(info_gifts[0].owned_id)
    #         return info_gifts[0]
    #     elif result == 'nft_middle':
    #         await send_nft_gift(info_gifts1[0].owned_id, user_id)
    #         await delete_gift(info_gifts1[0].owned_id)
    #         return info_gifts1[0]
    #     elif result == 'default':
    #         return 'default'
    #     else:
    #         return False
def random_default_gift():
    res = random.choices(list(gift_default_wt_None.keys()), weights = list(gift_default_wt_None.values()), k = 9)
    res_1 = [x + f'_{n}' for n, x in enumerate(res)]
    return res_1
