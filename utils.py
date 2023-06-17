import time
from threading import Thread
from itertools import islice
from account import Account
from scraper import scraper

def get_accounts() -> list[Account]:
    with open('accounts.txt', 'r') as file:
        return [Account(line) for line in islice(file, 2, None)]

def run_scraper(account: Account):
    while True:
        thread = Thread(target=scraper, args=(account,))
        thread.start()
        time.sleep(Account.to_seconds(account.interval))