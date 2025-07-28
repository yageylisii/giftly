from databases import database

async def upgrade_balance(user_data, profit:int):
    balance_now = user_data.balance_star
    await database.update_user(
        user_id=user_data.user_id,
        column = "balance_star",
        value = balance_now + profit
    )
    if profit > 0:
        playwin_now = user_data.play_win
        await database.update_user(
            user_id=user_data.user_id,
            column="play_win",
            value=playwin_now + profit
        )
    else:
        play_count = user_data.count_win
        await database.update_user(
            user_id=user_data.user_id,
            column="count_win",
            value=play_count + 1
        )
