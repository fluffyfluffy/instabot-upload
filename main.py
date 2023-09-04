from instabot import Bot
import glob
import os
import time as t


cookie_del = glob.glob("config/*cookie.json")
if cookie_del : os.remove(cookie_del[0])

bot = Bot()
bot.login(username="uname", password="pass")

captionconf = open("caption.txt", "r")

#change photo according to filename
photo = "testpic.jpg"

caption = captionconf.read()

#change repeat based on how much you wanna spam
repeat = 10
for i in range(repeat):
    bot.upload_photo(photo, caption=caption)
    #set delay in seconds
    t.sleep(10)

captionconf.close()
