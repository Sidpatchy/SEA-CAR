# Sidpatchy's Extremely Awesome, Complex, and Advanced Reddit bot (SEA-CAR) is a very simple reddit bot by Sidpatchy
# More info about the bot can be found on its GitHub: https://github.com/sidpatchy/SEA-CAR

import praw
import re
import os
import datetime as DT
import yaml
import sLOUT as lout

# Create config.yml if it doesn't exist
if not os.path.isfile('repliedPosts.txt'):
    configValues = {'redditAccount', 'subreddit', 'botName', 'postTitle', 'postText', 'reply', 'postTitle2', 'postText2', 'reply2'}
    with open('config.yml', 'w') as f:
        configuration = yaml.dump(configValues, f)

# Read yaml file and assign its data to variables
with open('config.yml') as f:
    config = yaml.safe_load(f)
    
    # Bot configuration
    redditAccount = config['redditAccount']
    sub = config['subreddit']
    botName = str(config['botName'])

    # First message
    postTitle = config['postTitle']
    postText = config['postText']
    reply = config['reply']

    # Second message
    postTitle2 = config['postTitle2']
    postText2 = config['postText2']
    reply2 = config['reply2']

# Select a reddit account from praw.ini and select a subreddit
reddit = praw.Reddit(redditAccount)
subreddit = reddit.subreddit(sub)

# Write to the logs stating that the bot has been initialized
lout.writeFile('{}Logs.txt'.format(botName), 'Bot initialized', True)

# Check if repliedPosts.txt exists, if it doesn't, declare the variable repliedPosts as an empty list
if not os.path.isfile('repliedPosts.txt'):
    repliedPosts = []

# If the file exists, open it and then read the file to repliedPosts
else:
    with open('repliedPosts.txt', 'r') as f:
       repliedPosts = f.read()
       repliedPosts = repliedPosts.split('\n')              # split the string from repliedPosts.txt into individual lines
       repliedPosts = list(filter(None, repliedPosts))      # Convert each line into an item in a list, then store it in repliedPosts

for submission in subreddit.new(limit=5):
    startTime = DT.datetime.now()                           # Store the time an operation on a post was started

    # Check if the post already has a reply from the bot and if 'No.' (not case sensitive) is in the post and if 'Post Title 1' (not case sensitive) is in the title
    if submission.id not in repliedPosts and re.search(postText, submission.selftext, re.IGNORECASE) and re.search(postTitle, submission.title, re.IGNORECASE):
        submission.reply(reply)                                                # Reply to the post with the contents of the variable 'reply'
        print('Replying to: {}, {}'.format(submission.title, submission.id))   # Print which post is being replied to
        repliedPosts.append(submission.id)                                     # Add the post to the list of posts that have been replied to

        # Open or create the file repliedPosts.txt
        with open("repliedPosts.txt", "w") as f:
            for post_id in repliedPosts:                                              # run shit for each each id (called post_id) in the list repliedPosts
                f.write(post_id + "\n")                                               # Write the ID on a new line
        
        lout.log(startTime, 'Replied \'{}\''.format(reply), botName)                  # Write to the log using sLOUT

    # Check if the post already has a reply from the bot and if 'No.' (not case sensitive) is in the post and if 'Post Title 2' (not case sensitive) is in the title            
    elif submission.id not in repliedPosts and re.search(postText2, submission.selftext, re.IGNORECASE) and re.search(postTitle2, submission.title, re.IGNORECASE):
        submission.reply(reply2)                                                 # Reply to the post with the contents of the variable 'reply'
        print('Replying to: {}, {}'.format(submission.title, submission.id))     # Print which post is being replied to
        repliedPosts.append(submission.id)

        # Open or create the file repliedPosts.txt
        with open("repliedPosts.txt", "w") as f:
            for post_id in repliedPosts:                                              # run shit for each each id (called post_id) in the list repliedPosts
                f.write(post_id + "\n")                                               # Write the ID on a new line
        
        lout.log(startTime, 'Replied \'{}\''.format(reply2), botName)                 # Write to the log using sLOUT