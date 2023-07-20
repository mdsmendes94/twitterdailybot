# import package
import os, random, tweepy, time, schedule

def job():                              
    folder=r"F:\mat\twitterbot\pics"    # Set your folder here, twitter allows .jpg, .jpeg, .png, .gif and mp4 videos to be uploaded as media. 
                                        # Current limitations as of 18/07/2022: Images 5MB, gifs 15mb, MP4 512mb(when using media_category=amplify)
    a=random.choice(os.listdir(folder)) # I recommended to have only these files formats in your folder otherwise it might result in an error.
    print(a)

    #os.open(a, os.O_RDWR)              # Do not remove the #
    from PIL import Image               # You might have to 'pip install pillow' on command prompt
    img = folder+'\\'+a
    print(img)
    print("Media successfully picked")
    upload(img)

CONSUMER_KEY = ""
CONSUMER_SEC = ""
AUTH_ACC = ""
AUTH_SEC = ""
BEARER = ""


# 1.1 API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SEC)
auth.set_access_token(AUTH_ACC, AUTH_SEC)
api = tweepy.API(auth, wait_on_rate_limit=True)

# 2.0 API
client = tweepy.Client(BEARER, CONSUMER_KEY, CONSUMER_SEC, AUTH_ACC, AUTH_SEC, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("V1.1 Authentication OK")
except Exception as e:
    print(f"Error during authentication: {e}")

# upload media
def upload(filename):
    status_text = ""                               # Insert your text message here if you will or leave in blank otherwise for no text message.    
    media_info = api.media_upload(filename)
    posted_status_v2 = client.create_tweet(text=status_text, media_ids=[media_info.media_id])    
    print("Uploaded successfully")
    return 0


schedule.every().day.at("13:00").do(job)    # Set the hour of the day the bot will start running check https://schedule.readthedocs.io/en/stable/ for more info.
while True:
    schedule.run_pending()
    time.sleep(1)

##Credit for help 
##STC, Merceal, Asplosions in Offline Chat
##Supe from Tweepy Discord server
