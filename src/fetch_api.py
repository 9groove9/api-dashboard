import httpx
import asyncio

from src.log_setup import logging
logger = logging.getLogger(__name__)


async def fetch_one(url, params):
    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params)
        return {'name': url, 'data': r.json()}

async def fetch_all(api_requests):
    task = [fetch_one(r['url'], r['params']) for r in api_requests]
    result = await asyncio.gather(*task, return_exceptions=True)
    logger.info('Data fetched successfully')
    return result  