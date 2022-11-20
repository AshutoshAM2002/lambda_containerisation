import json

def lambda_handler(event, context):
    msg = "Hello world from lambda!"

    response = {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"myMsg": msg})
    }

    return response
