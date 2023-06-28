# exceptions lines 14-24, lines 48-53, lines 62-65
#creating address book using dictionary
address_book = {}

import json
import csv
from datetime import datetime

def time():
    print(datetime.now())

# command add
while True:
    choose_command = input("ENTER YOUR COMMAND\nADD - to add a contact\n"
                           "STATS - # of contacts\n"
                           "LIST - all names\n"
                           "DELETE - delete a name\n"
                           "SHOW NAME - to show details of the name\n"
                           "STOP - to stop\n")
    if choose_command.lower() == "add":
        time()
        key = input("Enter the contact name: ")
        counter = 5
        value1 = 0
        while counter:
            try:
                value1 = int(input(f"Enter the contact phone number. Only digits."
                                   f"You have {counter} attempts: "))
                break
            except ValueError:
                print("Only digits. Try again")
            finally:
                counter -=1
            #value2 = input("Enter the contact address: ")
            #value3 = input("Enter a person status: Family, colleague, friend, jerk etc: ")
        if key in address_book:
            print("this name is already in phone book")
        else:
            address_book[key] = value1
# writing an address book into the file with a help of json
        json_book = json.dumps(address_book)
        try:
            with open("json_address_book", "w") as file:
                file.write(json_book)
        except FileNotFoundError:
            with open("json_address_book", "x") as file:
                file.write(json_book)


# command list
    elif choose_command.lower() == "list":
        time()
        print("The address book is: ")
        with open("json_address_book") as file:
            data = file.read()
            json_data = json.loads(data)
            print(json_data)


#        print(address_book)
#        for key, value in address_book.items():
#            print(f"{key} : {value1},\t{value2},\t{value3}")


# command stats
    elif choose_command.lower() == "stats":
        time()
        contact_amounts = len(address_book)
        print(f"Contacts amounts - {contact_amounts} ")

#command delete
    elif choose_command.lower() == "delete":
        time()
        deleted_name = input("What name do you want to delete? ")
        try:
            address_book.pop(deleted_name)
            print("Contact is deleted")
        except KeyError:
            print(f"The name {deleted_name} doesn't exist in your contact list.")
        print("The address book is: ")
        print(address_book)
#        for key1, value in address_book.items():
#            print(f"{key1} : {value1},\t{value2},\t{value3}")

# command show name
    elif choose_command.lower() == "show name":
        time()
        showed_name = input("What name do you want to see? ")
        try:
            print(f"{showed_name} :", address_book[showed_name])
        except KeyError:
            print(f"The name {showed_name} doesn't exist in your contact list.")
            with open("errors", "a") as print_file:
                print(datetime())
                print(f"The name {showed_name} doesn't exist in your contact list.", file = print_file)


# command stop
    elif choose_command.lower() == "stop":
        time()
        break
        print("Exit")
# wrong command
    else:
        time()
        print("Wrong command!")
        print()



