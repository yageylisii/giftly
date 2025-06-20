from Scripts.bottle import response

from config import bot
import asyncio
from aiogram.methods import GetAvailableGifts
import requests
# # info = await bot.get_business_account_gifts('ZaEuVHZAWEaHAAAAOf7ssj4-XQ4')
# url1 = f'https://api.telegram.org/bot7723902874:AAGgd5QffwNPZFpGUisoRcTn-0zcSx6mso8/getBusinessAccountGifts'
url = f'https://api.telegram.org/bot7723902874:AAGgd5QffwNPZFpGUisoRcTn-0zcSx6mso8/getAvailableGifts'
# # response = requests.post(url, data= {
# #     'business_connection_id': 'ZaEuVHZAWEaHAAAAOf7ssj4-XQ4',
# #     'owned_gift_id': '5170145012310081615',
# #     'new_owner_chat_id': 1035765417
# # })
# response1 =  requests.post(url1, data = {"business_connection_id": "ZaEuVHZAWEaHAAAAOf7ssj4-XQ4"})
# response = requests.get(url)
# inf = response.json()['result']['gifts']
# for x in inf:
#     print(x['id'], x['star_count'], x['sticker']['emoji'])
# print(response1.text)
print(len("cell_🏆_7_['💐_0', '🏆_1', '🎁_2', '🎁_3', '🧸_4', '🌹_5', '🌹_6', '🏆_7', '🌹_8']"))


# import json
#
# a = json.dumps("message_id=923 date=datetime.datetime(2025, 6, 15, 8, 39, 50, tzinfo=TzInfo(UTC)) chat=Chat(id=1035765417, type='private', title=None, username='aidzensolo', first_name='Sergey', last_name=None, is_forum=None, accent_color_id=None, active_usernames=None, available_reactions=None, background_custom_emoji_id=None, bio=None, birthdate=None, business_intro=None, business_location=None, business_opening_hours=None, can_set_sticker_set=None, custom_emoji_sticker_set_name=None, description=None, emoji_status_custom_emoji_id=None, emoji_status_expiration_date=None, has_aggressive_anti_spam_enabled=None, has_hidden_members=None, has_private_forwards=None, has_protected_content=None, has_restricted_voice_and_video_messages=None, has_visible_history=None, invite_link=None, join_by_request=None, join_to_send_messages=None, linked_chat_id=None, location=None, message_auto_delete_time=None, permissions=None, personal_chat=None, photo=None, pinned_message=None, profile_accent_color_id=None, profile_background_custom_emoji_id=None, slow_mode_delay=None, sticker_set_name=None, unrestrict_boost_count=None) message_thread_id=None from_user=User(id=1035765417, is_bot=False, first_name='Sergey', last_name=None, username='aidzensolo', language_code='ru', is_premium=True, added_to_attachment_menu=None, can_join_groups=None, can_read_all_group_messages=None, supports_inline_queries=None, can_connect_to_business=None, has_main_web_app=None) sender_chat=None sender_boost_count=None sender_business_bot=None business_connection_id='ZaEuVHZAWEaHAAAAOf7ssj4-XQ4' forward_origin=None is_topic_message=None is_automatic_forward=None reply_to_message=None external_reply=None quote=None reply_to_story=None via_bot=None edit_date=None has_protected_content=None is_from_offline=None media_group_id=None author_signature=None paid_star_count=None text=None entities=None link_preview_options=None effect_id=None animation=None audio=None document=None paid_media=None photo=None sticker=None story=None video=None video_note=None voice=None caption=None caption_entities=None show_caption_above_media=None has_media_spoiler=None contact=None dice=None game=None poll=None venue=None location=None new_chat_members=None left_chat_member=None new_chat_title=None new_chat_photo=None delete_chat_photo=None group_chat_created=None supergroup_chat_created=None channel_chat_created=None message_auto_delete_timer_changed=None migrate_to_chat_id=None migrate_from_chat_id=None pinned_message=None invoice=None successful_payment=None refunded_payment=None users_shared=None chat_shared=None gift=None unique_gift=UniqueGiftInfo(gift=UniqueGift(base_name='Lol Pop', name='LolPop-286964', number=286964, model=UniqueGiftModel(name='Cucumber', sticker=Sticker(file_id='CAACAgIAAxUAAWhOhtbH8gy_e7IzkbfM7KiYtK5OAAKuawACMh3ZStYaR-kk2EvRNgQ', file_unique_id='AgADrmsAAjId2Uo', type='custom_emoji', width=512, height=512, is_animated=True, is_video=False, thumbnail=PhotoSize(file_id='AAMCAgADFQABaE6G1sfyDL97sjORt8zsqJi0rk4AAq5rAAIyHdlK1hpH6STYS9EBAAdtAAM2BA', file_unique_id='AQADrmsAAjId2Upy', width=128, height=128, file_size=4022), emoji='🍭', set_name=None, premium_animation=None, mask_position=None, custom_emoji_id='5393374129338477486', needs_repainting=None, file_size=57733, thumb={'file_id': 'AAMCAgADFQABaE6G1sfyDL97sjORt8zsqJi0rk4AAq5rAAIyHdlK1hpH6STYS9EBAAdtAAM2BA', 'file_unique_id': 'AQADrmsAAjId2Upy', 'file_size': 4022, 'width': 128, 'height': 128}), rarity_per_mille=12), symbol=UniqueGiftSymbol(name='Eagle', sticker=Sticker(file_id='CAACAgIAAxUAAWhOhta8WJkQNvBOG6uvDlh7jCp6AALzXgACkZqAS3UQqDOD2ZTkNgQ', file_unique_id='AgAD814AApGagEs', type='custom_emoji', width=512, height=512, is_animated=True, is_video=False, thumbnail=PhotoSize(file_id='AAMCAgADFQABaE6G1rxYmRA28E4bq68OWHuMKnoAAvNeAAKRmoBLdRCoM4PZlOQBAAdtAAM2BA', file_unique_id='AQAD814AApGagEty', width=128, height=128, file_size=1852), emoji='🦅', set_name=None, premium_animation=None, mask_position=None, custom_emoji_id='5440518297424518899', needs_repainting=True, file_size=1070, thumb={'file_id': 'AAMCAgADFQABaE6G1rxYmRA28E4bq68OWHuMKnoAAvNeAAKRmoBLdRCoM4PZlOQBAAdtAAM2BA', 'file_unique_id': 'AQAD814AApGagEty', 'file_size': 1852, 'width': 128, 'height': 128}), rarity_per_mille=5), backdrop=UniqueGiftBackdrop(name='Satin Gold', colors=UniqueGiftBackdropColors(center_color=12557127, edge_color=9271097, symbol_color=6109952, text_color=16704681), rarity_per_mille=15)), origin='transfer', owned_gift_id='923', transfer_star_count=25) connected_website=None write_access_allowed=None passport_data=None proximity_alert_triggered=None boost_added=None chat_background_set=None forum_topic_created=None forum_topic_edited=None forum_topic_closed=None forum_topic_reopened=None general_forum_topic_hidden=None general_forum_topic_unhidden=None giveaway_created=None giveaway=None giveaway_winners=None giveaway_completed=None paid_message_price_changed=None video_chat_scheduled=None video_chat_started=None video_chat_ended=None video_chat_participants_invited=None web_app_data=None reply_markup=None forward_date=None forward_from=None forward_from_chat=None forward_from_message_id=None forward_sender_name=None forward_signature=None user_shared=None")
# print(json.loads(a))

# from databases.database import select_gift
# import asyncio
# async def main():
#     print(await select_gift('default'))
# asyncio.run(main())
# print(len('🎁 Открой бокс — испытай'))




# import asyncio
# from config import bot
# async def main():
#     ChatFullInfo = await bot.get_chat('@floorpricegift')
#     return ChatFullInfo
# print(asyncio.run((main())))


# address = "EQAkzx-hmjaPghHQjRxA26cfHSE-D38mSoRRJ7b8Btll3Obg"  # ваш адрес
# headers = {"Authorization": "Bearer AFVBQYIYSUAJOUYAAAAB5AY6IIIJH2W3LM3R2GUL3DO4HIZKD275BFSOR24RDDLS2JQ24UQ"}
# url = f"https://tonapi.io/v2/blockchain/accounts/{address}/transactions?limit=5"
#
# res = requests.get(url, headers=headers)
# print(res.json())
# last_hash = '05d82580d574c6df74d830e5e03e2deab1ef1eb90ad2508dbb77b9687fa75f65'
# new_deps = []
# for x in res.json()['transactions']:
#     if x['success']:
#         new_deps.append(float((x['credit_phase']['credit']) / 1000000000))
#     if x['hash'] == last_hash:
#         break
# print(new_deps)
