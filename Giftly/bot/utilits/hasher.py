from cryptography.fernet import Fernet
from bot.config import key
import aiohttp

def encoder(user_id: str):
    cipher = Fernet(key.encode())
    return cipher.encrypt(user_id.encode())
def decoder(hash: bytes):
    cipher = Fernet(key.encode())
    return cipher.decrypt(hash).decode()

async def get_info(data):
    url = f"https://tonapi.io/v2/accounts/{data['account_id']}/events/{data['tx_hash']}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

