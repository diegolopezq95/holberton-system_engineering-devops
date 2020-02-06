#!/usr/bin/python3
"""This module queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """
    top ten hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    usr_agt = {"User-Agent": "Holberton"}
    params = {"limit": "10"}
    r = requests.get(url, headers=usr_agt, params=params,
                     allow_redirects=False)
    if r.status_code != 200:
        print("None")
    else:
        json_request = r.json()
        json_data = json_request.get("data")
        json_children = json_data.get("children")
        for post in json_children:
            post_data = post.get("data")
            post_title = post_data.get("title")
            print(post_title)
