import streamlit as st
import pandas as pd
import plotly.graph_objs as go


st.title("HOUSE PRICES DATA ANALYSIS")
st.subheader('BY MUHAMMAD TAUSEEF')
st.markdown('---')

# Load your dataset
data = pd.read_csv('House_Prices_Analysis.csv')

# Sidebar title
st.sidebar.image('House.png')
st.sidebar.title("Select Your Requirements")

# Sidebar options
chart_choices = {
    "Most Sold Houses by Carpet Area": "carpet_area",
    "Average Price by Location": "location",
    "House Prices by Car Parking": "car_parking",
    "House Prices by Ownership Status": "ownership",
    "House Prices by Overlooking View": "overlooking",
    "House Prices by Furnishing": "furnishing",
    "House Prices by Transaction Type": "transaction"
}

selected_chart = st.sidebar.selectbox("Select Chart", list(chart_choices.keys()))

# Slider for price range
price_range = st.sidebar.slider("Price Range (in rupees)", 
                                min(data['Price (in rupees)']), 
                                max(data['Price (in rupees)']), 
                                (min(data['Price (in rupees)']), max(data['Price (in rupees)'])))

# Function to plot selected chart
def plot_chart(data, chart_type, price_range):
    filtered_data = data[(data['Price (in rupees)'] >= price_range[0]) & 
                         (data['Price (in rupees)'] <= price_range[1])]
    
    if chart_type == "carpet_area":
        most_sold_houses = filtered_data.groupby('Carpet Area')['Price (in rupees)'].sum().nlargest(10)
        fig = go.Figure(go.Bar(x=most_sold_houses.index, y=most_sold_houses.values))
        fig.update_layout(title='Mostly Sold Houses based on the Area of a House',
                          xaxis_title='Carpet Area', yaxis_title='Price (in rupees)')
        st.plotly_chart(fig)
    elif chart_type == "location":
        average_price_by_location = filtered_data.groupby('location')['Price (in rupees)'].mean().sort_values()
        fig = go.Figure(go.Bar(x=average_price_by_location.index, y=average_price_by_location.values,
                               marker_color='skyblue'))
        fig.update_layout(title='Average House Price by Location', xaxis_title='Location',
                          yaxis_title='Average Price (in rupees)', xaxis_tickangle=-45)
        st.plotly_chart(fig)
    elif chart_type == "car_parking":
        average_prices = filtered_data.groupby('Car Parking')['Price (in rupees)'].mean()
        fig = go.Figure(go.Bar(x=average_prices.index, y=average_prices.values, 
                               marker_color='blue'))
        fig.update_layout(title='Average House Prices by Car Parking', xaxis_title='Car Parking',
                          yaxis_title='Average Price (in rupees)')
        st.plotly_chart(fig)
    elif chart_type == "ownership":
        average_prices = filtered_data.groupby('Ownership')['Price (in rupees)'].mean()
        fig = go.Figure(go.Bar(x=average_prices.index, y=average_prices.values, 
                               marker_color='skyblue'))
        fig.update_layout(title='Average House Prices by Ownership Status', xaxis_title='Ownership Status',
                          yaxis_title='Average Price (in rupees)')
        st.plotly_chart(fig)
    elif chart_type == "overlooking":
        average_prices = filtered_data.groupby('overlooking')['Price (in rupees)'].mean()
        fig = go.Figure(go.Bar(x=average_prices.index, y=average_prices.values, 
                               marker_color='brown'))
        fig.update_layout(title='Average House Prices by Overlooking View', xaxis_title='Overlooking View',
                          yaxis_title='Average Price (in rupees)', xaxis_tickangle=-45)
        st.plotly_chart(fig)
    elif chart_type == "furnishing":
        average_prices = filtered_data.groupby('Furnishing')['Price (in rupees)'].mean()
        fig = go.Figure(go.Bar(x=average_prices.index, y=average_prices.values, 
                               marker_color=['skyblue', 'lightcoral']))
        fig.update_layout(title='Average House Prices by Furnishing', xaxis_title='Furnishing',
                          yaxis_title='Average Price (in rupees)')
        st.plotly_chart(fig)
    elif chart_type == "transaction":
        average_prices = filtered_data.groupby('Transaction')['Price (in rupees)'].mean()
        fig = go.Figure(go.Bar(x=average_prices.index, y=average_prices.values, 
                               marker_color='skyblue'))
        fig.update_layout(title='Average House Prices by Transaction Type', xaxis_title='Transaction Type',
                          yaxis_title='Average Price (in rupees)')
        st.plotly_chart(fig)

# Plot selected chart
plot_chart(data, chart_choices[selected_chart], price_range)
