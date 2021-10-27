import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#graph 1
gas_data = pd.read_csv('state-gas-price.csv')

la, = plt.plot(gas_data['Year'], gas_data['Los Angeles'], label='Los Angeles')
cle, = plt.plot(gas_data['Year'], gas_data['Cleveland'], label='Cleveland')

plt.xlabel("Year")
plt.ylabel("Price ($)")
plt.title("Price of gas over time in different states")
plt.legend(labels=['Los Angeles', 'Cleveland'])

plt.show()

#graph 2
bigmac_data = pd.read_csv('bigmac.csv')

plt.bar(bigmac_data.Country[:4], bigmac_data.Price[:4])

plt.xlabel("Country")
plt.ylabel("Price ($)")
plt.title("Price of big macs in different countries")

plt.show()






