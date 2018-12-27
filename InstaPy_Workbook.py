#!/usr/bin/env python
# coding: utf-8

# In[1]:


from instapy import InstaPy
from instapy.util import smart_run


# In[2]:


# date_today = datetime.today().strftime('%m-%d-%Y')

# instagram=pd.read_csv('instagram.csv')
# instagram.loc[:, ~instagram.columns.str.contains('^Unnamed')]

# url = 'https://www.instagram.com/mcstagner'
# r = requests.get(url)
# soup = BeautifulSoup(r.content)
# follower = soup.find('meta', {'name': 'description'})['content']
# count = follower.split('Followers')[0]
# #today_info=[date, insta_name, follower_count]
# d={
#    'date': [date_today],
#    'insta_name': ['mcstagner'],
#    'follower_count': [count]
# }
# today_info_df=pd.DataFrame(data=d)
# instagram=pd.concat([today_info_df, instagram])


# instagram['yesterday']=instagram.groupby(['insta_name'])['follower_count'].shift(-1)
# instagram['daily_growth']=instagram['follower_count']-instagram['yesterday']

# instagram.to_csv('instagram.csv', index=False)


# In[ ]:


insta_username = 'mcstagner'
insta_password = 'DuckHunting2019$$**'

# Login
session = InstaPy(username=insta_username, password=insta_password)
session.login()


# # Find non followers
# mcstagner_nonfollowers = session.pick_nonfollowers(username="mcstagner", live_match=True, store_locally=True)


# set up all the settings
session.set_relationship_bounds(enabled=False,
                 potency_ratio=-1.21,
                 delimit_by_numbers=True,
                 max_followers=7000,
                 max_following=5000,
                 min_followers=700,
                 min_following=1000)


# Make comments
# session.set_do_comment(True, percentage=15)
# session.set_comments(['Nice shot @{}!', 'Nice!', 'Great Pict @{}!'], media='Photo')
# # session.set_comments(['Great Video!'], media='Video')


# # Prevents unfollow followers who have liked one of your latest 5 posts
# session.set_dont_unfollow_active_users(enabled=True, posts=5)

# # Unfollow the users WHO do not follow you back:
# session.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)

# session.set_dont_include(['friend1', 'friend2', 'friend3'])


# # Follow people who post the hashtags
# # default enabled=False, follows ~ 10% of the users from the images, times=1
# # (only follows a user once (if unfollowed again))

# session.set_do_follow(enabled=True, percentage=10, times=1)



# # Follows the followers of each given user
# # The usernames can be either a list or a string
# # The amount is for each account, in this case 30 users will be followed
# # If randomize is false it will pick in a top-down fashion

# session.follow_user_followers(['philkahnkephotos'], amount=25, randomize=True, sleep_delay=60)

# # Unfollow users Instapy followed if they do not follow me back after 96 hours

# session.unfollow_users(amount=10, InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=96*60*60, sleep_delay=501)

# Hashtags not to like (spam)

session.set_dont_like(['marykay', 'vintagefashion'])

# do the actual liking 
session.like_by_tags(['waterfowlphotography', 'duckhunting', 'sitkagear', 'drakewaterfowl', 'wildlifephotographer', 'wildlifephotography'], amount=50)


# Like posts in my feed

session.like_by_feed(amount=50, randomize=True, unfollow=False, interact=False)


# end the bot session
session.end()


# In[ ]:




