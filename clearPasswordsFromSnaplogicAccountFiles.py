# Importing re module
import json
  
#Reading the SnapLogic Account file
SnaplogicAccountFile = open("Test IFS Account.sla", "r")

#Parse the JSON contents to create
#a Python Dictionary object
SnaplogicAccountDictionary = json.loads(SnaplogicAccountFile.read())
  
print(SnaplogicAccountDictionary["property_map"])
