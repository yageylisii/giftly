import random
from Gamee.constants import gift_default_wt_None


def Game_super():
    pole = [0] * 25
    gift_default = random.sample(range(0, 25), k = 10)
    free_cell = [x for x in range(0, 25) if x not in gift_default]
    gift_nft = random.choices(free_cell, k = 2)
    for x in range(0, 25):
        if x in gift_default:
            gift = random.choices(list(gift_default_wt_None.keys()), weights=list(gift_default_wt_None.values()), k=1)[0]
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
# ['1_🧸', 0_None