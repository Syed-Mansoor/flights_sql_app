import mysql.connector
import pandas as pd

class DB:
    def __init__(self):
        # Connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='9596531520',
                database='flights'
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except Exception as e:
            print(f'Connection error: {e}')

    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
            SELECT DISTINCT(Destination) FROM flight
            UNION
            SELECT DISTINCT(Source) FROM flight
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self, source, destination):
        self.mycursor.execute("""
            SELECT Airline, Route, Dep_Time, Duration, Price FROM flight
            WHERE Source = %s AND Destination = %s
        """, (source, destination))
        data = self.mycursor.fetchall()
        df = pd.DataFrame(data, columns=["Airline", "Route", "Dep_Time", "Duration", "Price"])
        return df

    def fetch_airline_frequency(self):
        self.mycursor.execute("""
            SELECT Airline, COUNT(*) FROM flight
            GROUP BY Airline
        """)
        data = self.mycursor.fetchall()
        airlines, frequencies = zip(*data)
        return airlines, frequencies

    def busy_airport(self):
        self.mycursor.execute("""
            SELECT Source, COUNT(*) AS Flight_Count FROM (
                SELECT Source FROM flight
                UNION ALL
                SELECT Destination FROM flight) t
            GROUP BY t.Source
            ORDER BY Flight_Count DESC
        """)
        data = self.mycursor.fetchall()
        cities, frequencies = zip(*data)
        return cities, frequencies

    def daily_frequency(self):
        self.mycursor.execute("""
            SELECT Date_of_Journey, COUNT(*) FROM flight
            GROUP BY Date_of_Journey
            ORDER BY Date_of_Journey
        """)
        data = self.mycursor.fetchall()
        dates, frequencies = zip(*data)
        return dates, frequencies

    def fetch_price_distribution_by_airline(self):
        self.mycursor.execute("""
            SELECT Airline, Price FROM flight
        """)
        data = self.mycursor.fetchall()
        df = pd.DataFrame(data, columns=["Airline", "Price"])
        return df

    def fetch_duration_vs_price(self):
        self.mycursor.execute("""
            SELECT Duration, Price FROM flight
        """)
        data = self.mycursor.fetchall()
        df = pd.DataFrame(data, columns=["Duration", "Price"])
        return df

    def fetch_total_stops_distribution(self):
        self.mycursor.execute("""
            SELECT Total_Stops, COUNT(*) FROM flight
            GROUP BY Total_Stops
        """)
        data = self.mycursor.fetchall()
        df = pd.DataFrame(data, columns=["Total_Stops", "Count"])
        return df

    def fetch_price_by_time_of_day(self):
        self.mycursor.execute("""
            SELECT HOUR(Dep_Time) AS Hour, AVG(Price) AS Avg_Price
            FROM flight
            GROUP BY Hour
            ORDER BY Hour
        """)
        data = self.mycursor.fetchall()
        df = pd.DataFrame(data, columns=["Hour", "Avg_Price"])
        return df

    # Additional utility methods as needed
    def close(self):
        self.mycursor.close()
        self.conn.close()
