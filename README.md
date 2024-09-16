# Flight Analytics Project


Developer: Syed Mansoor

Technology Stack: MySQL, Python, Streamlit, Plotly

# Project Overview

The Flight Analytics Project is an interactive data analytics tool designed to analyze flight data and provide insights into various flight-related metrics such as flight frequency, price distribution, and duration. It allows users to search for flights between cities, view specific flight details, and explore in-depth visualizations to gain insights into pricing trends, busiest airports, and more.

This project utilizes Streamlit for building the user interface, Plotly for dynamic data visualizations, and MySQL for querying flight data.

# Features
1. Check Flights : The Check Flights section allows users to search for available flights between two cities. The following details are displayed:

- Airline: Name of the airline operating the flight.
- Route: The flight route between the source and destination.
- Departure Time: Time of departure from the source city.
- Duration: Total flight duration.
- Price: The ticket price for the flight.
2. Flight Analytics
The Analytics section includes several interactive visualizations to provide insights into the flight data:

- Airline Frequency: A pie chart visualizing the number of flights operated by each airline.
- Busy Airports: A bar chart showing the busiest airports based on flight traffic.
- Daily Flight Frequency: A line chart showing the number of flights on different days, providing insight into daily flight trends.
- Price Distribution by Airline: A box plot showing the distribution of flight prices for different airlines.
- Flight Duration vs. Price: A scatter plot analyzing the relationship between flight duration and price.
- Total Stops Distribution: A bar chart displaying the distribution of the number of stops across flights.
- Price by Time of Day: A bar chart showcasing the average flight prices based on the time of day (departure hour).
3. Project Overview
In this section, the app provides a detailed overview of the project, explaining its goals, insights, and possible future enhancements.

The data for this project is stored in a MySQL database named flights. The database contains flight-related information such as:
# Data Source
- Airline
- Source and Destination
- Departure Time
- Duration
- Price
- Total Stops

# Installation Guide
Prerequisites
- Python 3.x
- MySQL
- Streamlit
- Plotly

# MySQL Database Setup
1. Ensure MySQL is installed on your system.
2. Create a database called flights.
3. Import your flight data into a table named flight.

# Setting Up the Project

1. Clone the repository to your local machine:




git clone https://github.com/yourusername/flight-analytics.git



2. Install the required dependencies using pip:


pip install streamlit mysql-connector-python plotly pandas
3. Set up your MySQL connection in the db_helper.py file:
'''
self.conn = mysql.connector.connect(
    host='127.0.0.1',
    user='username',
    password='your_password',
    database='your_database_name'
)
'''


4. Run the Streamlit app:

streamlit run app.py

# Usage
## Navigating the App
1. Open the app in a browser via the Streamlit interface.

2. On the sidebar, choose between:

- Check Flights: Search for flights between two cities.
- Analytics: Explore flight data through interactive visualizations.
3. In the Check Flights section:

- Select your Source and Destination cities.
- Click Search to view the available flights.
4. In the Analytics section:

- Explore various visualizations that provide insights into airline frequency, pricing trends, flight duration, and more.

# Contact
For more information or inquiries about this project, feel free to reach out:

Developer: Syed Mansoor

Email: saeedmansoor56@gmail.com

LinkedIn: www.linkedin.com/in/syed-mansoor-88404a1b0



# Special thanks to campusx