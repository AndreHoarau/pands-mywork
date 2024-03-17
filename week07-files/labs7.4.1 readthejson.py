# This program will read in the json that we have created
# Author Andre Hoarau
import json 
FILENAME = "pands-mywork\week07-files\labs7.3.2messingwithjson.json"
def readthejson():
    with open (FILENAME) as f:
        return json.load(f)

jsonread= readthejson()
print(jsonread)