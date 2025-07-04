from bot.config import bot, BUSINESS_ID
from pyrogram import Client

async def default_gift(user_id: int, gift_ID: int):
    async with Client('my_account', api_id = 26923970, api_hash= 'db55c2cbb6b105f373c9d692b5e30b7a') as pyro:
        await pyro.send_gift(
            user_id=user_id,
            gift_id=int(gift_ID),
            text="Подарок от Giftly 💜"
        )
async def send_nft_gift(owned_id, user_to):
    try:
        await bot.transfer_gift(
                business_connection_id= BUSINESS_ID,
                owned_gift_id=owned_id,
                new_owner_chat_id=int(user_to),
            star_count=25
            )
    except Exception as e:
        print(e)
