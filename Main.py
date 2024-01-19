import mysql.connector
import csv

from mysql.connector import Error

from menu_1 import MainMenu

# Replace these values with your MySQL server information
# host = "localhost"
# user = "root"
# password = "Imraina@03"
# database="rev"

# conn = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )

def load_data_from_csv(conn, csv_path, table_name):
        cursor = conn.cursor()
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                placeholders = ', '.join(['%s' for _ in row])
                cursor.execute(f'INSERT INTO {table_name} VALUES ({placeholders})', row)
        conn.commit()
        print(f"Data loaded into '{table_name}' table successfully.")


# Establish a connection
try:
#     conn = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )

#     if conn.is_connected():
#         print("Connected to MySQL server")

        # Create a database
        # database_name = "rev"
        # create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"

        #cursor=conn.cursor()
        
        # cursor.execute(""" 
        #                Create table if not exists signups(ID int primary key,username varchar(90) unique,passowrd varchar(90)not null,role varchar(90) not null);
        #                """)
        
#         cursor.execute("""
#     CREATE TABLE IF NOT EXISTS travel (
#     Passenger_ID INT,
#     First_Name VARCHAR(255),
#     Last_Name VARCHAR(255),
#     Gender VARCHAR(10),
#     Age INT,
#     Nationality VARCHAR(255),
#     Airport_Name VARCHAR(255),
#     Airport_Country_Code VARCHAR(5),
#     Country_Name VARCHAR(255),
#     Airport_Continent VARCHAR(255),
#     Continents VARCHAR(255),
#     Departure_Date varchar(255),
#     Arrival_Airport VARCHAR(255),
#     Pilot_Name VARCHAR(255),
#     Flight_Status VARCHAR(20),
#     Airline_Code VARCHAR(90),
#     TravelID VARCHAR(20),
#     PRIMARY KEY (TravelID),
#     FOREIGN KEY (Airline_Code) REFERENCES airline_codes(airline_Code)
    
    

# )


# """
#         )

        
#         cursor.execute("""
#     CREATE TABLE IF NOT EXISTS airport_codes (AirportCode varchar(90),	AirportName varchar(90),	Location varchar(90),	
#     Country varchar(90),	PassengerTraffic float,	Size int,	Revenue int,	FlightCount int


# )"""
#         )
#         cursor.execute("""
#     CREATE TABLE IF NOT EXISTS airline_codes (airline_Code int,revenue int,number_of_flights int,
#     passenger_count int


# )"""
#         )
        
    #load_data_from_csv(conn,'C:/Users/User/Desktop/Rev_P[0]/Final/travel.csv', 'travel')
    #load_data_from_csv(conn, 'C:/Users/User/Desktop/Rev_P[0]/Final/airport_codes.csv', 'airport_codes')
    #load_data_from_csv(conn, 'C:/Users/User/Desktop/Rev_P[0]/Final/airline_codes.csv', 'airline_codes')

    #--------------------- Main function starts here ------------------------------   
    menu=MainMenu()
    
    menu.run()          
    
    

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL server: {e}")

finally:
    # Close the connection when done
    if 'connection' in locals() and conn.is_connected():
        conn.close()
        print("Connection closed")

  
