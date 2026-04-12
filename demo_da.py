import pandas as pd 


df = pd.read_csv('house_price_prediction.csv')
# print(df.head())
print(df['Location'].unique())
# print(df.describe())

# What is the average price of listings by Location

# SELECT Location, AVG(Price) FROM house_price
# GROUP BY Location

k = df.groupby('Location')['Price'].mean()
print(k)