
import os
import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

API_ID ="7264251d318caad78e5906469d749b54"
Account_SID ="ACef222dfb0ee7054424c94bc4750261ce"
Auth_token="dfa0e606820b31ce09374a4e070f9256"
parameter ={
    "lat":"19.0760",

    "lon": "72.8777",
    "appid":API_ID,
    "exclude":"current,minutely,daily"
}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall",params=parameter)

response.raise_for_status()
data =response.json()
weather_slice= data["hourly"][:12]
print(weather_slice)
# weather=data["hourly"][0]["weather"][0]["id"]
will_rain=False
for i in weather_slice:
    code =i["weather"][0]["id"]
    if int(code) <700:
        will_rain=True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(Account_SID, Auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_='+18722053628',
        to='+919372328198'
    )
    print(message.status)