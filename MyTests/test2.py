import json, datetime
try:
    with open('json_data.json') as json_file:
        data = json.load(json_file)
        print(data)
except FileNotFoundError:
    print("Nie ma pliku")
    exit()

data["data"].append(data["data"][0])

with open('json_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

today = datetime.date.today()
print("Today's date:", today)