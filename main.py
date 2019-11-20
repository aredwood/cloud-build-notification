import base64
import requests
import json
import os


def notification(event, context):

    # contains the message object
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')

    # send a slack notification
    sendSlackNotification(pubsub_message)

    # other things here


def sendSlackNotification(buildUpdateJson):

    # parse the json
    updatePayload = json.loads(buildUpdateJson)

    # extract what we need
    status = updatePayload['status']
    buildId = updatePayload['id']

    # post url
    url = os.environ.get("SLACK_LINK")

    emojis = {
        "QUEUED": "📨",
        "WORKING": "🔨",
        "SUCCESS": "✔️",
        "FAILURE": "😭"
    }

    # form the message, here it is a single line
    line = "%s - %s" % (buildId, emojis.get(status))

    print(updatePayload)

    # create a json payload
    payload = json.dumps({
        "attachments": [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#36a64f",
                "title": "Slack API Documentation",
                "title_link": "https://api.slack.com/",
                "text": "Optional text that appears within the attachment",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": False
                    }
                ],
                "footer": "Slack API",

                "ts": 123456789
            }
        ]
    })

    # send the request, capture the response
    res = requests.post(url=url, data=payload, headers={
        "Content-Type": "application/json"
    })

    # do something with response
