import datetime
import requests
import bs4
from twilio.rest import Client

# changed to send a text no matter what the weather is

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.9537&lon=-121.2905#.XLvkSOhKguU')
res.raise_for_status()
weatherSoup = bs4.BeautifulSoup(res.text, features='html.parser')
weather = weatherSoup.select('.short-desc')
tonight = weather[1].getText()


accountSID = 'AC076e8901facea8276713211a58129707'
authToken = '3eb8cd89a72450c18d8a4a11418459d5'
twilioCli = Client(accountSID, authToken)
twilioNum = '(209) 222-2705'
myNum = '(209) 652-7598'
message = twilioCli.messages.create(body='YOUR OVERLORD ROMAN PREDICTS THE WEATHER: ' + tonight.upper(), from_=twilioNum, to=myNum)
