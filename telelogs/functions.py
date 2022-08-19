from urllib import response
import requests
import os

from dotenv import load_dotenv

load_dotenv()


def send_massage(text:str):
    hash_key = os.environ.get("HASH_KEY")
    chat_id = os.environ.get("CHAT_ID")
    url=f"https://api.telegram.org/bot{hash_key}/sendMessage?chat_id={chat_id}&text={text}"
    return requests.get(url)


def retrieve_chat_id():
    hash_key = os.environ.get("HASH_KEY")
    url=f"https://api.telegram.org/bot{hash_key}/getUpdates"
    response = requests.get(url)
    result = response.json()["result"][0]["message"]["chat"]["id"]
    os.system(f'echo "HASH_KEY={hash_key}\nCHAT_ID={result}" > .env')