from facebook_scraper import *
import pandas as pd

@data_loader
def load_data_from_file(*args, **kwargs):
    profile = get_profile('funandstupid', cookies='C:/Users/Magik/Documents/mage/test/data_loaders/cookies.txt')

    profile.keys()


    info = {}

    for key,value in profile.items():
        info[key] = value

    dict = info['top_post']

    profile_df = pd.DataFrame([dict])
    fb_df = profile_df.loc[:, ['username', 'user_id', 'header']]
    return fb_df