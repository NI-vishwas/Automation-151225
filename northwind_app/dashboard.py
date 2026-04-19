import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv() 

# 1. Page Configuration
st.set_page_config(page_title="Northwind Sales Dashboard", layout="wide")

# 2. Database Connection with Caching
# We use @st.cache_resource for the engine and @st.cache_data for queries
@st.cache_resource
def get_engine():
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    return create_engine(f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}/{db_name}")

@st.cache_data
def load_data(_engine):
    orders = pd.read_sql("SELECT * FROM Orders", _engine)
    customers = pd.read_sql("SELECT * FROM Customers", _engine)
    merged = pd.merge(orders, customers, on='CustomerID', how='inner')
    return merged

# 3. Main Logic
st.title("🚢 Northwind Customer Orders Dashboard")

try:
    engine = get_engine()
    df = load_data(engine)

    # Sidebar Filters
    st.sidebar.header("Filter Data")
    selected_country = st.sidebar.multiselect(
        "Select Country:", options=df["Country"].unique(), default=df["Country"].unique()[:5]
    )
    
    filtered_df = df[df["Country"].isin(selected_country)]

    # Metrics Row
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Orders", len(filtered_df))
    col2.metric("Unique Customers", filtered_df["CustomerID"].nunique())
    # col3.metric("Avg Freight Cost", f"${filtered_df['Freight'].mean():.2f}")

    # Visualizations Row
    left_chart, right_chart = st.columns(2)

    with left_chart:
        st.subheader("Orders by Customer")
        order_counts = filtered_df.groupby("ContactName")["OrderID"].count().sort_values(ascending=False).head(10)
        
        fig, ax = plt.subplots()
        sns.barplot(x=order_counts.values, y=order_counts.index, palette="viridis", ax=ax)
        ax.set_xlabel("Number of Orders")
        st.pyplot(fig)

    with right_chart:
        st.subheader("Order Distribution")
        fig2, ax2 = plt.subplots()
        ax2.pie(order_counts, labels=order_counts.index, autopct='%1.1f%%', startangle=140)
        ax2.axis('equal')
        st.pyplot(fig2)

    # Data Table
    st.subheader("Raw Order Data")
    st.dataframe(filtered_df)

except Exception as e:
    st.error(f"Error connecting to database: {e}")