import time
import sys
import json
import requests
from  yahoo_fin import stock_info as si
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
from operator import itemgetter

lastPrice = 0
while True:
    sPrice = si.get_live_price("gme")
    price = round(sPrice, 2)
    pStr = str(price)
    if price >= lastPrice:
        cprint(figlet_format('GME: ' + pStr, font='starwars'),
            'yellow', 'on_green', attrs=['bold'])
    elif price < lastPrice:
        cprint(figlet_format('GME: ' + pStr, font='starwars'),
            'yellow', 'on_red', attrs=['bold'])
    time.sleep(3.5)
    lastPrice = price
