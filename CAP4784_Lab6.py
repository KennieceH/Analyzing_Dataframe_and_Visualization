import datetime
import matplotlib.pyplot as plt
import pandas as pd
"""
CAP 4784: Lab 6 – Data Cleaning and Visualization
<p>
This purpose of this program is to convert the csv file "Lab6.csv" to a dataframe
(items) that is then used to clean the data via removing duplicates and NaN values
as well as visualize the results in a bar chart, scatterplot, and histogram.
<p>
@author <Kenniece Harris>
@version <4/25/2023>
"""

"""
The purpose of the new_date method is to generate a new date for the 
years in contained in the birth_date column that are greater than 2023.
The new date is generated by subtracting 100 from the year if it is 
greater than 2023.
"""


def new_date(date):
    if date.year == 2023 and date.month == 7:
        year = 2023 - 100
    elif date.year > 2023:
        year = date.year - 100
    else:
        year = date.year
    return datetime.date(year, date.month, date.day)


# load in csv to a dataframe called items.
items = pd.read_csv('Lab6.csv')

# Q1: Displays the first ten rows of the dataframe
print(items.head(10))

# display all column names
print('Data Frame Columns ->')
print(list(items.columns.values))

# Q2: removal of duplicate rows in the dataframe
print('Length of the DataFrame before dropping duplicates -> {0}'.format(len(items)))
items = items.drop_duplicates(keep='first')
print('Length of the DataFrame after dropping duplicates -> {0}'.format(len(items)))

# Q3: Display unique eye color column + counts
print('Unique Eye Colors ->')
print(items['Eye color'].unique())
print(items.value_counts('Eye color'))

# Q4: Display count of NaN values for each column
print('Count of NaN Values')
print(items.isna().sum())

# Fill NaN values for each column
items = items.fillna(value={'Gender': 'Male', 'Eye color': 'blue', 'Hair color': 'Black', 'Skin color': 'white',
                            'Weight': items['Weight'].mean()})
print(items)

# Add column 'dob' and change dates to datetime format
items['dob'] = pd.to_datetime(items['birth_date'], format='%m/%d/%y')
# Fix dates that are greater than 2023
items['dob'] = pd.to_datetime(items['dob'].apply(new_date))

# Q5: add the age column to the dataframe
items['age'] = 2023 - items['dob'].dt.year

# Q6: Separate day, month, and year in birthdate in new columns
items['day'] = items['dob'].dt.day
items['month'] = items['dob'].dt.month
items['year'] = items['dob'].dt.year

# Q7: Create subset of dataframe grouping year on gender
grouped = items['Gender'].groupby(items['year'])
print(grouped.size())

# Q8: plot hair color counts (bar chart)
plotdata = items['Hair color'].value_counts()
plotdata.plot(kind='bar')
plt.show()

# Q9: plot weight vs. height (scatterplot)
plotdata2 = items.plot.scatter(x='Weight', y='Height')
plt.show()

# Q10: plot age (histogram)
plotdata3 = items['age'].plot.hist(bins=15)
plt.show()






