'''This scrip gives you all the keys for the Twitter-API
Look in the text below to costume it with your app. Or only run it to get all
keys for the socialpy gateway.
This app-token are from my test app. I'm not shore if it's a god idea to let
them now you. But so you can easily run this scrip and have all the keys you
need for my gateway.
'''
from tweepy import OAuthHandler, API, TweepError
import webbrowser

# Go to https://dev.twitter.com and sign up for a developer account. Then create
# an app. This app shouldn’t have a callback url. Look in your app for the
# tokens and use them for the OAuthHandler
consumer_token = 'kYdbvAGXIhWGHyNKdNTssfpzE'
consumer_secret = 'MM2EVucINNxfFEB0akTenqConUnucj9FaS4hMX1F7wEw5WDvD1'
auth = OAuthHandler(consumer_token, consumer_secret)

# This will open your web browser and ask you to verify for the app. If you
# agree, they show you a pin. If your app has a callback url, they would
# redirect you to this url and didn't show you the pin.
try:
    redirect_url = webbrowser.open(auth.get_authorization_url())
except TweepError:
    print('Error! Failed to get request token.')
    exit()

pin = input('Verification pin number from twitter.com: ').strip()
token = auth.get_access_token(verifier=pin)

print('All the token:')
print('ckey:', consumer_token)
print('csecret:', consumer_secret)
print('akey:', auth.access_token)
print('asecret:', auth.access_token_secret)
