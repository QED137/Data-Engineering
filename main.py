# main.py
from data.cities import cities_data
from db.push_to_database import push_to_database
from db.retrieve_from_db import retrieve_from_db
from db.database import load_config, connect_database
from data.weather import get_weather_data
from data.flight import icao_airport_codes, get_flight_data



def main():
    # 1. Load the config from the database.py module
    config = load_config()

    # 2. Set up the database connection using the config
    engine = connect_database(config)
    API_key = config['API']['api_key']

    if engine:
        # 3. Define the list of cities to fetch data for
        #city_list = ['Berlin', 'Hamburg', 'Munich']

        # 4. Fetch city data from Wikipedia using cities_data
        #city_df = cities_data(city_list)
        #print(f"City data: \n{city_df}")

        # # 5. Push city data into the database
        # #push_to_database(city_df, 'cities', engine)

        # # 6. Retrieve city data from the database
        # cities_from_db = retrieve_from_db('cities', engine)
        # print(f"Cities from DB: \n{cities_from_db}")

        # # 7. Fetch weather data using the retrieved city data from the DB
        # api_key = config['API']['api_key']
        # weather_df = get_weather_data(API_key,cities_from_db)
        # print(f"Weather data: \n{weather_df}")
        #air_df =icao_airport_codes()
        #print(air_df)
        
        #push_to_database(air_df, 'airports', engine)
        #air_from_DB=retrieve_from_db('airports', engine)
        #print(air_from_DB)
        icao_list = ["EDDB", "EDDH"] #  one can also fetch the data for icao code form dataabse
        flights_to_db = get_flight_data(icao_list)
        
        #wrtie flight information to the databse 
        push_to_database(flights_to_db, 'flights', engine)
        
    else:
        print("Could not connect to the database.")

if __name__ == "__main__":
    main()
