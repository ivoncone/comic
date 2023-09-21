from api.settings import MARVEL_BASE_URL, MARVEL_KEY, MARVEL_PRIV_KEY
import requests
import time
import hashlib


def payload():
    public_key = MARVEL_KEY
    private_key = MARVEL_PRIV_KEY
    timestamp = str(int(time.time()))
    hash_value = hashlib.md5((timestamp + private_key + public_key).encode()).hexdigest()
    params = {
                'apikey': public_key,
                'ts': timestamp,
                'hash': hash_value
    }
    return params