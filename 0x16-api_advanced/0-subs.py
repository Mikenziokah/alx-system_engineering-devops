#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ Finds number of subscribers of an specific users """
    try:
        req = requests.get(
            'https://www.reddit.com/r/' + sys.argv[1] + '/about.json',
            allow_redirects=False,
            headers={'User-agent': 'Baquero28'})

        dict_reddit = json.loads(req.text)
        data_key = dict_reddit['data']

        return (data_key['subscribers'])
    except:
        return (0)
