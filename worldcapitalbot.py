# worldcapitalbot

import praw
import config

# reddit API login details
reddit = praw.Reddit(client_id = config.client_id,
                     client_secret = config.client_secret,
                     username = config.username,
                     password = config.password,
                     user_agent = config.user_agent)

# subreddit that the bot operates on
subreddit = reddit.subreddit('test')

# phrase that activates the bot
keyphrase = '!worldcapital '

# dictionary of countries and their capital cities
world_capitals = {"Afganistan": "Kabul", "Albania": "Tirana",
                  "Algeria": "Algiers", "Andorra": "Andorra la Vella",
                  "Angola": "Luanda", "Antigua and Barbuda": "Saint John’s",
                  "Argentina": "Buenos Aires", "Armenia": "Yerevan",
                  "Australia": "Canberra", "Austria": "Vienna",
                  "Azerbaijan": "Baku", "Bahamas": "Nassau",
                  "Bahrain": "Manama", "Bangladesh": "Dhaka",
                  "Barbados": "Bridgetown", "Belarus": "Minsk",
                  }

# read country name from comment and search dictionary
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        if word in world_capitals:
            reply = 'Capital city: ' + world_capitals[word]
            comment.reply(reply)
        else:
            reply = 'No result found.'
            comment.reply(reply)
