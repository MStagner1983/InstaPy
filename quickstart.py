""" Quickstart script for InstaPy usage """
# imports
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



# login credentials
insta_username = 'mcstagner'
insta_password = 'DuckHunting2019$$**'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)


with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                      delimit_by_numbers=True,
                                       max_followers=7000,
                                        min_followers=700,
                                        min_following=1000)
    
    # session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(['marykay', 'vintagefashion'])
    
    
    # activity
    session.like_by_tags(['waterfowlphotography', 'duckhunting', 'sitkagear', 'drakewaterfowl', 'wildlifephotographer', 'wildlifephotography'], amount=50)

    # Get my followers 
    
    stagner_followers=session.grab_followers(username='mcstagner', amount='full', live_match=True, store_locally=True)
    
    # Get my following

    stagner_following = session.grab_following(username="mcstagner", amount="full", live_match=True, store_locally=True)
    
    # Unfollowers

    all_unfollowers, active_unfollowers = session.pick_unfollowers(username="mcstagner", compare_by="day", compare_track="first", live_match=False, store_locally=True, print_out=True)


Insta=pd.read_csv(r'C:\Users\matth\Dropbox\InstaPy\Insta.csv')
followers=len(stagner_followers)
following=len(stagner_following)
Insta.loc[datetime.datetime.now().strftime('%m-%d-%Y')]=[datetime.datetime.now().strftime('%m-%d-%Y'),followers, following]
Insta.to_csv(r'C:\Users\matth\Dropbox\InstaPy\Insta.csv', index=False)

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