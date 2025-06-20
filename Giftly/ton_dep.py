import aiohttp
from config import TON_API
from databases.database import select_wallet, update_wallet


async def checker(user_id):
    adress = await select_wallet('check', user_id)
    url = f"https://tonapi.io/v2/blockchain/accounts/{adress[0].wallet_name}/transactions?limit=5"
    headers = {"Authorization": f"Bearer {TON_API}"}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers = headers) as response:
            info = await response.json()
            last_hash = adress[0].last_hash
            new_deps = []
            for x in info['transactions']:
                if x['success'] and x['hash'] != last_hash:
                    new_deps.append(float((x['credit_phase']['credit']) / 1000000000))
                if (x['hash'] == last_hash or last_hash == '0'):
                    if new_deps == []:
                        return 'dep_unknown'
                    else:
                        await update_wallet(adress[0].wallet_name, 0, 0, info['transactions'][0]['hash'])
                        return new_deps
