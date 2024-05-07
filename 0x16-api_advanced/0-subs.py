#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a subreddit.

    Args:
        subreddit: The name of the subreddit (e.g., "learnpython").

    Returns:
        The number of subscribers for the subreddit, or 0 if the subreddit
        is invalid.
    """

    # Use a custom User-agent to avoid throttling
    user_agent = "My Reddit scraper v1.0 (by /u/your_username)"
    headers = {"User_agent": user_agent}

    # Construct the API URL
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        # Send GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for successful response. likely invalid subreddit
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
        # Subreddit may be invalid
            print(f"Error: Subreddit '{subreddit}' may be invalid (status code: {response.status_code})")
            return 0
    except requests.exceptions.RequestException as e:
        # Handle general request errors
        print(f"Error fetching data from Reddit API: {e}")
        return 0

# Example usage 
subreddit_name = "learnpython"
num_subscribers = number_of_subscribers(subreddit_name)
print(f"Number of subscribers for r/{subreddit_name}: {num_subscribers}")
