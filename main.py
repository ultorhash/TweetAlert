import sys
sys.dont_write_bytecode = True

from threading import Thread
from utils import get_accounts, run_scraper

for account in get_accounts():
    Thread(target=run_scraper, args=(account,)).start()