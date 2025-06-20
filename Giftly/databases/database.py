from sqlalchemy import select, update, desc, delete
import time
from databases.core import async_session
from databases.models import User, Gifts, Deposit_TON


async def insert_data(user_id:int, name:str, referer_id:int, user_name:str):
    async with async_session() as session:
        requests = await select_user(user_id)
        if not requests:
            work_data = User(
                user_id = int(user_id),
                name = name,
                referer = int(referer_id),
                user_name = '@' + user_name,
                time_register = time.time()
            )
            session.add(work_data)
            await session.commit()
            return True

async def select_user(user_id:int):
    async with async_session() as session:
        requests = select(User).where(User.user_id == int(user_id))
        result = await session.execute(requests)
        user = result.scalars().first()
    return user

async def update_user(user_id:int, column: str, value: int | str):
    async with async_session() as session:
        request = (
            update(User).
            where(User.user_id == user_id).
            values({column: value})
        )

        await session.execute(request)
        await session.commit()

async def top_users(category):
    async with async_session() as session:
        if category == 'win':
            request = select(User).order_by(desc(User.play_win))
        else:
            request = select(User).order_by(desc(User.referals))
        result = await session.execute(request)
        top = result.scalars().all()
    return top

async def insert_gift(owner_id:str, rarity:str, name:str):
    async with async_session() as session:
        work_data = Gifts(
            owned_id = owner_id,
            name = name,
            rarity = rarity
        )
        session.add(work_data)
        await session.commit()
        return True

async def select_gift(rarity:str):
    async with async_session() as session:
        requests = select(Gifts).where(Gifts.rarity == rarity)
        result = await session.execute(requests)
        gifts = result.scalars().all()
    return gifts

async def delete_gift(owned_id:int):
    async with async_session() as session:
        requests = delete(Gifts).where(Gifts.owned_id == owned_id)
        await session.execute(requests)
        await session.commit()

async def select_wallet(category, user_id = None):
    async with async_session() as session:
        if category == 'select':
            requests = select(Deposit_TON).where(Deposit_TON.busy == False)
        else:
            requests = select(Deposit_TON).where(Deposit_TON.user_id == user_id)
        result = await session.execute(requests)
        gifts = result.scalars().all()
    return gifts

async def update_wallet(wallet:str, busy, user_id:int, last_hash = None):
    async with async_session() as session:
        res = {'busy': busy, 'user_id': user_id}
        if last_hash != None:
            res.setdefault('last_hash', last_hash)
        request = (
            update(Deposit_TON).
            where(Deposit_TON.wallet_name == wallet).
            values(res)
        )

        await session.execute(request)
        await session.commit()

