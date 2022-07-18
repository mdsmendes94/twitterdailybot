# 1. import package
import os, random, tweepy, time, schedule

def job():
    folder=r"SET YOUR FOLDER HERE"
    
    a=random.choice(os.listdir(folder))
    print(a)

    #os.open(a, os.O_RDWR)
    from PIL import Image
    img = folder+'\\'+a
    print(img)
    return(img)
    print("Media successfully picked")


# 2. Store credentials
apiKey = "SET YOUR KEY HERE"
apikeySecret = "SET YOUR KEY HERE"
accessToken = "SET YOUR KEY HERE"
accessTokenSecret = "SET YOUR KEY HERE"


# 3. Create Oauth client and set authentication and create API object
oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
oauth.set_access_token(accessToken, accessTokenSecret)
print("Authentication successfully")

api = tweepy.API(oauth)


# 4. upload media and message
text = ""
filename = job()
media = api.media_upload(filename)
result = api.update_status(status = text,media_ids = [media.media_id_string])
print("Uploaded successfully")
    
schedule.every().day.at("").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
