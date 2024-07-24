# Pakistan E-Commerce 2017-2019
This short project to import, clean and analyse Pakistan E-Commerce data

```python
# Importing Package
import pandas as pd

# Importing Pakistan Economy Data
cols_to_use = ['item_id', 'status', 'created_at', 'sku', 'price', 'qty_ordered', 'grand_total', 'increment_id', 'category_name_1', 'sales_commission_code', 'discount_amount', 'payment_method', 'Working Date', 'BI Status', 'Year', 'Month', 'Customer Since', 'FY', 'Customer ID']

p_economy = pd.read_csv(
    'E:/Portfolio/Retail & E-Commerce - Data & Resource/Data/Pakistan Economy/Pakistan Largest Ecommerce Dataset.csv',
    low_memory = False,
    usecols = cols_to_use
)

# Cleaning the column names
p_economy.columns = pd.Series(p_economy.columns)\
    .str.strip()\
    .str.replace(' ', '_')\
    .str.lower()

# Dropping the Empty rows from the dataset
p_economy = p_economy.dropna()

# Making sure that item_id only has unique values
assert len(p_economy) == p_economy['item_id'].nunique()

# cleaning the inconsistencies in the "status" column
status_map = {
    'complete':'received',
    'received':'received',
    'order_refunded':'order_refunded',
    'refund':'order_refunded',
    'canceled':'canceled',
    'closed':'canceled',
    'cod':'received',
    'paid':'received'
}

p_economy['status'] = p_economy['status'].map(status_map)

assert p_economy['status'].nunique() == 3

# Converting "created_at", "working_date" and "customer_since" column to datetime
p_economy['created_at'] = pd.to_datetime(p_economy['created_at']).dt.date
p_economy['working_date'] = pd.to_datetime(p_economy['working_date']).dt.date
p_economy['customer_since'] = pd.to_datetime(p_economy['customer_since']).dt.date

# Clearing the inconsistencies in the "payment_method" column
payment_map = {
    'cod':'cod',
    'customercredit':'customer_credit',
    'cashatdoorstep':'cod',
    'productcredit':'product_credit',
    'Easypay':'easypay',
    'Easypay_MA':"easypay",
    'jazzwallet':'jazzcash',
    'jazzvoucher':'voucher',
    'mcblite':'bank',
    'internetbanking':'bank',
    'marketingexpense':'Unknown',
    'financesettlement':'Unknown',
    'easypay_voucher':'voucher',
    'bankalfalah':'bank',
    'apg':'Unknown',
    'ublcreditcard':'bank',
    'Payaxis':'pay_axis',
    'mygateway':'Unknown'
}

p_economy['payment_method'] = p_economy['payment_method'].map(payment_map)

# Fixing the "year" column
p_economy['year'] = p_economy['year']\
    .astype('int')

# Fixing the "month" column
month_map = {
    1:'Jan',
    2:'Feb',
    3:'Mar',
    4:'Apr',
    5:'May',
    6:'Jun',
    7:'Jul',
    8:'Aug',
    9:'Sep',
    10:'Oct',
    11:'Nov',
    12:'Dec'
}

p_economy['month'] = p_economy['month']\
    .astype('int')\
    .map(month_map)

# Imputng the Nulls in "status" column
p_economy['status'] = p_economy['status'].fillna('Unknown')

# Saving the cleaned data for analysis
p_economy.to_csv('Pakistan Economy Cleaned.csv')
```

Now lets create some visuals with this newly cleaned data!


!['Orders per Category'](Orders%20per%20Category.png)

It seems the majority of online orders from 2017-2019 were based on Technology and Fashion.

Another thing to note is that the majority of orders placed from 2017-2019 were in the month of "*November*"

!['Orders per Month'](Orders%20per%20Month.png)

This is great insight for anyone looking to increase their sales

There are plenty of payment methods to chose from when it comes to online purchasing

!['Orders per Payment Method'](Orders%20per%20Payment%20Method.png)

Looking at the above visual. Its obvious that most people chose COD as their preferred method of payment

There are also plenty of instances of Payments through various banks, While some purchases were made through vouchers and credits.

But not all orders are completed. 

!['Orders per Status'](Status%20of%20Orders.png)

This visual shows that only 56% of orders were received by the customer, while 31.71% of overall orders were cancelled
