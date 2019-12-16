import json

car_dictionary = {
    'Name': 'Tesla',
    'Engine': '90000kW',
    'Type': 'Electric'
}

print(type(car_dictionary))

# json.dumps(dict_object) --> string
    # Use this to create JSON string from our dictionaries on the go
car_data_json_string = json.dumps(car_dictionary)
print(car_data_json_string)

# json.dump(dict_object, file) --> writes json to a file
with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_dictionary, jsonfile)

# json.load(jsonfile) --> outputs dictionary
with open('new_json_file.json', 'r') as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car['Engine'])