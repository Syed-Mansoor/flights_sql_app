import streamlit as st
from db_helper import DB
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Initialize the database connection
db = DB()

# Sidebar for navigation
st.sidebar.title('Flights Analytics')
user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

# Check Flights
if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    # Fetch city names for dropdown
    city = db.fetch_city_names()

    with col1:
        source = st.selectbox('Source', sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)

# Analytics
elif user_option == 'Analytics':
    # Airline Frequency Pie Chart
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        )
    )
    st.header("Airline Frequency Pie Chart")
    st.plotly_chart(fig)

    # Busy Airport Bar Chart
    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1,
        labels={'x': 'City', 'y': 'Frequency'},
        title='Busy Airports'
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Daily Flight Frequency Line Chart
    date, frequency2 = db.daily_frequency()
    fig = px.line(
        x=date,
        y=frequency2,
        labels={'x': 'Date', 'y': 'Frequency'},
        title='Daily Flight Frequency'
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Price Distribution by Airline (Box Plot)
    df_price_distribution = db.fetch_price_distribution_by_airline()
    fig = px.box(
        df_price_distribution,
        x='Airline',
        y='Price',
        title='Price Distribution by Airline'
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Flight Duration vs. Price (Scatter Plot)
    df_duration_vs_price = db.fetch_duration_vs_price()
    fig = px.scatter(
        df_duration_vs_price,
        x='Duration',
        y='Price',
        title='Flight Duration vs. Price'
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Total Stops Distribution (Bar Chart)
    df_total_stops = db.fetch_total_stops_distribution()
    fig = px.bar(
        df_total_stops,
        x='Total_Stops',
        y='Count',
        title='Total Stops Distribution'
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Price by Time of Day (Bar Chart)
    df_price_by_time_of_day = db.fetch_price_by_time_of_day()
    fig = px.bar(
        df_price_by_time_of_day,
        x='Hour',
        y='Avg_Price',
        title='Price by Time of Day'
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# Default Page
else:
    st.title('Tell about the project')

# Close the database connection
db.close()
