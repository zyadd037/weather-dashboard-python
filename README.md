# weather-dashboard-python
A Python CLI weather dashboard using WeatherAPI.

# Weather Dashboard 

A simple Python command-line application that retrieves real-time weather information for any city using the WeatherAPI service.

## Features

- Get current weather information by entering a city name.
- Display temperature in Celsius.
- Display humidity percentage.
- Display wind speed in km/h.
- Display current weather conditions.
- Handle invalid city names and API errors.
- Handle connection errors and request timeouts.
- Use environment variables to protect the API key.
- Test application behavior using pytest and mocking.

## Technologies Used

- Python
- Requests
- WeatherAPI
- python-dotenv
- pytest
- unittest.mock

## Project Structure

```text
Weather_Dashboard/
├── main.py
├── weather.py
├── .env
├── .gitignore
├── requirements.txt
└── testing/
    └── test_weather.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/weather-dashboard-python.git
```

2. Navigate to the project folder:

```bash
cd weather-dashboard-python
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your WeatherAPI key:

```env
API_KEY=your_api_key_here
```

5. Run the application:

```bash
python main.py
```

## Running Tests

Run the following command:

```bash
python -m pytest testing -v
```

The tests cover successful API requests, invalid city responses, and request timeouts.

## What I Learned

Through this project, I practiced working with REST APIs, JSON responses, environment variables, exception handling, and automated testing with mocking.

## Author

Zeyad Ahmed Mohamed
