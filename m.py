import simplejson as sj
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = sj.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "nick", "age": 27}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(sj.dumps(data))
