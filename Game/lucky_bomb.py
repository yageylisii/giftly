import random
from bot.utils.constants import gift_default_wh_none


def Game_super():
    pole = [0] * 25
    gift_default = random.sample(range(0, 25), k = 10)
    free_cell = [x for x in range(0, 25) if x not in gift_default]
    gift_nft = random.sample(free_cell, k = 2)
    for x in range(0, 25):
        if x in gift_default:
            gift_list = gift_default_wh_none.copy()
            del gift_list[None]
            gift = random.choices(list(gift_list.keys()), weights=list(gift_list.values()), k=1)[0]
            pole[x] = {
                'status': 1,
                'gift': gift,
                'emodji': gift,
                'num': x
            }
        elif x in gift_nft:
            pole[x] = {
                'status': 2,
                'gift_NFT': None, #взять рандом owned_id из БД
                'emodji': '💜',
                'num': x
            }
        else:
            pole[x] = {
                'status': 0,
                'emodji': '💣',
                'num': x
            }
    return pole