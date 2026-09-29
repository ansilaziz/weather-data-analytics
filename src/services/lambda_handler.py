def lambda_handler(event, context): 
    """AWS Lambda entry point for the weather data pipeline.""" 
    return {"statusCode": 200, "message": "Lambda handler is ready"} 
