# recording numbers to the file
import re
import json
#
data = {'Yana': '+38067555112233','Ana':'+380451112233','John':'3861112233','Sam':'380971112233444444 ','m':'0651112223'}
json_book = json.dumps(data)
with open("json_phone_book", "w") as file:
    file.write(json_book)

with open("json_phone_book") as file:
    read_data = file.read()
    print("Valid mobile numbers are:")
    print(re.findall(r"\+?3?8?0\d{9}\W",read_data))
    #print(re.findall(r"\+?3?8?0\d{9}[;, ]",read_data)) - this one works on regex101 but doesn't wok here