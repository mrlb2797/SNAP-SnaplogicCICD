# Importing re module
import json
import argparse
import os

#Parse script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--SL_ProjectFolder", type=str)

#Map arguments to variables
args = parser.parse_args()
SL_ProjectFolderPath = args.SL_ProjectFolder

for SL_ProjectAsset in os.listdir(SL_ProjectFolderPath):
    if SL_ProjectAsset.endswith(".sla"):
        # Prints only text file present in My Folder
        print(SL_ProjectAsset)


  
#Reading the SnapLogic Account file
#SnaplogicAccountFile = open(SnaplogicAccountFileName, "r")

#Parse the JSON contents to create
#a Python Dictionary object
#SnaplogicAccount_PyDict = json.loads(SnaplogicAccountFile.read())
#SnaplogicAccountFile.close()

#Replace property_map.settings.password.value 
#SnaplogicAccount_PyDict["property_map"]["settings"]["password"]["value"] = "NO       PASSWORD - Removed by GitHub action"

#Convert the Python Dictionary object back to JSON
#and overwrite the original file
#SnaplogicAccountFile = open(SnaplogicAccountFileName, "w")
#SnaplogicAccountFile.write(json.dumps(SnaplogicAccount_PyDict, indent=4))
#SnaplogicAccountFile.close()
  
#open and read the file after the overwriting:
#f = open(SnaplogicAccountFileName, "r")
#print(f.read())
