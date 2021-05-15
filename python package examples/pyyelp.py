import requests
from requests.models import Response

import config
headers ={
    "Authorization":"Bearer" + config.api_key
    
}
params = {
    "terms":"barber",
    "location":"nyc"
}
response = requests.get("https:/api/yelp",headers= headers,params=params)
businesses = response.json()["businesses"]

for business in businesses:
    print(business['name'])