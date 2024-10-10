# main.py
from data.cities import cities_data
from db.push_to_database import push_to_database
from db.retrieve_from_db import retrieve_from_db
from db.database import load_config, connect_database
from data.weather import get_weather_data
from data.flight import icao_airport_codes, get_flight_data
import logging
import argparse
import smtplib
from email.mime.text import MIMEText
import os


# def main():
#     # 1. Load the config from the database.py module
#     config = load_config()

#     # 2. Set up the database connection using the config
#     engine = connect_database(config)
#     API_key = config['API']['api_key']

#     if engine:
#         # 3. Define the list of cities to fetch data for
#         #city_list = ['Berlin', 'Hamburg', 'Munich']

#         # 4. Fetch city data from Wikipedia using cities_data
#         #city_df = cities_data(city_list)
#         #print(f"City data: \n{city_df}")

#         # # 5. Push city data into the database
#         # #push_to_database(city_df, 'cities', engine)

#         # # 6. Retrieve city data from the database
#         # cities_from_db = retrieve_from_db('cities', engine)
#         # print(f"Cities from DB: \n{cities_from_db}")

#         # # 7. Fetch weather data using the retrieved city data from the DB
#         # api_key = config['API']['api_key']
#         # weather_df = get_weather_data(API_key,cities_from_db)
#         # print(f"Weather data: \n{weather_df}")
#         #air_df =icao_airport_codes()
#         #print(air_df)
        
#         #push_to_database(air_df, 'airports', engine)
#         #air_from_DB=retrieve_from_db('airports', engine)
#         #print(air_from_DB)
#         icao_list = ["EDDB", "EDDH"] #  one can also fetch the data for icao code form dataabse
#         flights_to_db = get_flight_data(icao_list)
        
#         #wrtie flight information to the databse 
#         push_to_database(flights_to_db, 'flights', engine)
        
#     else:
#         print("Could not connect to the database.")

# if __name__ == "__main__":
#     main()
# Set up logging
logging.basicConfig(filename='project_log.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_desktop_notification(title, message):
    """Send desktop notification (for Linux-based systems)."""
    try:
        os.system(f'notify-send "{title}" "{message}"')
        logging.info(f"Desktop notification sent: {title} - {message}")
    except Exception as e:
        logging.error(f"Failed to send desktop notification: {e}")

def send_email(subject, body, to_email):
    """Send an email notification."""
    config = load_config()  # Load config to retrieve email credentials
    sender_email = config['Email']['sender_email']
    email_password = config['Email']['email_password']
    smtp_server = config['Email']['smtp_server']
    smtp_port = config['Email']['smtp_port']

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, to_email, msg.as_string())
            logging.info(f"Email sent to {to_email}: {subject}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def fetch_and_store_weather(engine, API_key):
    """Fetches weather data and stores it in the database."""
    # Retrieve city data from the database
    cities_from_db = retrieve_from_db('cities', engine)
    if cities_from_db.empty:
        logging.error("No cities found in the database.")
        return
    logging.info(f"Retrieved city data: \n{cities_from_db}")

    # Fetch weather data using the retrieved city data from the DB
    weather_df = get_weather_data(API_key, cities_from_db)
    logging.info(f"Weather data fetched: \n{weather_df}")

    # Push weather data into the database
    push_to_database(weather_df, 'weather', engine)
    logging.info("Weather data pushed to the database.")

def fetch_and_store_flights(engine, icao_list):
    """Fetches flight data and stores it in the database."""
    flights_to_db = get_flight_data(icao_list)
    logging.info(f"Flight data fetched: \n{flights_to_db}")

    # Push flight information to the database
    push_to_database(flights_to_db, 'flights', engine)
    logging.info("Flight data pushed to the database.")

def main(fetch_weather=False, fetch_flights=False):
    # 1. Load the config
    config = load_config()

    # 2. Set up the database connection using the config
    engine = connect_database(config)
    if not engine:
        logging.error("Could not connect to the database.")
        return

    API_key = config['API']['api_key']

    # 3. Perform actions based on the command line arguments
    if fetch_weather:
        fetch_and_store_weather(engine, API_key)
        send_desktop_notification('Weather Data Update', 'Weather data has been successfully pushed to the database.')
        send_email(
            subject='Weather Data Update',
            body='Weather data has been successfully pushed to the database.',
            to_email='recipient@example.com'  # Change to the recipient's email
        )

    if fetch_flights:
        icao_list = ["EDDB", "EDDH"]  # Example ICAO codes; could also be fetched from DB
        fetch_and_store_flights(engine, icao_list)
        send_desktop_notification('Flight Data Update', 'Flight data has been successfully pushed to the database.')
        send_email(
            subject='Flight Data Update',
            body='Flight data has been successfully pushed to the database.',
            to_email='recipient@example.com'  # Change to the recipient's email
        )

if __name__ == "__main__":
    # 4. Set up command-line arguments
    parser = argparse.ArgumentParser(description='Data Pipeline for Weather and Flight Data')
    parser.add_argument('--weather', action='store_true', help='Fetch and store weather data')
    parser.add_argument('--flights', action='store_true', help='Fetch and store flight data')
    
    args = parser.parse_args()
    
    main(fetch_weather=args.weather, fetch_flights=args.flights)