import asyncio
import schedule
import time
from main import update_dashboard

from src.log_setup import logging
logger = logging.getLogger(__name__)

def start_scheduler():
   
    schedule.every().day.at("12:20").do(lambda: asyncio.run(update_dashboard()))
    logger.info('Scheduler running...')

    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == '__main__':
    start_scheduler()