from fastapi import FastAPI, Request
from bot.config import bot
from bot.utils import hasher
from databases import database
from bot import keyboards

app = FastAPI()

@app.post('/webhook') #сверять хэш транзакции
async def test(request: Request):
    body = await request.json()
    info = await hasher.get_info(body)
    comment = info['actions'][0]['TonTransfer']['comment']
    amount = int(info['actions'][0]['TonTransfer']['amount']) / 1_000_000_000
    user_get = hasher.decoder(comment.encode())
    info_old = await database.select_user(user_get)
    await database.update_user(user_id=user_get, column='balance_star',
                               value=info_old.balance_star + amount * 200)
    text = f'💜 Поступил платеж {amount} TON.\n\n{amount * 200} ⭐ зачислены на баланс\n\nБаланс: {info_old.balance_star + amount * 200} ⭐'
    await bot.send_message(int(user_get), text, reply_markup=keyboards.tonorstars())


@app.get('/')
async def tss():
    return {'status': 'OK'}
