#!/usr/bin/env python3

from mastodon import Mastodon
from datetime import datetime
import configparser, os

# ordinal helper function
def makeOrdinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

# read config
config = configparser.ConfigParser()
config.read('config.ini')

# set up some variables
dateNumber = datetime.today().strftime('%d')
weekdayName = datetime.today().strftime('%A')
weekdayNumber = datetime.today().strftime('%w')

# initialize pytooter
mastodon = Mastodon(access_token = 'pytooter_usercred.secret')

# generate post
postText = "Today is " + weekdayName + " the " + makeOrdinal(int(dateNumber)) + "."
imageDescription = 'A screenshot from The Simpsons of a rapper wearing a large necklace that says "' + weekdayName + " the " + makeOrdinal(int(dateNumber)) + '".'
imageFilename = os.path.join("images", weekdayNumber, dateNumber+".jpg")

if config['Bot'].getboolean('DryRun'):
  print(postText)
  print(imageDescription)
  print(imageFilename)
else:
  image = mastodon.media_post(media_file = imageFilename, description = imageDescription) # upload image
  mastodon.status_post(status = postText, visibility = "unlisted", media_ids = image) # do the posting
