import os
import re
import time
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from winotify import Notification, audio
from attributes import *
from account import Account
from tweet import Tweet
from logger import Logger

BASE_URL = 'https://twitter.com'
ALERT_ID = 'Tweet Alert'
ALERT_ACTION = 'View Tweet'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
TWITTER_GMT_SECONDS = 7200

def scraper(account: Account) -> None:
    Logger.scrapping_started(account.name)
    options = Options()
    options.headless = True
    driver = webdriver.Edge(options)
    driver.set_window_size(1920, 1080)
    driver.get(f"{BASE_URL}/{account.name}")

    time.sleep(1)
    resp = driver.page_source
    driver.close()

    soup = BeautifulSoup(resp, 'html.parser')
    tweets = soup.find_all('article', TWEET_ATTRS)

    for tweet in tweets:
        tweet_iso_date = tweet.find('time').attrs[DATETIME]

        if (is_latest_tweet(tweet_iso_date, Account.to_seconds(account.lifespan))):
            author = tweet.find('span', TWEET_AUTHOR_ATTRS).text
            text = tweet.find('div', TWEET_TEXT_ATTRS).text
            link = tweet.find('time').parent.attrs[LINK]

            formatted_text = os.linesep.join([s for s in text.splitlines() if s])
            formatted_link = f'{BASE_URL}{link}'
            tweet_data = Tweet(author, account.name, formatted_text, formatted_link)

            if account.keywords == '*':
                alert(tweet_data)
                continue
        
            tweet_keywords = find_keywords(formatted_text, account.keywords)

            if tweet_keywords:
                alert(tweet_data, tweet_keywords)
    
    Logger.scrapping_ended(account.name, account.interval)

def alert(tweet: Tweet, keywords: str | list[str] = []) -> None:
    toast = Notification(ALERT_ID, f'{tweet.author} | {tweet.symbol}', tweet.text)
    toast.add_actions(ALERT_ACTION, tweet.link)
    toast.set_audio(audio.SMS, loop=True)
    
    if keywords:
        toast.title = f'{tweet.author} | {tweet.symbol} [{" ".join(keywords).upper()}]'
    
    toast.show()

def is_latest_tweet(iso_date: str, lifespan: int) -> bool:
    tweet_time = pd.to_datetime(iso_date, format = ISO_FORMAT)
    current_time =  pd.to_datetime(datetime.now().strftime(DATETIME_FORMAT))
    time_diff = current_time - tweet_time
    
    return time_diff.total_seconds() - TWITTER_GMT_SECONDS <= lifespan

def find_keywords(text: str, keywords: list[str]) -> list[str]:
    words = re.sub('\W+', ' ', text).lower()
    keywords_set = set([keyword.lower() for keyword in keywords])

    return list(set(words.split(' ')) & keywords_set)
