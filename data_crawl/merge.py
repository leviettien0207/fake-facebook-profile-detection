import os
import json

files = os.listdir('out_data')

result = list()
for f1 in files:
    with open('out_data\\' + f1, encoding='utf-8') as fh:
        data = json.load(fh)

    for i in data['list_users']:
        if i["nums_of_friend"] is not None:
            i["nums_of_friend"] = float(i.get("nums_of_friend"))
    result.extend(data['list_users'])

dictionary = {"list_users": result}

json_object = json.dumps(dictionary, indent=4, ensure_ascii=False)

with open("combined.json", "w", encoding='utf-8') as outfile:
    outfile.write(json_object)
