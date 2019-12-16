import requests
# Get request
# Do not have a body (JSON)
# They have a base url, path, arguments

base_url = 'http://api.postcodes.io/'
path = 'postcodes/'
arguments = 'e146gt'

request_response = requests.get(base_url + path + arguments)
print(request_response)

# Turning a request to dictionary --> use .json
dict_response = request_response.json()
print(dict_response)
print(dict_response['result']['admin_ward'])