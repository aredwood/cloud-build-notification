import base64
import requests
import json
import os
from datetime import datetime


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

    print(updatePayload)

    fallback = "%s%s -> %s:%s" % (
        status,
        emojis.get(status), 
        updatePayload['source']['repoSource']['branchName'], 
        updatePayload['source']['repoSource']['repoName']
    )

    colors = {
        "QUEUED": "#1da7f2",
        "WORKING": "#f2e01d",
        "SUCCESS": "#20c74d",
        "FAILURE": "#d11919"
    }

    title_link = "https://console.cloud.google.com/cloud-build/builds/%s?project=%s" % (updatePayload['id'],updatePayload['projectId'])

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    # create a json payload
    payload = json.dumps({
        "attachments": [
            {
                "fallback": fallback,
                "color": colors.get(status),
                "title": "Google Cloud Build Notification",
                "title_link": title_link,
                "text": "%s -> %s" % (updatePayload['source']['repoSource']['branchName'],updatePayload['source']['repoSource']['repoName']),
                "fields": [
                    {
                        "title": "Status",
                        "value": "%s %s" % (status,emojis.get(status)),
                        "short": True
                    }
                ],

                "ts": timestamp
            }
        ]
    })

    # send the request, capture the response
    res = requests.post(url=url, data=payload, headers={
        "Content-Type": "application/json"
    })

    # do something with response
