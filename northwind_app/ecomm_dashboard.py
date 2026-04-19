from utils import get_conn,get_table_data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

engine = get_conn()
sns.set_theme(style="whitegrid")
colors = sns.color_palette('pastel')


orders_df = get_table_data("Orders",engine)

# print(orders_df.head())

customers_df = get_table_data("Customers",engine)
# print(customer_df.head())

merged_df = pd.merge(
        orders_df, 
        customers_df, 
        on='CustomerID', 
        how='inner'
    )

# print(merged_df.head())

order_counts = merged_df.groupby(['CustomerID', 'ContactName']).agg(
    total_orders=('OrderID', 'count')
).reset_index()

# Sort by the highest number of orders
order_counts = order_counts.sort_values(by='total_orders', ascending=False)

print(order_counts.head())

top_customers = order_counts.head(10)

# 3. Create the pie chart using Matplotlib
plt.figure(figsize=(10, 7))
plt.pie(
    top_customers['total_orders'], 
    labels=top_customers['ContactName'], 
    colors=colors, 
    autopct='%1.1f%%',   # Show percentages
    startangle=140,      # Rotate for better starting orientation
    pctdistance=0.85     # Distance of percentage labels from center
)

# 4. Draw a circle at the center to turn it into a 'Donut' chart (optional but cleaner)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Order Distribution by Top Customers')
plt.axis('equal') 
plt.tight_layout()
plt.savefig('order_distribution_pie_chart.png')
