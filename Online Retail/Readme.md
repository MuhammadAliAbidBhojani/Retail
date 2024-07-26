# Online Retail Analysis
This is a small project in which I import, clean and analyse data


# Data Preparation:
```python
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

# Changing "ratings", "Gender", "income", "customer_segment", "feedback", "shipping_method",
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
```

Now lets use this newly prepared data for analysis!

First lets see which category makes the most amount of sales:
!['Orders per Category'](Orders%20per%20Category.png)

The above visual shows that the "Electronic" category has the most orders, making up 23% of Overall orders

Now lets see which month has the most orders:
!['Orders per Month'](Orders%20per%20Month.png)

This visual shows that the month of "April" has the most orders overall.
It can also be seen that the number of orders take a dive in February followed by March
and only rises back up in April

Now lets see which shipping method is more common:
!['Orders per Shipping Method'](Shipping%20Method%20Proportions.png)

It can be seen that all shipping methods have roughly equal proportions.

Now lets see which country has more orders:
!['Orders per Country'](Orders%20per%20Country.png)

The above visual shows that the United States have the most orders overall,
making up around 31% or total orders

Lets take a look at the brands USA orders from most:
!['Orders per Brand Name'](Orders%20per%20Brand%20Name.png)

It can be seen that United States orders products from "Pepsi" alot more than any other brand
United States also orders the most products from "Pepsi"

Now lets see which age group orders more often:
!['Orders py Age'](Orders%20by%20Age.png)

It's obvious in the above visual that the age group 19-29 appears more often than others.