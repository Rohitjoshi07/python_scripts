import json
import difflib
from difflib import get_close_matches # it import the library functions.

data= json.load(open("076 data.json"))  #it loads the data in a variable and make a list of it.
given_data = input("enter word: ")
kim=(get_close_matches(given_data,data.keys()))
def find_meaning(given_data):            #it creates a function for all the process.
    given_data = given_data.lower()

    if given_data in data:
       return data[given_data]
    elif given_data.upper() in data:
        return data[given_data.upper()]
    elif given_data.title() in data: # this will check the uppercase version of input too in dictionary.
        return data[given_data.title()]

    elif len(kim)>0:
         reply = input("Did you mean %s instead? enter Y for YES or N for NO: " % kim[0] )
         if "Y" in reply:
            return data[kim[0]]

         elif "N" in reply:
            return "This word doesn't exist! "
         else:
            return "sorry we didn't get appropriate response ! "
    else:
        return "This word doesn't exist! "

optimise=find_meaning(given_data)
if type(optimise)==str:
     print(optimise)
else:
     for item in optimise:
         print(item)