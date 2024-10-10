Add a 'config.ini' file to your project directory. the config.ini file contains the following code 

[Database]
user = your_mysql_username
password = your_mysql_password
host = localhost
database = weatherDB
port = 3306

[API]
weather_api_key = your_openweather_api_key
flight_api_key = your_flight_api_key

[Email]
sender_email = your_email@gmail.com
email_password = your_email_password
smtp_server = smtp.gmail.com
smtp_port = 587
