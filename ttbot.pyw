# 1. import package
import os, random, tweepy, time, schedule

def job():                              
    folder=r""                          # Set your folder here, in between the quotes. Twitter allows jpg, jpegs, gifs and mp4 videos to be uploaded as media. 
                                        # Current limitations as of 18/07/2022: Images 5MB, gifs 15mb, MP4 512mb(when using media_category=amplify)
    a=random.choice(os.listdir(folder)) # I recommended to have only these files formats in your folder otherwise it might result in an error.
    print(a)

    #os.open(a, os.O_RDWR)              # Do not remove the #
    from PIL import Image               # You might have to 'pip install pillow' on command prompt
    img = folder+'\\'+a
    print(img)
    return(img)
    print("Media successfully picked")


# 2. Store credentials
apiKey = ""                             # Set your 'Consumer Key API Key' in between the quotes;
apikeySecret = ""                       # Set your 'Consumer Key  Secret' in between the quotes;
accessToken = ""                        # Set your 'Authentication Token Access Token' in between the quotes; 
accessTokenSecret = ""                  # Set your 'Authentication Token Secret' in between the quotes.


# 3. Create Oauth client and set authentication and create API object
oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
oauth.set_access_token(accessToken, accessTokenSecret)
print("Authentication successfully")

api = tweepy.API(oauth)


# 4. upload media
text = ""                                       #Insert your text message here if you will or leave in blank otherwise for no text message.
filename = job()
media = api.media_upload(filename)
result = api.update_status(status = text,media_ids = [media.media_id_string])
print("Uploaded successfully")
    
schedule.every().day.at("13:00").do(job)        #Set the hour of the day the bot will start running check https://schedule.readthedocs.io/en/stable/ for more info.
while True:
    schedule.run_pending()
    time.sleep(1)
