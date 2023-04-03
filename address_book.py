# creating address book using dictionary
address_book = {}
# entering keys and values
# asking user input in a loop
while True:
    key = input("Enter the contact name: ")
    value = input("Enter the contact phone number: ")
    value1 = input("Enter the contact address: ")
    value2 = input("Enter a person status: Family, colleague, friend, jerk etc: ")
    address_book[key] = value + value1 + value2
    command = input("Would you like to enter another contact?\n\tTo continue - Yes \n\tTo stop - No\n")
    if command == "Yes":
        continue
    if command == "No":
        break
        print("Exit")
    if command != "Yes" or command != "No":
        print(f"Invalid command: {command}")
        print("Only 'Yes' and 'No' commands are implemented.")

# printing the address book
print("The address book is: ")
for key, value in address_book.items():
    print(f"{key} : {value},\t{value1},\t{value2}")
contact_amounts = len(address_book)
print(f"Amount of contacts: {contact_amounts}")

