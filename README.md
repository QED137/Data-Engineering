# Data-Engineering
Basics of Data Engineering.  Fetching data from several apis, writing to the database and retrieving from database

# How to run this porject in your own sytem

# **Weather and Flight Data Project**

This project fetches **weather data** and **flight information**, stores them in a **MySQL database**, and provides functionality for retrieving and analyzing the data. The application integrates two APIs: **OpenWeather API** for weather data and **AeroDataBox API** for flight information.

## **Table of Contents**

- [Data-Engineering](#data-engineering)
- [How to run this porject in your own sytem](#how-to-run-this-porject-in-your-own-sytem)
- [**Weather and Flight Data Project**](#weather-and-flight-data-project)
  - [**Table of Contents**](#table-of-contents)
  - [**Project Overview**](#project-overview)
  - [**Features**](#features)
  - [**Technologies Used**](#technologies-used)
  - [**Setup Instructions**](#setup-instructions)
    - [**1. Prerequisites**](#1-prerequisites)
    - [**2. Clone the Repository**](#2-clone-the-repository)

---

## **Project Overview**

This project automates the collection of weather and flight data for a list of cities, stores the data in a MySQL database, and provides capabilities to retrieve and analyze this information. The project leverages two APIs to gather real-time information:

1. **OpenWeather API**: Fetches weather forecasts, including temperature, humidity, wind speed, and outlook.
2. **AeroDataBox API**: Retrieves flight arrival data, including flight numbers, scheduled arrival times, and departure airport details.

The application interacts with these APIs, processes the data, and stores it in a MySQL database for easy querying and analysis.

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
