import os

class Config(object):
	BOT_TOKEN = 5239472545:AAHMjdTfoDUHKav_37eC8j_hTFDAnIjTCRg
	APP_ID = 4063950
	API_HASH = 5ebe4b5c0a2af776bf5d2e52d7f5aaa4
	DATABASE_URL = postgres://lhxjftxlfkjgav:d9e5ae235d9cc7791d105e6cdfbde4f376a22561c8cce5faaf74549c71da116b@ec2-52-204-195-41.compute-1.amazonaws.com:5432/d717bqhgquba2a
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(853393439)
	SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "[🔔](https://imageup.me/2no) **FORCE SUBSCRIBE :**\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "[⚙](https://imageup.me/2no) **SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\n● Note: Only Creator Of The Group Can Setup Me.",
        
        "[⚙](https://imageup.me/2no) **COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\n● Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[👨‍💻](https://telegra.ph/Music-06-11-2) **DEVELOPED BY IG- @pankaj_ji_2.o **"
      ]

      START_MSG = "**Hey! [👋](https://i.imgur.com/SmqQApH.jpg) [{}](tg://user?id={})**\n\n● I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\n● Learn More At 👉 /help"
