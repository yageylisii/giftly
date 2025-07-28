import random
from bot.utils.constants import *
from bot.utils.send_gifts import *
from databases.database import delete_gift


async def Game_NFT(user_id, type):
    if type == 'default':
        box = gift_default_wh_none
        result = random.choices(list(box.keys()), weights=list(box.values()), k=1)[0]
        if result == None: return 0, 'game_lose'
        return result, 'game_win_def'
    if type == 'lolpop':
        if not await gift_checker(['default']): return 'gifts_end'
        box = lolpop_box
    elif type == 'sword':
        if not await gift_checker(['default', 'middle']): return 'gifts_end'
        box = sword_box
    elif type == 'lovepotion':
        if not await gift_checker(['default', 'middle', 'high']): return 'gifts_end'
        box = lovepotion_box
    elif type == 'tgprem':
        box = tgprem_box
    result = random.choices(list(box.keys()), weights=list(box.values()), k=1)[0]
    if result == 'nft_default':
        gift = random.choice(await select_gift('default'))

        await send_nft_gift(gift, user_id)
        await delete_gift(gift.owned_id)

        return gift, 'game_win'
    elif result == 'nft_middle':
        gift = random.choice(await select_gift('middle'))

        await send_nft_gift(gift, user_id)
        await delete_gift(gift.owned_id)

        return gift, 'game_win'
    elif result == 'nft_high':
        gift = random.choice(await select_gift('high'))

        await send_nft_gift(gift, user_id)
        await delete_gift(gift.owned_id)

        return gift, 'game_win'
    elif result == 'default':
        return random_default_gift(), 'game_win_list'
    elif result in ['prem_3', 'prem_6', 'prem_12']:
        _, month_count = result.split('_')
        return month_count, 'game_win_prem'
    else: return 0, 'game_lose'

def random_default_gift():
    gift_list = gift_default_wh_none.copy()
    del gift_list[None]
    res = random.choices(list(gift_list.keys()), weights = list(gift_default_wt_None.values()), k = 9)
    res_1 = [x + f'_{n}' for n, x in enumerate(res)]
    return res_1
