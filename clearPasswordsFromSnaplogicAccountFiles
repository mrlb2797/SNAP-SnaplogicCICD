# Importing re module
import re
  
# Creating a function to
# replace the text
def replacetext(search_text,replace_text):
  
    # Opening the file in read and write mode
    with open('SampleFile.txt','r+') as f:
  
        # Reading the file data and store
        # it in a file variable
        file = f.read()
          
        # Replacing the pattern with the string
        # in the file data
        file = re.sub(search_text, replace_text, file)
  
        # Setting the position to the top
        # of the page to insert data
        f.seek(0)
          
        # Writing replaced data in the file
        f.write(file)
  
        # Truncating the file size
        f.truncate()
  
    # Return "Text replaced" string
    return "Text replaced"
  
# Creating a variable and storing
# the text that we want to search
search_text = "dummy"
  
#Creating a variable and storing
# the text that we want to update
replace_text = "replaced"
  
# Calling the replacetext function
# and printing the returned statement
print(replacetext(search_text,replace_text))
