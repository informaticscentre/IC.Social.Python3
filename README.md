# IC.Social.Python3 - Implementing a Twitter feed in Python
This code based on the original blog post from https://www.informaticscentre.co.uk/blog/implementing-a-twitter-feed-in-python that we published in 2013 and has now been updated to work with Python 3.4.3+ in this version (https://www.informaticscentre.co.uk/blog/updating-the-twitter-feed-for-python-3). If you wish to view the Python 2.7 source code visit the repository - https://github.com/informaticscentre/IC.Social.

## Prerequisites
1. Python 3.4.3+
2. Setup your application with Twitter's Developer API (https://dev.twitter.com/docs/auth/tokens-devtwittercom)
3. pip (if not installed - https://pip.pypa.io/en/latest/installing.html)
4. Pillow - As PIL does not support Python 3 you need to install Pillow through pip. ```pip install pillow```
5. python3-oauth2 (https://github.com/i-kiwamu/python3-oauth2) install with ```python setup.py install```

## How to use
You will need to modify the **start.py** file to include your own Twitter Application details.
```python
consumerKey = ''
consumerSecret = ''
apiKey = ''
apiSecret = ''
```
Change the hash tag ```#informatictips``` in **start.py** to something of your choice.
```python
 tweets = twitterRepository.GetTweetsFromUnblockedUsers('#informaticstips', 20)
```

Start the application from your command line.
```
python start.py
```
