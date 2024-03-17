# This program will store a simple dict to a file as JSON 
# Author Andre Hoarau
import json 
FILENAME = "pands-mywork\week07-files\labs7.3.2messingwithjson.json"
testdict = {'name' : 'Andre', 
            'age' : '28'}
def writejson(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

writejson(testdict)