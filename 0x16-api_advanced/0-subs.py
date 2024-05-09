#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a subreddit.
    """
    import requests

    sub info = requests.get("https:/www.reddit.com/r/{}/about.json"
            .format(subreddit)
            headers={"User-agent": "My-User-Agent"},
            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
