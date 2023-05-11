# to replace email with *@*

import re
import json

data = {'Yana email': 'aaa@fhfh.com',
        'Ana email':'bbb@hjhj.com',
        'John email':'ccc@fff.com',
        'Sam email':'ddd@jhj.com',
        'm email':'eeee@fgfg.com'}
json_book = json.dumps(data)
with open("json_address_book", "w") as file:
    file.write(json_book)

with open("json_address_book") as file:
    read_data = file.read()
    a = re.sub("email","*@*",read_data)
    print(a)