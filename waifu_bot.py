from service.twitter_service import TwitterService
from service.get_image_service import get_random_image_url, download_image, remove_image
import schedule
import time

def tweet_waifu():
    t = TwitterService()
    filename = download_image(get_random_image_url())
    medias = []

    media = t.get_media_id(filename)
    medias.append(media)
    t.post_tweet(medias)
    remove_image(filename)

#schedule.every().day.at("01:20").do(tweet_waifu)
schedule.every().hour.at(":59").do(tweet_waifu)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute