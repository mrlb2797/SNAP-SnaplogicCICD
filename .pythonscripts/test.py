# Importing re module
import json
import argparse

#Parse script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--sla_filename", type=str)

#Map arguments to variables
args = parser.parse_args()
SnaplogicAccountFileName = args.sla_filename

  
#Reading the SnapLogic Account file
SnaplogicAccountFile = open(SnaplogicAccountFileName, "r")

#Parse the JSON contents to create
#a Python Dictionary object
SnaplogicAccount_PyDict = json.loads(SnaplogicAccountFile.read())
SnaplogicAccountFile.close()

#Replace property_map.settings.password.value 
SnaplogicAccount_PyDict["property_map"]["settings"]["password"]["value"] = "NO       PASSWORD - Removed by GitHub action"

#Convert the Python Dictionary object back to JSON
#and overwrite the original file
SnaplogicAccountFile = open(SnaplogicAccountFileName, "w")
SnaplogicAccountFile.write(json.dumps(SnaplogicAccount_PyDict, indent=4))
SnaplogicAccountFile.close()
  
#open and read the file after the overwriting:
f = open(SnaplogicAccountFileName, "r")
print(f.read())
