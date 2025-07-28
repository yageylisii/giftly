from aiogram import F, types
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, Message, CallbackQuery
from Game import casino
from bot import keyboards
from bot.config import bot, dp
from bot.utils import text_game, constants
import asyncio

from bot.utils.upgrade_balance import upgrade_balance
from databases import database


@dp.callback_query(F.data.startswith("casino"))
async def handle_casino_start(callback: CallbackQuery, state: FSMContext) -> None:
    try:
        _, mode = callback.data.split('_')
        image = FSInputFile(f'bot/photo/{mode}.png')
        caption = text_game.casino_plays(mode)
        user_id = callback.from_user.id
        user_data = await database.select_user(user_id)
        reply_markup = keyboards.play(mode, user_data)

        await callback.message.edit_media(media=types.InputMediaPhoto(media=image))
        await callback.message.edit_caption(
            caption=caption,
            reply_markup=reply_markup,
        )
    except Exception as e:
        await callback.answer("Произошла ошибка при запуске игры")
        raise e


@dp.callback_query(F.data.in_(["play_basketball", "play_darts", "play_bouling", "play_football"]))
async def handle_game_start(callback: CallbackQuery, state: FSMContext) -> None:

    _, mode = callback.data.split('_')
    user_id = callback.from_user.id
    user_data = await database.select_user(user_id)

    if user_data.balance_star >= user_data.bet_casino:
        game = await casino.Game_create(state, mode)
        if not game.get("status"):
            await callback.answer(game.get("description", "Ошибка запуска игры"))
            return

        await upgrade_balance(user_data, user_data.bet_casino*-1)

        await callback.answer("💙💜 Игра началась. Я хожу первым 💜💙")
        await casino.step_bot(state, player="bot", user_id=user_id)
        await callback.message.answer(text=f"💙 Ваш ход!")
    else:
        await callback.answer('⚠️ Не хватает баланса ⚠️')
        await callback.message.delete()
        await callback.message.answer(
            text='💜💙 Выбери способ оплаты 💙💜',
            reply_markup=keyboards.tonorstars()
        )

@dp.message(F.content_type == ContentType.DICE)
async def handle_dice_roll(message: Message, state: FSMContext) -> None:

    state_data = await state.get_data()
    expected_emoji = state_data.get("mode")
    is_bot_turn = state_data.get("is_bot", None)

    if message.dice.emoji != expected_emoji:
        warning = await message.answer(f"⚠️ Используй нужный режим: {expected_emoji}")
        await asyncio.sleep(2)
        await warning.delete()
        return

    if is_bot_turn:
        wait_msg = await message.answer("⏳ Дождись конца анимации!!!")
        await asyncio.sleep(2)
        await wait_msg.delete()
        return

    player_result = await casino.step_bot(
        state=state,
        player="player",
        user_id=message.from_user.id,
        result=message
    )

    round_number = player_result["info_field"].get("round")
    if round_number == 3:
        user_data = await database.select_user(message.from_user.id)
        text = await casino.game_result(player_result['info_field'], user_data, user_data.bet_casino)

        text_final = f"🏁 Игра завершена\n\n{text[0]}"
        keyboard = keyboards.play(player_result['info_field']['name'], user_data)

        if text[1] == 'win':
            mode = player_result["info_field"]["name"]
            await message.answer_photo(
                photo=FSInputFile(f'bot/photo/{mode}_win.png'),
                caption=text_final,
                reply_markup=keyboard,
            )
        else:
            await message.answer(
                text = text_final,
                reply_markup=keyboard,
            )
        await state.clear()
        return

    emodji = message.dice.emoji
    value = message.dice.value
    await message.answer(constants.point_and_value[emodji][value][1])
    await casino.step_bot(
        state=state,
        player="bot",
        user_id=message.from_user.id
    )
    await message.answer(text=f"💙 Ваш ход!")



