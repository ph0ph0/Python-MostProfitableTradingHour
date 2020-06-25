import pandas as pd
import matplotlib.pyplot as plot
import sys  # Only needed to determine Python version
import matplotlib  # Only needed to determine Matplotlib version number
import chardet
from datetime import date

# Enable inline plotting
# %matplotlib inline

print('Python Version: ' + sys.version)
print('Pandas Version: ' + pd.__version__)
print('Matplotlib Version: ' + matplotlib.__version__)

Location = r'/Users/Pho/Documents/Freelance/Projects/GrahamStockTradingPlatform/Code/TradingScripts/MostProfitableHour/Raw/2020_06_25_Set1.csv'
Headers = ['No', 'Time', 'Type', 'Order', 'Size',
           'Price', 'SL', 'TP', 'Profit', 'Balance']
df = pd.read_csv(Location, names=Headers,  encoding="ISO-8859-1")


# df.info(verbose=True)

# Remove unnecessary columns
del df["SL"]
del df["TP"]
del df["Balance"]
del df["Size"]

# Create arrays to hold extracted data
OrderNumberArray = []
OrderTypeArray = []
OpenTimeArray = []
CloseTimeArray = []
OpenPriceArray = []
ClosePriceArray = []
ProfitArray = []

# Extract data
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

data = {"OrderNumber": OrderNumberArray, "OrderType": OrderTypeArray, "OpenTime": OpenTimeArray,
        "CloseTime": CloseTimeArray, "OpenPrice": OpenPriceArray, "ClosePrice": ClosePriceArray, "Profit": ProfitArray}

columnNames = ["OrderNumber", "OrderType", "OpenTime",
               "CloseTime", "OpenPrice", "ClosePrice", "Profit"]

# Overwrite existing dataframe
df = pd.DataFrame(data, columns=columnNames)

todaysDate = date.today().strftime("%Y_%m_%d")
newCSVName = "Raw/" + todaysDate + "_Processed_Set1"
df.to_csv(newCSVName, index=False)

# Convert date columns to datetime
df["OpenTime"] = pd.to_datetime(df["OpenTime"], format="%Y.%m.%d %H:%M")
df["CloseTime"] = pd.to_datetime(df["OpenTime"], format="%Y.%m.%d %H:%M")

# Extract Open/CloseTime and convert to DayOfWeek
OpenTimeDayArray = []
CloseTimeDayArray = []
for row in df.itertuples():
    OpenTimeDayArray.append(row[3].dayofweek)
    CloseTimeDayArray.append(row[4].dayofweek)

df.insert(3, "OrderOpenDay", OpenTimeDayArray)
df.insert(5, "OrderCloseDay", CloseTimeDayArray)
print(df)
# print(df["OpenTime"].dt.dayofweek)
