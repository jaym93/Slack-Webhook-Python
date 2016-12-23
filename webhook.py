import http.client, json
import getopt, sys, os
import subprocess
import gzip
import re

colors = {'danger': '#ef4438', 'success': '#49b050', 'warning': '#fec110', 'info': '#4690cd'}
messages = [
    {
        'title': 'Sample danger message',
        'text': 'This is a message that requires high priority',
        'pretext': 'This is a message that requires high priority',
        'color': colors['danger'],
        'title': 'Sample Event 1',
        'desc': 'This is the description of first sample event'
    },
    {
        'title': 'Sample warning message',
        'text': 'This is a message that requires medium priority',
        'pretext': 'This is a message that requires medium priority',
        'color': colors['warning'],
        'title': 'Sample Event 2',
        'desc': 'This is the description of second sample event'
    },
    {
        'title': 'Sample success message',
        'text': 'This is a message that requires low priority',
        'pretext': 'This is a message that requires low priority',
        'color': colors['success'],
        'title': 'Sample Event 3',
        'desc': 'This is the description of third sample event'
    },
    {
        'title': 'Sample info message',
        'text': 'This is a message that requires no action',
        'pretext': 'This is a message that requires no action',
        'color': colors['info'],
        'title': 'Sample Event 4',
        'desc': 'This is the description of fourth sample event'
    }
]


def main():
    WEBHOOK_URL = "https://hooks.slack.com/services/#########/########/#######################" #Paste your webhook URL here
    headers = {'Content-Type': 'application/json'}
    connection = http.client.HTTPSConnection('hooks.slack.com')
    for message in messages:
        payload = {
            'username': 'Squak Event Logger',
            'fallback': message['text'],
            'pretext': message['text'],
            'color': message['color'],
            'channel': '#channel_name',         #Add Channel Name here
            'fields': [
                {
                    'title': message['title'],
                    'value': message['desc'],
                    'short': False
                }
            ]
        }
        connection.request('POST', WEBHOOK_URL, json.dumps(payload), headers)
        #print(json.dumps(payload))
        response = connection.getresponse()
        #print(response.read().decode())


if __name__ == '__main__':
    main()
