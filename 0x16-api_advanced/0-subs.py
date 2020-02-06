#!/usr/bin/python3
"""This module returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""


import requests


def number_of_subscribers(subreddit):
    """
    number of reddit subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    usr_agt = {"User-Agent": "Holberton"}
    r = requests.get(url, headers=usr_agt, allow_redirects=False)
    if r.status_code != 200:
        return 0
    json_request = r.json()
    json_data = json_request.get("data")
    json_subs = json_data.get("subscribers")
    return (json_subs)
