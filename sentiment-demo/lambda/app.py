import os
import json
import boto3

#def handler(event, context):
#
 #   client = boto3.client('comprehend')
#   body = event["body"]
#   sentiment = client.detect_sentiment(LanguageCode = "en", Text = body)
#   return {
#           "statusCode": 200,
#           "headers": {
#               "Content-Type": "application/json"
#           },
#           "body": json.dumps({
#                "sentiment ": json.dumps(sentiment)
#            })
#    }
    
from botocore.exceptions import BotoCoreError, ClientError

def handler(event, context):
    try:
        client = boto3.client('comprehend')
        body = event["body"]
        sentiment = client.detect_sentiment(LanguageCode="en", Text=body)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "sentiment": sentiment
            })
        }
    except (BotoCoreError, ClientError) as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
