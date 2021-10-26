import json
import matplotlib.pyplot as plt 
import numpy as np
file = 'USD.json'
with open(file, encoding = 'ascii') as k:
    text = k.read()
    currency_str= json.loads(text)

file2 = 'GBP.json'
with open(file2, encoding = 'ascii') as f:
    text2 = f.read()
    currency_str= json.loads(text2)


count = {'JPY': 114, 'ALL': 104.69, 'ARS': 99.38, 'DZD': 137.19}

names = ['JPY', 'ALL', 'ARS', 'DZD']
values = [114, 104.69, 99.38, 137.19]

plt.figure(1)
plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)

plt.suptitle('Currencies equivalence to 1 USD')
plt.xlabel('Currency')
plt.ylabel('Amount in currency equal to 1 USD')

plt.show()



# plt.figure(2)

# names1 = ['BOB', 'BRL', 'CNY', 'DKK']
# values1 = [9500, 7770, 8830, 8370]

# plt.figure(figsize=(9, 3))

# plt.subplot(132)
# plt.scatter(names1, values1)
# plt.suptitle('Currencies equivalence to 1000 GBP')
# plt.xlabel('Currency')
# plt.ylabel('Amt in currency equal to 1000 GBP')
# plt.show()
   