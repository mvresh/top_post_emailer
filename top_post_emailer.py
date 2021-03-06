import os
import praw
import smtplib
from email.mime.text import MIMEText
import argparse

parser = argparse.ArgumentParser(description="Email from any sub you like with a top post")
parser.add_argument("one")
parser.add_argument("two")
parser.add_argument("three")
parser.add_argument("four")


args = parser.parse_args()

to_email = args.one
from_email = args.two
password = args.three
subreddit = args.four

r = praw.Reddit(user_agent='Pytoresh')
submissions = r.get_subreddit(subreddit).get_top(limit=1)

for top in submissions:
    top_link = top.url
    title = top.title


top_link += "\n\n Sends the top post at this time everyday."


msg = MIMEText(top_link)
msg['Subject'] = title
msg['From'] = from_email
msg['Reply-to'] = from_email
msg['To'] = to_email



server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.close()
