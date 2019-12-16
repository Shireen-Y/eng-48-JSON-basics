import requests
import json

# Making POST requests
# We need a path and a JSON object to send
# Possibly headers, depending on the api

dictionary_post_codes = {
    'postcodes': ['EC2Y 5AS', 'E14 6GT', 'CT1 2EH']
}
json_body = json.dumps(dictionary_post_codes)

# The url
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

# The headers
headers = {'Content-type': 'application/json'}

# Making the requests
postcodes_post_response = requests.post(base_url + path, data=json_body, headers = headers)
print(postcodes_post_response.json())
results = postcodes_post_response.json()['result']

for request in results:
    print(request['result']['nhs_ha'])