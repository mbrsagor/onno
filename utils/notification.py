import requests
from django.conf import settings

url = "https://onesignal.com/api/v1/notifications/"
authorization = "NDVjOTQxNTQtOTYyOS00NTlkLTk0NGMtZGY5MGViZjNmZTEx"
APP_ID = "5d85cda9-28c8-4655-ad11-69f5414dfe8a"
app_name = "HerculesDev"

headers = {
    "accept": "text/plain",
    "Content-Type": "application/json",
    "Authorization": f"Basic {authorization}"
}


# The notification will throw all users
def send_notification_to_all(title, message, icon=None, picture=None):
    body = {
        "app_id": APP_ID,
        "app_name": app_name,
        "included_segments": ['Subscribed Users'],
        "large_icon": icon,
        "big_picture": picture,
        "headings": {"en": title},
        "contents": {"en": message},
    }

    response = requests.post(url, json=body, headers=headers)
    return response


# The notification will throw for single user
def send_notification_single_user(device_token, title, message, icon=None, picture=None):
    body = {
        "app_id": APP_ID,
        "app_name": app_name,
        "include_player_ids": [device_token],
        "large_icon": icon,
        "big_picture": picture,
        "headings": {"en": title},
        "contents": {"en": message},
    }

    response = requests.post(url, json=body, headers=headers)
    return response
