#!/usr/bin/python3
"""This module queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    list all hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    usr_agt = {"User-Agent": "Holberton"}
    params = {"limit": "100", "after": after}
    r = requests.get(url, headers=usr_agt, params=params)
    if r.status_code != 200:
        print("None")
    else:
        json_request = r.json()
        json_data = json_request.get("data")
        json_children = json_data.get("children")
        json_after = json_data.get("after")
        if json_after is not None:
            recurse(subreddit, hot_list, json_after)
        for post in json_children:
            post_data = post.get("data")
            post_title = post_data.get("title")
            hot_list.append(post_title)
        return (hot_list)
