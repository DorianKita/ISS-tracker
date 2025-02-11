import requests
import datetime

# url = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url=url)
# response.raise_for_status()
#
# data = response.json()
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

now = datetime.datetime.now()

parameters = {
    'lat': 51.110548,
    'lng': 17.025558,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters,)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
