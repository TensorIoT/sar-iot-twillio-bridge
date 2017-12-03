# AWS IOT - Twilio Bridge

Let your devices to send Twillio messages for you. This service provides a bridge between AWS IOT and Twilio. Now using this service, the text messages sent by devices via aws iot can be forwarded to a phone number that is registered via twillio.

## Input Format from the IOT Topic
	
~~~~
{
    "deviceID": "deviceID123",
    "incomingText": "Text From Device"
    "toNumber": "+1xxxxxxxxxx"
}
	
~~~~

## Needed configuration

The following items needs to be configured in the template

~~~~
1.) AccountSid - Account SID for Twilio account.
2.) AuthToken - AuthToken for Twilio account.
3.) IncomingTopic - The topic that will be used as the trigger for the lambda.
4.) FromNumber - The phone number the message is coming from.





