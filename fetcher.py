import csv
import globalvars as gv
from datetime import datetime
import requests
import apikey as ak


def fetcher():
    gv.userin = input("Enter the stock symbol: ")
    gv.usercountry = input("Enter your country's 2-letter identifier (e.g. Canada = CA): ")
    url = "https://yh-finance.p.rapidapi.com/stock/v3/get-historical-data"
    querystring = {"symbol": f"{gv.userin}", "region": f"{gv.usercountry}"}
    response = requests.get(url, headers=ak.headers, params=querystring).json()
    keylist = ['date', 'open', 'high', 'low', 'close', 'volume', 'adjclose']
    with open(f'{gv.userin}{gv.usercountry}info.csv', 'w') as cf:
        fw = csv.writer(cf, delimiter=',')
        fw.writerow(['UNIX timestamp', 'Open', 'High', 'Low:', 'Close', 'Volume', 'Adjusted Close', 'Date'])
        for n in range(0, 252):
            row = []
            for key in keylist:
                curr = response['prices']
                num = curr[n]
                try:
                    wrt = num[key]
                    row.append(wrt)
                except KeyError:
                    wrt = ''
                    row.append(wrt)
                    pass
            ts = int(f'{row[0]}')
            dt_object = datetime.fromtimestamp(ts)
            row.append(dt_object)
            fw.writerow(row)
