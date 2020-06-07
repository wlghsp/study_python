import json

with open('student_file.json') as json_file:
    json_data = json.load(json_file)

print(json_data)

