import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load Excel data
df = pd.read_excel("Book2.xlsx")

# Clean column names and values
df.columns = df.columns.str.strip()
df = df[pd.to_numeric(df['Year'], errors='coerce').notnull()]
df['Year'] = df['Year'].astype(int)
df['Total'] = df['Total'].astype(str).str.replace(',', '')
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

# Group by year and category
grouped = df.groupby(['Year', 'Category'])['Total'].sum().reset_index()
pivot_df = grouped.pivot(index='Year', columns='Category', values='Total').sort_index()
yoy_df = pivot_df.pct_change() * 100
yoy_df = yoy_df.round(2)

# Streamlit UI
st.set_page_config(page_title="Vehicle Dashboard", layout="centered")

# Title and subtitle
st.title("🚗📈 India Vehicle Registration Dashboard (2021–2025)")
st.markdown("Get investor insights by tracking **2W, 3W, 4W** trends and YoY growth.")

# Select category
selected_category = st.selectbox("📂 Select Vehicle Category", pivot_df.columns)

# Summary Metric
latest_year = pivot_df.index.max()
previous_year = latest_year - 1

current_value = pivot_df[selected_category].loc[latest_year]
previous_value = pivot_df[selected_category].loc[previous_year]
diff = current_value - previous_value
delta_percent = ((diff) / previous_value) * 100

st.metric(
    label=f"Registrations in {latest_year}",
    value=f"{int(current_value):,}",
    delta=f"{delta_percent:.2f}%" if not pd.isna(delta_percent) else "N/A"
)

# Line chart - registrations over time
st.subheader(f"📈 Total Registrations for {selected_category}")
fig, ax = plt.subplots()
pivot_df[selected_category].plot(kind='line', marker='o', color='teal', linewidth=2, ax=ax)
ax.set_ylabel("Registrations")
ax.set_xlabel("Year")
st.pyplot(fig)

# Bar chart - YoY growth
st.subheader(f"📊 Year-over-Year Growth (%) for {selected_category}")
fig2, ax2 = plt.subplots()
yoy_df[selected_category].plot(kind='bar', color='salmon', ax=ax2)
ax2.set_ylabel("YoY Growth %")
ax2.set_xlabel("Year")
st.pyplot(fig2)

# Data tables
st.subheader("📄 Data Table - Total Registrations")
st.dataframe(pivot_df)

st.subheader("📈 Data Table - YoY Growth %")
st.dataframe(yoy_df)
