import random

from bot.utils.constants import gift_default_wh_none


#добавить анотации + пояснения к каждой переменной

def Game_tower():
    pole = []
    gifts_pole_count = [4, 3, 2, 2, 1]
    num_cell = 0
    for row_num in range(4, -1, -1):
        row = [0] * 5
        gift = random.sample(range(5), k=gifts_pole_count[row_num])
        for x in range(0, len(row)):
            if x in gift:
                gift_list = gift_default_wh_none.copy()
                del gift_list[None]
                gift_emodji = random.choices(list(gift_list.keys()), weights=list(gift_list.values()), k=1)[0]
                row[x] = {
                    'status': 1,
                    'gift': gift_emodji,
                    'emodji':  gift_emodji,
                    'num':  num_cell,
                    'row': row_num
                }
            else:
                row[x] = {
                    'status': 0,
                    'emodji': '❌',
                    'num': num_cell,
                    'row': row_num
                }
            num_cell  += 1
        pole += row
    return pole