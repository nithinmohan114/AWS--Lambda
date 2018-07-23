import json
import requests


def hello(event, context):
    body = event.get('body')
    data = json.loads(body)
    title = data.get('object_attributes').get('title')
    url = data.get('object_attributes').get('url')
    user = data.get('user').get('name')
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    webhookurl = "https://hooks.slack.com/services/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"
    data = {
        "attachments": [
            {
                "fallback": "fallback",
                "color": "#36a64f",
                # "pretext": "Optional",
                "author_name": "Nithin",
                # "author_link": "http://flickr.com/bobby/",
                # "author_icon": "http://flickr.com/icons/bobby.jpg",
                "title": "{}, You have an issue in gitlab.com".format(user),
                "title_link": url,
                "text": title,
                # "image_url": image_url,
                # "thumb_url": "http://example.com/path/to/thumb.png",
                "footer": "Entri",
                # "footer_icon": "png",
            }
        ]
    }

    requests.post(webhookurl, json=data,
                  headers={'Content-Type': 'application/json'})
    requests.post("http://f3f7d7cf.ngrok.io", json=data,
                  headers={'Content-Type': 'application/json'})
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
