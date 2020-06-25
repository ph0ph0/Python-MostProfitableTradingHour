import pandas as pd
import matplotlib.pyplot as plot
import sys  # Only needed to determine Python version
import matplotlib  # Only needed to determine Matplotlib version number
import chardet

# Enable inline plotting
# %matplotlib inline

print('Python Version: ' + sys.version)
print('Pandas Version: ' + pd.__version__)
print('Matplotlib Version: ' + matplotlib.__version__)

Location = r'/Users/Pho/Documents/Freelance/Projects/GrahamStockTradingPlatform/Code/TradingScripts/MostProfitableHour/Raw/2020_06_25_Set1.csv'
Headers = ['No', 'Time', 'Type', 'Order', 'Size',
           'Price', 'SL', 'TP', 'Profit', 'Balance']
df = pd.read_csv(Location, names=Headers,  encoding="ISO-8859-1")

# print(df)
# df.info(verbose=True)
del df["SL"]
del df["TP"]
del df["Balance"]
del df["Size"]

data = {}

nDF = pd.DataFrame(data, columns=['First Column Name', 'Second Column Name'])

OrderNumberArray = []
OrderTypeArray = []
OpenTimeArray = []
CloseTimeArray = []
OpenPriceArray = []
ClosePriceArray = []
ProfitArray = []

for row in df.itertuples():
    if (row[0] % 2) == 0:
        OrderNumberArray.append(row[4])
        OrderTypeArray.append(row[3])
        OpenTimeArray.append(row[2])
        OpenPriceArray.append(row[5])
    if (row[0] % 2) != 0:
        CloseTimeArray.append(row[2])
        ClosePriceArray.append(row[5])
        ProfitArray.append(row[6])

print(ProfitArray)
# print(df["Order"] == 1)
