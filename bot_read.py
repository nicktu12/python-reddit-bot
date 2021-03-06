#!/usr/local/lib/python3.6
import praw

reddit = praw.Reddit('bot2')
subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
