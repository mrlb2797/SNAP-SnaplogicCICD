# Importing re module
import json
  
#Reading the SnapLogic Account file
SnaplogicAccountFile = open("Test IFS Account.sla", "r")

#Parse the JSON contents to create
#a Python Dictionary object
SnaplogicAccount_PyDict = json.loads(SnaplogicAccountFile.read())
SnaplogicAccountFile.close()

#Replace property_map.settings.password.value 
SnaplogicAccount_PyDict["property_map"]["settings"]["password"]["value"] = "NO       PASSWORD - Removed by GitHub action"

#Convert the Python Dictionary object back to JSON
#and overwrite the original file
SnaplogicAccountFile = open("Test IFS Account.sla", "w")
SnaplogicAccountFile.write(json.dumps(SnaplogicAccount_PyDict, indent=4))
SnaplogicAccountFile.close()
  
print(SnaplogicAccountDictionary["property_map"]["settings"]["password"]["value"])
