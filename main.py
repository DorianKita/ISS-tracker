import requests
import datetime

MY_LAT= 51.110548
MY_LNG= 17.025558



def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    iss_position = (longitude, latitude)


    if MY_LAT - 5 <= latitude <= MY_LAT +5 and MY_LNG - 5 <= longitude <= MY_LNG +5:
        if now.hour > sunset or now.hour < sunrise:
            return True
    else:
        return False



now = datetime.datetime.now()

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters,)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

is_overhead()