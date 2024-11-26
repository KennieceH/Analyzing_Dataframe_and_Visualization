import numpy.random
import pandas as pd

"""
CAP 4784: Lab 5 – Analyzing items Dataframe
<p>
This program analyzes the items.csv by loading the csv into a dataframe 
and using panda dataframe commands.
<p>
@author <Kenniece Harris>
@version <4/04/2023>
"""


items = pd.read_csv('C:\\Users\\kikic\\Downloads\\items.csv')

# Displays the first seven rows of the dataframe
print(items.head(7))

# Displays the last seven rows of the dataframe
print(items.tail(7))

# Displays description of items DataFrame using “info” method
print(items.info(verbose=True))

# Displays the number of rows and columns in items DataFrame
print('Items DataFrame has {0} rows and {1} columns'.format(len(items), len(items.columns)))

# Displays descriptive statistics for Bottle_Cost using “describe” method
print(items['Bottle_Cost'].describe())

# Adds a new Column ‘bottle_profit_margin’ to items DataFrame
dfBPM = (items['Bottle_Retail_Price'] - items['Bottle_Cost']) / items['Bottle_Retail_Price']
items['bottle_profit_margin'] = dfBPM
print(items.head(10))

# Deletes/drops rows 5-15 from items DataFrame
print(items.drop(items.index[5:15]).head(25))

# Displays items that have Bottle_Volume_ml> 750 and more than 12 pack and bottle_profit_margin more than 0.3
print(items[(items['Bottle_Volume_ml'] > 750) & (items['Pack'] > 12) & (items['bottle_profit_margin'] > 0.3)])

# Displays the number of energy drinks ('Category' ='Energy Drink')
print('The number of Energy Drink {0}'.format(len(items.loc[items['Category'] == 'Energy Drink'])))

# Creates a new DataFrame ‘items2’ and Adds a new Column ‘QTY’ to the data frame
items2 = pd.DataFrame(items[['Item_id', 'Item_Description', 'Bottle_Retail_Price', 'bottle_profit_margin']])
items2['QTY'] = numpy.random.randint(low=0, high=100, size=len(items2))
print(items2.head(7))

