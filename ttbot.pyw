# 1. import package
import os, random, tweepy, time, schedule

def job():                              
    folder=r""                          # Set your folder here, twitter allows jpg, jpegs, gifs, and mp4 videos to be uploaded as media. 
                                        # Current limitations as of 18/07/2022: Images 5MB, gifs 15mb, MP4 512mb(when using media_category=amplify)
    a=random.choice(os.listdir(folder)) # I recommended to have only these files formats in your folder otherwise it might result in an error.
    print(a)

    #os.open(a, os.O_RDWR)              # Do not remove the #
    from PIL import Image               # You might have to 'pip install pillow' on command prompt
    img = folder+'\\'+a
    print(img)
    print("Media successfully picked")
    upload(img)    
    
    
# 2. Store credentials
apiKey = "" # Consumer Keys API Key
apikeySecret = "" # Consumer Keys  Secret
accessToken = "" # Authentication Token Access Token
accessTokenSecret = "" # Authentication Token Secret

# 3. Create Oauth client and set authentication and create API object
oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
oauth.set_access_token(accessToken, accessTokenSecret)
print("Authentication successful")
api = tweepy.API(oauth)


# 4. upload media
def upload(filename):
    text = ""                               # Insert your text message here if you will or leave in blank otherwise for no text message.
    media = api.media_upload(filename)
    result = api.update_status(status = text,media_ids = [media.media_id_string])
    print("Uploaded successfully")
    return 0
    
schedule.every().day.at("13:00").do(job)    # Set the hour of the day the bot will start running check https://schedule.readthedocs.io/en/stable/ for more info.
while True:
    schedule.run_pending()
    time.sleep(1)

##Thanks to STC, Merceal, Asplosions in Offline Chat for the help
