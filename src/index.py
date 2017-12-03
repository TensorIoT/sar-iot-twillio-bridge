from time import sleep
import boto3, json, os, uuid, logging, random, string

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = os.environ['AccountSid']
# Your Auth Token from twilio.com/console
auth_token  = os.environ['AuthToken']
client = Client(account_sid, auth_token)

def lambda_handler(event, context):
    print(event)
    if 'deviceID' not in event:
        print("Missing DeviceID")
        return "Error"

    if 'incomingText' not in event:
        print("Missing IncomingText")
        return "Error"

    if 'toNumber' not in event:
        print("Missing To Number")
        return "Error"

    print(event['deviceID'])
    print(event['incomingText'])
    print(event['toNumber'])

    try:
        message = client.messages.create(
            to=event['toNumber'],
            from_=os.environ['FromNumber'],
            body=event['deviceID'] + ": " + event['incomingText'])
        print(message)

        return "Success"

    except Exception as e:
        print(e)
        return "Error"