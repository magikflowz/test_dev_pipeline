import pandas as pd
import praw

from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
   
    # Praw instance with authentication details
    reddit=praw.Reddit(
    client_id="r2jXLWXnq3fBlbOSH7tJ0A",
    client_secret="BINI2gYBIkx826x7i3ZxzeAIKzxAqQ",
    user_agent="my-app by u/idunno69694200",
    username="u/idunno69694200",
    password=""
    )

    # Define the Subreddit and append the atrribuates of posts to DataFrame
    subreddit= reddit.subreddit("ChatGPT")
    reddit_df = pd.DataFrame([ vars(post) for post in subreddit.new(limit=8) ])

    return reddit_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'