""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run



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



