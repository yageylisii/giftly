import random

from Gamee.constants import gift_default_wt_None
#добавить анотации + пояснения к каждой переменной

def Game_tower():
    pole = []
    gifts_pole_count = [4, 3, 2, 2, 1]
    for row_num in range(5):
        row = [0] * 5
        gift = random.sample(range(5), k=gifts_pole_count[row_num])
        for x in range(0, len(row)):
            if x in gift:
                row[x] = f'1_{random.choices(list(gift_default_wt_None.keys()), weights=list(gift_default_wt_None.values()), k=1)[0]}_{row_num}'
            else:
                row[x] = f'0_❌_{row_num}'
        pole += row

    return pole[::-1]
print(Game_tower())