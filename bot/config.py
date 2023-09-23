import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "6215788567:AAFuh8O6xVK5lZutvY0_Oe_uUlJTrGE6Fc8")
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH', "9364c24fd2f5a74afc436c1f140225f5")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID', "22924434"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
