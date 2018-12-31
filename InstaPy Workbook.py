#!/usr/bin/env python
# coding: utf-8

# In[41]:


from instapy import InstaPy
from instapy.util import smart_run
import pandas as pd
import smtplib
import datetime
from datetime import datetime as dt
import time
from email.message import EmailMessage
from email.headerregistry import Address
from email.message import EmailMessage
import os


# Program Started Email

gmail_user = "matthew.stagner@gmail.com"
gmail_pwd = "TexasTech2018$$**"
TO = 'matthew.stagner@gmail.com'
SUBJECT = 'Program Started'
TEXT = 'Program Started'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(gmail_user, [TO], BODY)



# login credentials
insta_username = 'mcstagner'
insta_password = 'DuckHunting2019$$**'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True, 
                  disable_image_load=True)


with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                      delimit_by_numbers=True,
                                       max_followers=7000,
                                        min_followers=500,
                                        min_following=1000)
    
    
    session.set_dont_like(['marykay', 'vintagefashion'])

    # do the actual liking 
    session.like_by_tags(['waterfowlphotography', 'duckhunting', 'sitkagear', 'drakewaterfowl', 'wildlifephotographer', 'wildlifephotography'], amount=50)

    
    # Like posts in my feed

    # session.like_by_feed(amount=50, randomize=True, unfollow=False, interact=False)


    # Get my followers 
    
    stagner_followers=session.grab_followers(username='mcstagner', amount='full', live_match=True, store_locally=True)
    
    # Get my following

    stagner_following = session.grab_following(username="mcstagner", amount="full", live_match=True, store_locally=True)
    
    # Unfollowers

    all_unfollowers, active_unfollowers = session.pick_unfollowers(username="mcstagner", compare_by="day", compare_track="first", live_match=False, store_locally=True, print_out=True)


# # Create the initial pandas CSV file


# d={'Date': ['12-29-2018'], 'Followers': [6483], 'Following': [561]}
# Insta=pd.DataFrame(data=d)

# Insta['Date']=pd.to_datetime(Insta['Date'], format='%m-%d-%Y')

# Insta.set_index('Date')

# Insta.to_csv(r'C:\Users\matth\Dropbox\InstaPy\Insta.csv', index=False)


# Open the CSV file


Insta=pd.read_csv(r'C:\Users\matth\Dropbox\InstaPy\Insta.csv')


# Get my follower count


followers=len(stagner_followers)
following=len(stagner_following)


# Add the new followers to the dataframe


Insta.loc[datetime.datetime.now().strftime('%m-%d-%Y')]=[datetime.datetime.now().strftime('%m-%d-%Y'),followers, following]


# Save the dataframe


Insta.to_csv(r'C:\Users\matth\Dropbox\InstaPy\Insta.csv', index=False)


# Send an email


t='{0:%m-%d-%Y}'.format(datetime.datetime.now())
followers=len(stagner_followers)
following=len(stagner_following)
line1='Followers: ' + str(followers) 
line2='Following: ' + str(following)

gmail_user = "matthew.stagner@gmail.com"
gmail_pwd = "TexasTech2018$$**"
TO = 'matthew.stagner@gmail.com'
SUBJECT = 'InstaPy Summary: '+  t 
TEXT = 'Un-Followers: {}'.format(str(active_unfollowers))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_pwd)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % gmail_user,
        'Subject: %s' % SUBJECT,
        '', TEXT])

server.sendmail(gmail_user, [TO], BODY)
print ('email sent')


# In[ ]:


# insta_username = 'mcstagner'
# insta_password = 'DuckHunting2019$$**'

# # Login
# session = InstaPy(username=insta_username, password=insta_password)
# session.login()


# # # Find non followers
# # mcstagner_nonfollowers = session.pick_nonfollowers(username="mcstagner", live_match=True, store_locally=True)


# # set up all the settings
# session.set_relationship_bounds(enabled=False,
#                  potency_ratio=-1.21,
#                  delimit_by_numbers=True,
#                  max_followers=7000,
#                  max_following=5000,
#                  min_followers=700,
#                  min_following=1000)


# # Make comments
# # session.set_do_comment(True, percentage=15)
# # session.set_comments(['Nice shot @{}!', 'Nice!', 'Great Pict @{}!'], media='Photo')
# # # session.set_comments(['Great Video!'], media='Video')


# # # Prevents unfollow followers who have liked one of your latest 5 posts
# # session.set_dont_unfollow_active_users(enabled=True, posts=5)

# # # Unfollow the users WHO do not follow you back:
# # session.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)

# # session.set_dont_include(['friend1', 'friend2', 'friend3'])


# # # Follow people who post the hashtags
# # # default enabled=False, follows ~ 10% of the users from the images, times=1
# # # (only follows a user once (if unfollowed again))

# # session.set_do_follow(enabled=True, percentage=10, times=1)



# # # Follows the followers of each given user
# # # The usernames can be either a list or a string
# # # The amount is for each account, in this case 30 users will be followed
# # # If randomize is false it will pick in a top-down fashion

# # session.follow_user_followers(['philkahnkephotos'], amount=25, randomize=True, sleep_delay=60)

# # # Unfollow users Instapy followed if they do not follow me back after 96 hours

# # session.unfollow_users(amount=10, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=96*60*60, sleep_delay=501)

# # Hashtags not to like (spam)

# session.set_dont_like(['marykay', 'vintagefashion'])

# # do the actual liking 
# session.like_by_tags(['waterfowlphotography', 'duckhunting', 'sitkagear', 'drakewaterfowl', 'wildlifephotographer', 'wildlifephotography'], amount=50)


# # Like posts in my feed

# session.like_by_feed(amount=50, randomize=True, unfollow=False, interact=False)


# # end the bot session
# session.end()


# In[ ]:




