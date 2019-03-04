import praw
import config
import time

def bot_login():
    print("Loggin in.....")
    r=praw.Reddit(username=config.username,
                password=config.password,
                client_id=config.client_id,
                client_secret=config.client_secret,
                user_agent="ParityPyhtonBot v0.1")
                print("Logged in")
    return r

def run_bot(r):
    for comment in r.subreddit('test').comments(limit=25):
        if "test" in comment.body:
            print("String with \"test\" Found") + comment.id
            comment.reply("I can confirm this statement to the best of my knowledge")
    print("Sleeping for a 30 seconds")
    time.sleep(30)                
while True:
    r = bot_login()
    run_bot(r)
