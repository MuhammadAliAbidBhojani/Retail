# Mock Car Sales!
In this project I will Import, Clean and Analyse Mockaroo Car Sales Data.

*note that this is a "fake dataset" and is being used for demonstration purposes only*

# Data Preparation
```python
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
```

# Data Visualization

Lets analyse the data to find any trends and insights!

First lets see which brand made the most sales:
!['Numbers of Cars Sold per Brand'](Number%20of%20Cars%20Sold%20per%20Brand.png)

It seems that ford has sold the most cars overall! But does it have the highest Price on average?

!['Average Price per Brand'](Average%20Sales%20Price%20per%20Brand%20(Top%2010).png)

This visual shows the Top 10 brands with the highest sales price on average. It also shows the average resale price of the brands

It seems that MG had the biggest loss in value. While Hillman had the smallest value loss.

But which brand had the biggest loss?
!['Loss in Value per Brand'](Average%20Loss%20in%20Price%20per%20Brand%20(Top%2010).png)

It seems that MG did have the biggest loss overall. Hillman also had a great loss, But kept the highest average resale price due to a higher sales price

Now lets take a look at all the brands and their respective sales and resale
!['Change in Price per Brand'](Change%20in%20Price%20per%20Brand.png)

It seems that most brands tend to stay close to the average sales price, While only a few go higher or lower

MG also happens to be the only brand with the lowest resale price, while Corbin has the lowest sales price.