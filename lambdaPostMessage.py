import json
from botocore.vendored import requests


def lambda_handler(event, context):
    
    myToken="<Your-OAuth-Token>"
    url="https://slack.com/api/chat.postMessage"
    
    myMessage= {
        'channel' : '<Your-Slack-Channel-Name>',
        'text' : 'Pipeline ' + event['detail']['pipeline'] + ' has change in the  ' + event['detail']['state']
    }
    
    headers = {'Content-type': 'application/json', 'Authorization' : 'Bearer ' + myToken}

    rsp = requests.post(url, json=myMessage, headers=headers)
    print (rsp.text)
