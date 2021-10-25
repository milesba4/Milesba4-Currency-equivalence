import json
import matplotlib.pyplot as plt 
file = 'USD.json'
with open(file, encoding = 'ascii') as k:
    text = k.read()
    currency_str= json.loads(text)


count = {'JPY': 114, 'ALL': 104.69, 'ARS': 99.38, 'DZD': 137.19}

names = ['JPY', 'ALL', 'ARS','DZD']
values = [currency_str["rates"]['JPY'], currency_str["rates"]['ALL'], currency_str["rates"]['ARS'], currency_str["rates"]['DZD']]




}
plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)

plt.show()