#creating address book using dictionary
address_book = {}

# command add
while True:
    choose_command = input("Enter your command\nadd - to add a contact\nstats - # of contacts\nlist - all names\ndelete - delete a name\nshow name - to show details of the name\nstop - to stop\n")
    if choose_command == "add":
        key = input("Enter the contact name: ")
        value = input("Enter the contact phone number: ")
        value1 = input("Enter the contact address: ")
        value2 = input("Enter a person status: Family, colleague, friend, jerk etc: ")
        if key in address_book:
            print("this name is already in phone book")
        else:
            address_book[key] = value + value1 + value2

# command list
    elif choose_command == "list":
        print("The address book is: ")
        for key, value in address_book.items():
            print(f"{key} : {value},\t{value1},\t{value2}")

# command stats
    elif choose_command == "stats":
        contact_amounts = len(address_book)
        print(f"Contacts amounts - {contact_amounts} ")

#command delete
    elif choose_command == "delete":
        deleted_name = input("What name do you want to delete? ")
        address_book.pop(deleted_name)
        print("The address book is: ")
        for key, value in address_book.items():
            print(f"{key} : {value},\t{value1},\t{value2}")

# command show name
    elif choose_command == "show name":
        showed_name = input("What name do you want to see? ")
        print(f"{showed_name} : {value},\t{value1},\t{value2}")

# command stop
    elif choose_command == "stop":
        break
        print("Exit")
