#Z3NCW1R7B1CYNSX119A82SQC
import requests
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 51.507351
MY_LONG = -0.127758
API_KEY = "92567f1ccd68f9b1d3f66a54cdca4d52"
account_sid = "AC5376e7ad6e6d3405356bf084fa3d86e3"
auth_token = "ebf2f9a0e02faef418887a6c077c2d41"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}
response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data['list'][0]['weather'][0]['id'])
will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) > 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "It's going to rain today. Remember to bring an ☂️",
        from_ = "+17624223997",
        to = "+918383077299"
    )
    print(message.status)