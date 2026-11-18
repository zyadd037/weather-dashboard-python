# Weather Dashboard

A Python command-line application that retrieves real-time weather information using WeatherAPI.

## Features
- Search for weather by city name.
- Display temperature, humidity, wind speed, and weather conditions.
- Handle invalid city names and API errors.
- Handle connection errors and request timeouts.
- Load API keys securely using environment variables.
- Automated testing using pytest and mocking.

## Technologies
- Python
- Requests
- REST API
- JSON
- Python-dotenv
- Pytest

## Project Structure

```text
Weather_Dashboard/
├── main.py
├── weather.py
├── requirements.txt
├── .gitignore
├── README.md
└── testing/
    └── test_weather.py
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```env
API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own WeatherAPI key.

## Run the Application

```bash
python main.py
```

## Run Tests

```bash
python -m pytest testing -v
```

## Author

Zeyad Ahmed Mohamed