from connection import *
from tabulate import tabulate
con=Connection()
class admin_class:
    conn=con.connec()
    cursor=conn.cursor(dictionary=True)
    
    def view_travellers(self):
        query="select * from travel limit  10"
        
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if not result:
            print("Oops No data here")
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
        query="select * from signups"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        data_tuples=[(row['ID'],row['username'],row['password'],row['role'])for row in result]
        headers=result[0].keys()
        print(tabulate(data_tuples,headers=headers,tablefmt="pretty"))
        
        
    def create_records(self,airline_code,revenue,number_of_flights,passenger_count):
        query="insert into airline_codes(airline_code,revenue,number_of_flights,passenger_count) values(%s,%s,%s,%s)"
        data=(airline_code,revenue,number_of_flights,passenger_count)
        self.cursor.execute(query,data)
        self.conn.commit()
        print("\nSuccessfully created a new data\n")
    def update_records(self,id,pwd):
        query="update signups set password=%s where ID=%s"
        data=(pwd,id)
        self.cursor.execute(query,data)
        print("\nPassword Updated")
    def delete_records(self,id):
        query="delete from signups where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        print("ID no.",id,"has been succesfully deleted\n")
    
    def admin(self):
        while True:
            print("\nChoose the option:")
            print("---------------------")
            print("1.View Travellers")
            print("2.Airports")
            print("3.Airlines")
            print("4.Users details")
            print("5.Create airline data")
            print("6.Update users password")
            print("7.Delete users")
            print("8.Exit")
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
                airline_code=input("\nEnter the airliine code:")
                revenue=int(input("Enter the revenue"))
                number_of_flights=int(input("enter the number of flights"))
                passenger_count=int(input("Enter the passenger_count"))
                self.create_records(airline_code,revenue,number_of_flights,passenger_count)
            elif choice == "6":
                id=int(input("\nEnter the ID to be change:"))
                pwd=input("Enter the new password:\t")
                
                self.update_records(id,pwd)
            elif choice == "7":
                id=int(input("\nEnter the ID to be delete:"))
                self.delete_records(id)
            
            elif choice == "8":
                break
   
        
        
                
        
            
