# to replace email with X***@***X

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
    b = re.findall(r"[\w\.]+@[\w\.]+",read_data)
    a = re.sub("[\w\.]+@[\w\.]+","X*****@*****X",read_data) # no clue how to safe the first letters of the emails
    print(b)
    print(a)

