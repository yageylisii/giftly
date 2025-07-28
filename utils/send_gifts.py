from bot.config import bot, BUSINESS_ID
from pyrogram import Client

from bot.utils import text_game
from bot.utils.text_game import cong_win_box, bomb_game
from databases.database import select_gift

async def send_premium(user_id: int, count_month: int):
    st_count = {
        3: 1000,
        6: 1500,
        12: 2500
    }
    try:
        ans = await bot.gift_premium_subscription(
            user_id = user_id,
            month_count = count_month,
            star_count = st_count[count_month]

        )
        return {'status': True, 'description': ans}
    except Exception as e:
        return {'status': False, 'description': e}

async def default_gift(user_id: int, gift_ID: int):
    async with Client('my_account', api_id = 26923970, api_hash= 'db55c2cbb6b105f373c9d692b5e30b7a') as pyro:
        await pyro.send_gift(
            user_id=user_id,
            gift_id=int(gift_ID),
            text="Подарок от Giftly 💜"
        )

async def send_nft_gift(gift_info, user_to, mode = 'boxes'):
    try:
        # await bot.transfer_gift(
        #         business_connection_id=BUSINESS_ID,
        #         owned_gift_id=gift_info.owned_id,
        #         new_owner_chat_id=int(user_to),
        #         star_count=25
        #     )
        if mode == 'boxes':
            text = cong_win_box('nft_win', gift_info)
        else:
            text = bomb_game(result='nft', NFT=gift_info)

        await bot.send_message(
            chat_id = user_to,
            text = text,
            parse_mode = "HTML"
        )
    except Exception as e:
        print(e)

async def gift_checker(types:list):
    return all([True if await select_gift(typee) != [] else False for typee in types])


