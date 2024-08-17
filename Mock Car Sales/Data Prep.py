# Importing package
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importing Car Sales Data
car_mock = pd.read_csv(
    'Cars Mock Data.csv'
)

# Cleaning column names
car_mock.columns = car_mock.columns\
    .str.lower()

car_mock.columns = car_mock.columns\
    .str.replace(' ', '_')

car_mock.columns = car_mock.columns\
    .str.replace('-', '_')

# Testing for null values
assert car_mock.isna().sum().sum() == 0

# Converting "puchase_date" to datetime
car_mock['purchase_date'] = pd.to_datetime(car_mock['purchase_date'], dayfirst=True).dt.date

# Exporting as a csv file for analysis
car_mock.to_csv('Car Mock Sales Data.csv')

brand_pop = car_mock.groupby('make')['model'].count().sort_values(ascending=False).reset_index()

sns.barplot(
    data = brand_pop,
    x = 'make',
    y = 'model',
    order = brand_pop['make']
)

plt.xticks(rotation=90)
plt.show()