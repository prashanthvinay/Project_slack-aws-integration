import json
import boto3
from botocore.vendored import requests

def process_message(userFrom, msg, channel):
  
  print("Got message " + msg)
  print("From User:" + userFrom)
  
  if "run pipeline" in msg:
    print('posting event to run pipeline...')
    post_to_eventbridge()
  

def post_to_eventbridge():
  #Create EventBridge Client
  client = boto3.client('events')

  #put the event in queue
  response = client.put_events(
      Entries=[
          {
              'Source': 'slack.devops',
              'Resources': [],
              'DetailType': 'Execute our pipeline',
              'Detail': '{}',
              'EventBusName': 'default'
          },
      ]
  )


def lambda_handler(event, context):

  params = json.loads(event['body'])
  
  print("Got request type: " + params['type'])
  print('Full request:')
  print( event)
  
  request_type = params['type']
  
  if request_type == 'url_verification':
    return {'challenge' : params['challenge'] }
  
  if request_type == 'event_callback':
    print ("processing message...")
    process_message(params['event']['user'], params['event']['text'], params['event']['channel'])
