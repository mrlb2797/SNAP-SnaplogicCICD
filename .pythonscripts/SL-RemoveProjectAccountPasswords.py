# Importing re module
import json
import argparse
import os

#
def Obfuscate_Password(FolderPath, SL_Account_File):

    #Reading the SnapLogic Account file
    SnaplogicAccountFile = open(FolderPath+"/"+SL_Account_File, "r")

    #Parse the JSON contents to create
    #a Python Dictionary object
    SnaplogicAccount_PyDict = json.loads(SnaplogicAccountFile.read())
    SnaplogicAccountFile.close()

    #Check if the 'value' field has already been updated previously
    if SnaplogicAccount_PyDict["property_map"]["settings"]["password"]["value"] == "NO       PASSWORD - Removed by GitHub action":
        return 0
    else:
    
        #Replace property_map.settings.password.value 
        SnaplogicAccount_PyDict["property_map"]["settings"]["password"]["value"] = "NO       PASSWORD - Removed by GitHub action"

        #Convert the Python Dictionary object back to JSON
        #and overwrite the original file
        SnaplogicAccountFile = open(FolderPath+"/"+SL_Account_File, "w")
        SnaplogicAccountFile.write(json.dumps(SnaplogicAccount_PyDict, indent=4))
        SnaplogicAccountFile.close()
        print("Password obsfucated for SL Account:"+SL_Account_File[0:-4])
        return 1

#Parse script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--SL_ProjectFolder", type=str)

#Map arguments to variables
args = parser.parse_args()
SL_ProjectFolderPath = args.SL_ProjectFolder

#Account modified counter
SL_Accounts_Changed = 0

for SL_ProjectAsset in os.listdir(SL_ProjectFolderPath):
    if SL_ProjectAsset.endswith(".sla"):
        # Prints only text file present in My Folder
        increment = Obfuscate_Password(SL_ProjectFolderPath,SL_ProjectAsset)
        # Increment counter
        SL_Accounts_Changed = SL_Accounts_Changed + increment
        
print("Accounts modified: "+str(SL_Accounts_Changed))

#Write the GITHUB_OUTPUT environment variable
with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    print(f'{"AccountsModified"}={SL_Accounts_Changed}', file=fh)
