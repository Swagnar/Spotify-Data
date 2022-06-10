import requests
import pandas as pd
import sqlalchemy
import sqlite3
import json
import os

from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from datetime import timedelta
from datetime import datetime

load_dotenv()
DATABASE = os.getenv("DATABASE")
USER_ID = os.getenv("USER_ID")
TOKEN = os.getenv("TOKEN")

if __name__ == "__main__":

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

    print(TOKEN)
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    yesterdayUnixTimestamp = int(yesterday.timestamp())

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterdayUnixTimestamp), headers=headers)

    data = r.json()

    print(data)