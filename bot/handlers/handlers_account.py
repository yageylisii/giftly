from bot.config import dp


@dp.business_message()
async def test(message):
    print(message)
    # if message.unique_gift != None:
    #     request = await database.insert_gift(
    #         owner_id=message.unique_gift.owned_gift_id,
    #         name = message.unique_gift.gift.name,
    #         rarity= 'default'
    #     )
    #     if request:
    #         print(f'Подарок {message.unique_gift.gift.name} {message.gifts.owned_gift_id} добавлен!')
    # else:
    #     print('это не гифт')
    # await bot.transfer_gift(
    #     business_connection_id=BUSINESS_ID,
    #     owned_gift_id='674',
    #     new_owner_chat_id=message.chat.id
    # )
    # print(message)
    # # await bot.send_gift('5170145012310081615', message.chat.id)
    # await message.answer('Подарок отправлен')