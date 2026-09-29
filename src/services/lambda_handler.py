from src.services.weather_service import process_weather_data

def lambda_handler(event, context):
    """AWS Lambda entry point for the weather data pipeline."""
    weather_data = event.get("weather_data", {})
    processed_data = process_weather_data(weather_data)
    return {
        "statusCode": 200,
        "data": processed_data
    }
