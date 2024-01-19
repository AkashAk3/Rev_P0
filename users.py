import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from connection import *
from tabulate import tabulate
con=Connection()
class user_class:
    conn=con.connec()
    cursor=conn.cursor(dictionary=True)
    
    def view_travellers(self):
        query="select * from travel limit  10"
        
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        data_tuples=[(row['Passenger_ID'],row['First_Name'],row['Last_Name'],row['Gender'],row['Age'],row['Nationality'],row['Airport_Name'],row['Airport_Country_Code'],row['Country_Name'],row['Airport_Continent'],row['Continents'],row['Departure_Date'],row['Arrival_Airport'],row['Pilot_Name'],row['Flight_Status'],row['Airline_Code'],row['TravelID'])for row in result]
        headers=result[0].keys()
        print(tabulate(data_tuples,headers=headers,tablefmt="pretty"))


    def view_airports(self):
        query="select * from airport_codes limit  10"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        data_tuples=[(row['AirportName'],row['Location'],row['Country'],row['PassengerTraffic'],row['Size'],row['Revenue'],row['FlightCount'])for row in result]
        headers=result[0].keys()
        print(tabulate(data_tuples,headers=headers,tablefmt="pretty"))
        
    def view_airlines(self):
        query="select * from airline_codes limit  10"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        data_tuples=[(row['airline_Code'],row['revenue'],row['number_of_flights'],row['passenger_count'])for row in result]
        headers=result[0].keys()
        print(tabulate(data_tuples,headers=headers,tablefmt="pretty"))
        
    def view_users(self):
        query="select ID,username,role from signups"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        data_tuples=[(row['ID'],row['username'],row['role'])for row in result]
        headers=result[0].keys()
        print(tabulate(data_tuples,headers=headers,tablefmt="pretty"))
        
    def analyze_travel(self):
        query1=""""create view analyse as select t.passenger_id,t.first_name,t.country_name,t.airline_code,a.revenue,
        a.number_of_flights from travel as t inner join airline_codes as a on t.Airline_Code =a.airline_Code"""
        query2="""select country_name,count(number_of_flights) as Total_Flights from analyse group by country_name"""
        self.cursor.execute(query2)
        result = self.cursor.fetchall()
        
        Airline_data = result
        df_Airline = pd.DataFrame(Airline_data)

        if df_Airline.empty:
            print(f"No data found for country code")
        else:
            col_data = ['country_name', 'Total_Flights']
            
        plt.figure(figsize=(14, 8))
        sns.barplot(x='country_name', y='Total_Flights', data=df_Airline, palette='viridis')
        plt.title('Total Flights by Country')
        plt.xlabel('Country')
        plt.ylabel('Total Flights')
        plt.show()
    
    

        # Melt the DataFrame to combine columns into a single variable
        #df_melted = pd.melt(df_Airline, id_vars=['year'], value_vars=col_data, var_name='Consumer Price Type', value_name='Consumer Price')

        # plt.figure(figsize=(12, 6))
        # sns.barplot(x="year", y="Consumer Price", hue="Consumer Price Type", data=df_melted, palette="viridis")
        # plt.xlabel("Year")
        # plt.ylabel("Consumer Price")
        # plt.title(f"Bar Graph for Consumer Prices in {country_code}")
        # plt.legend(title="Consumer Price Type", bbox_to_anchor=(1, 1))
        # plt.show()
        
        
    
    
    def user(self):
        while True:
            print("\nChoose the option:")
            print("1.View Travellers")
            print("2.Airports")
            print("3.Airlines")
            print("4.users")
            print("5.Analyse the traveller detail")
            print("6.Exit")
            choice=input("\nEnter the choice:")
            if choice == "1":
                self.view_travellers()
                
            elif choice == "2":
                self.view_airports()
            elif choice == "3":
                self.view_airlines()
            elif choice == "4":
                self.view_users()
            elif choice == "5":
                self.analyze_travel()
            elif choice == "6":
                break
        
        
                
        
            
