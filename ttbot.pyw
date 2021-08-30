import os, random, tweepy, time, schedule
def job():
    folder=r""

    a=random.choice(os.listdir(folder))
    print(a)

    #os.open(a, os.O_RDWR)
    from PIL import Image
    img = folder+'\\'+a

    # assign the values accordingly
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    #api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    status = ""
    filename = img
    # posting the tweet with media
    api.update_with_media(filename, status)
    print("Done!")

schedule.every().day.at("13:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
