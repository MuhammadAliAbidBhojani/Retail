# Importing pandas
import pandas as pd

# Importing Retail Data
online_retail = pd.read_csv(
    'new_retail_data.csv'
)

# Cleaning the column names for convenience
online_retail.columns = online_retail.columns\
    .str.lower()

# There are a few null values in the data, However due to the size of the data the Null values are insignificant
online_retail = online_retail.dropna()

# Dropping duplicated entries "transaction_id"
online_retail = online_retail.drop_duplicates(subset=['transaction_id'])

# Converting "date" column to datetime
online_retail['date'] = pd.to_datetime(online_retail['date']).dt.date

# Converting unnecessary floats to integers
online_retail['phone'] = online_retail['phone']\
    .astype('int')
online_retail['zipcode'] = online_retail['zipcode']\
    .astype('int')
online_retail['age'] = online_retail['age']\
    .astype('int')
online_retail['year'] = online_retail['year']\
    .astype('int')
online_retail['total_purchases'] = online_retail['total_purchases']\
    .astype('int')
online_retail['ratings'] = online_retail['ratings']\
    .astype('int')

#Changing "ratings", "Gender", "income", "customer_segment", "feedback", "shipping_method",
# "payment_method" and "order_status" column to Categorical data type

online_retail['ratings'] = online_retail['ratings']\
    .astype('category')
online_retail['gender'] = online_retail['gender']\
    .astype('category')
online_retail['income'] = online_retail['income']\
    .astype('category')
online_retail['customer_segment'] = online_retail['customer_segment']\
    .astype('category')
online_retail['feedback'] = online_retail['feedback'] \
    .astype('category')
online_retail['shipping_method'] = online_retail['shipping_method'] \
    .astype('category')
online_retail['payment_method'] = online_retail['payment_method'] \
    .astype('category')
online_retail['order_status'] = online_retail['order_status'] \
    .astype('category')

# Creating an "hour" column using "time" column
hour = []
for time in online_retail['time']:
    hour.append(time.split(':')[0])

online_retail['hour'] = hour

# Saving the prepared data into a csv file for analysis
online_retail.to_csv('Online Retail Cleaned.csv')
