import json
import matplotlib.pyplot as plt 
file = 'USD.json'
with open(file, encoding = 'ascii') as k:
    text = k.read()
    currency_str= json.loads(text)

names = ['JPY', 'ALL', 'ARS','DZD']
values = [currency_str["rates"]['JPY'], currency_str["rates"]['ALL'], currency_str["rates"]['ARS'], currency_str["rates"]['DZD']]