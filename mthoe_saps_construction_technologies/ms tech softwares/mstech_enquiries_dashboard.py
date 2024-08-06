import streamlit as st
import pandas as pd
import plotly.express as px
import time
from PIL import Image

# Read the Excel file
df = pd.read_excel('ms tech softwares/databases/enquiries.xlsx')

# Create the app layout
st.title('Enquiries Dashboard')

# Add filtering mechanisms in the sidebar
#st.sidebar.subheader('Filters')

filter_cols = ['Full Name', 'Surname', 'Company Name', 'Province', 'Services', 'Total Charge']
filters = {}

with st.sidebar:
    image = Image.open("ms tech softwares/vids and img/logo3.png")
    st.image(image, use_column_width=False, width=250)
    st.sidebar.subheader('Filters')
    for col in filter_cols:
        if col == 'Total Charge':
            min_charge = st.slider('Minimum Total Charge', float(df['Total Charge'].min()), float(df['Total Charge'].max()), float(df['Total Charge'].min()))
            max_charge = st.slider('Maximum Total Charge', float(df['Total Charge'].min()), float(df['Total Charge'].max()), float(df['Total Charge'].max()))
            filters[col] = (min_charge, max_charge)
        else:
            filters[col] = st.multiselect(f'Filter by {col}', df[col].unique())

# Filter the data based on the selected filters
filtered_df = df.copy()
for col, values in filters.items():
    if col == 'Total Charge':
        filtered_df = filtered_df[(filtered_df['Total Charge'] >= values[0]) & (filtered_df['Total Charge'] <= values[1])]
    else:
        filtered_df = filtered_df[filtered_df[col].isin(values)]

# Display the filtered data
st.subheader('Filtered Data')
st.dataframe(filtered_df)

# Create visualizations
st.subheader('Visualizations')

# Time series bar graph with play and pause button
fig1 = px.bar(filtered_df.groupby(pd.to_datetime(filtered_df['Timestamp']).dt.date)['Total Charge'].sum().reset_index(), x='Timestamp', y='Total Charge', title='Total Charge over Time')
fig1.update_layout(xaxis_tickformat='%Y-%m-%d')

# Add play and pause button in columns
col1, col2 = st.columns(2)
with col1:
    play_state = st.button('Play')
with col2:
    pause_state = st.button('Pause')

# Animate the plot
if play_state:
    for i in range(len(fig1.data[0].x)):
        fig1.layout.xaxis.range = [fig1.data[0].x[i], fig1.data[0].x[i]]
        st.plotly_chart(fig1, use_container_width=True)
        time.sleep(0.5)
        if pause_state:
            break
else:
    st.plotly_chart(fig1, use_container_width=True)

# Pie chart of services
services_count = filtered_df['Services'].value_counts()
fig2 = px.pie(services_count, values=services_count.values, names=services_count.index, title='Services Breakdown')
st.plotly_chart(fig2, use_container_width=True)

# Bar chart of total charge by province
fig3 = px.bar(filtered_df.groupby('Province')['Total Charge'].sum().reset_index(), x='Province', y='Total Charge', title='Total Charge by Province')
st.plotly_chart(fig3, use_container_width=True)