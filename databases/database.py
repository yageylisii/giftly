from sqlalchemy import select, update, desc, delete
import time
from databases.core import async_session
from databases.models import User, Gifts, Tasks


async def insert_data(user_id:int, name:str, referer_id:int, user_name:str):
    async with async_session() as session:
        requests = await select_user(user_id)
        if not requests:
            work_data = User(
                user_id = int(user_id),
                name = name,
                referer = int(referer_id),
                user_name = 'unknown' if user_name == None else user_name,
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

async def select_tasks():
    async with async_session() as session:
        tasks_get = select(Tasks)
        result = await session.execute(tasks_get)
        tasks = result.scalars().all()
        return tasks

