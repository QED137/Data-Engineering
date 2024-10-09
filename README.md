# **Data-Engineering: Weather and Flight Data Project**

This project is part of the training at **WBS Coding School**. The goal of this project is to develop a data engineering pipeline that fetches **weather data** and **flight information** using external APIs, stores the data in a **MySQL database**, and provides functionality for **retrieving** and **analyzing** the data.
This project fetches **weather data** and **flight information**, stores them in a **MySQL database**, and provides functionality for retrieving and analyzing the data. The application integrates two APIs: **OpenWeather API** for weather data and **AeroDataBox API** for flight information.

The project integrates two main APIs:
- **OpenWeather API**: Retrieves weather forecast data, including temperature, humidity, wind speed, and overall outlook for specific cities.
- **AeroDataBox API**: Fetches flight arrival data, including flight numbers, scheduled arrival times, and departure airport detail

## **Features**

- Fetches weather data for a specified list of cities.
- Retrieves flight arrival information from airports.
- Stores the data in a MySQL database.
- Provides retrieval functions for weather and flight data.
- Configuration management for API keys and database credentials.
- Customizable city and airport lists.

## **Technologies Used**

- **Python**: Core programming language used.
  - Libraries: `requests`, `pandas`, `SQLAlchemy`, `pytz`, `BeautifulSoup`
- **APIs**: OpenWeather API and AeroDataBox API.
- **MySQL**: For storing weather and flight data.
- **ConfigParser**: For handling configuration files.

## **Setup Instructions**

### **1. Prerequisites**

Before you begin, ensure you have the following software installed on your local machine:

- **Python 3.9+**
- **MySQL Server** or **MySQL Workbench**
- **Pip**: Python package manager
- **Git**: To clone the repository

### **2. Clone the Repository**

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your_username/your_repository_name.git
cd your_repository_name

```
### **3. Setup a database in your mysqlworkbench**

- create database and uplaod  weatherDB.sql file to your mysqlworkbench
### **Get your API key**
- **OpenWeather API**: Create your API key for weather data [here](https://openweathermap.org/api).
- **AeroDataBox API**: Create your API key for flight data [here](https://aerodatabox.p.rapidapi.com).

### **4. Create `config.ini`**

The instructions for creating the `config.ini` file are provided in the `config` folder's `README.md` file. This file is essential because it contains the necessary information for your local database and API keys.

Your `config.ini` file should look like this:

```ini
[Database]
user = your_mysql_username
password = your_mysql_password
host = localhost
database = weatherDB
port = 3306

[API]
weather_api_key = your_openweather_api_key
flight_api_key = your_flight_api_key
```
### **Run the following command**
```bash
python3 main.py
``