# Matt Griffiths www.twitter.com/mwgriffiths88
# Informatics Centre www.informaticscentre.co.uk
# MIT License

# This script will pull a feed from Twitter from the users unblocked users.
# Blocking a user in Twitter will not pull their tweets.

from feedrenderer import *
from twitterrepository import *

# You must register your own application and fill in the following fields.
# https://dev.twitter.com/docs/auth/tokens-devtwittercom
consumerKey = ''
consumerSecret = ''
apiKey = ''
apiSecret = ''


renderer = FeedRenderer(4, 4)

twitterRepository = TwitterRepository(consumerKey, consumerSecret, apiKey, apiSecret)

def Draw():
    tweets = twitterRepository.GetTweetsFromUnblockedUsers('#informaticstips', 20)
    renderer.DrawFeed(tweets)
    renderer.root.after(61, Draw)

Draw()
renderer.Draw()
