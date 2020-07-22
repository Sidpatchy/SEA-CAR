# A module of Sidpatchy's Extremely Awesome, Complex, and Advanced Reddit bot (SEA-CAR) designed to allow you to blacklist all recent posts so that your bot doesn't try to comment on any posts you don't want it to
# More info about the bot can be found on its GitHub: https://github.com/sidpatchy/SEA-CAR

import praw
import re
import os
import sLOUT as lout

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('')    # Replace with the subreddit you want to blacklist

if not os.path.isfile('repliedPosts.txt'):
    repliedPosts = []    
else:
    with open('repliedPosts.txt', 'r') as f:
       repliedPosts = f.read()
       repliedPosts = repliedPosts.split('\n')
       repliedPosts = list(filter(None, repliedPosts))

for submission in subreddit.hot(limit=100):    # Change the limit to an amount you deem best
    print('Blacklisting: {}, {}'.format(submission.title, submission.id))
    print()
    if submission.id not in repliedPosts:
        repliedPosts.append(submission.id)
        with open("repliedPosts.txt", "w") as f:
            for post_id in repliedPosts:
                f.write(post_id + "\n")