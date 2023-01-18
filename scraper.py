import json
import re
import shutil
import os

#custom class for json objects
class jsonObject:
    def __init__(self, path, hash, size, hashDirectory):
        self.path = path
        self.hash = hash
        self.size = size
        self.hashDirectory = hashDirectory

#open json file and load it into "data"
with open("1.19.json", "r") as f:
    data = json.load(f)

#list of sounds containing json objects
sounds = []

for object in data["objects"]:
    if (re.search("^minecraft/sounds/", object)):
        sounds.append(jsonObject(object, data["objects"][object]["hash"], data["objects"][object]["size"], data["objects"][object]["hash"][0:2]))
    
for jsonObject in sounds:
    print ("path:", jsonObject.path, "hash:", jsonObject.hash, "size:", jsonObject.size, "hash directory:", jsonObject.hashDirectory)


#now to get all those files, move them, and rename them

for jsonObject in sounds:
    startPath = "objects/" + jsonObject.hashDirectory + "/" + jsonObject.hash
    endPath = "sounds/" + jsonObject.path
    os.makedirs(os.path.dirname(endPath), exist_ok=True)
    shutil.copy(startPath, endPath)

