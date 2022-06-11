# scheduledComicDownloaded.py - Checks on the front page image of a comic website.
# If the comic was updated since the website's last visit, it is downloaded and
# copied onto the desktop to make it easy to find.


import datetime
import requests
import bs4
import os
from twilio.rest import Client


res = requests.get('https://www.savagechickens.com/')
res.raise_for_status()
frontSoup = bs4.BeautifulSoup(res.text, features="html.parser")
soupElem = frontSoup.select("[title]")


dateElem = str(soupElem[7])
lastTime = str(datetime.datetime.now() - datetime.timedelta(1))


comicDate = dateElem[41:51]
lastTime = lastTime[:-16]


if comicDate > lastTime:
   comicElems = frontSoup.select('img')
   latestComic = comicElems[4]
   latestComicText = comicElems[4].get('alt')
   latestComicLink = comicElems[4].get('src')
   print(latestComic.getText())
   res = requests.get(latestComicLink)
   res.raise_for_status()

   fileName = os.path.join(r'C:\Users\juan_jr\Desktop', os.path.basename(latestComicLink))
   imageFile = open(fileName, 'wb')
   for chunk in res.iter_content(100000):
      imageFile.write(chunk)
   imageFile.close()

   accountSID = 'AC076e8901facea8276713211a58129707'
   authToken = '3eb8cd89a72450c18d8a4a11418459d5'
   twilioCli = Client(accountSID, authToken)
   twilioNum = '(910) 665-7494'
   myNum = '(209) 652-7598'
   message = twilioCli.messages.create(body='CHICKEN COMIC READY: ' + latestComicText, from_=twilioNum, to=myNum)
   print('CHICKEN COMIC READY: ' + latestComicText)
