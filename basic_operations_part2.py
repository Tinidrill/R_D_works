# number or text check
checked_text=input("Input any combinations of symbols: ")
if checked_text.isalpha():
    print(f"You have entered only letters. The length of entered combination is {len(checked_text)}.\n")
elif checked_text.isdigit() and int(checked_text) % 2 == 0:
    print("You have entered an even number.\n")
elif checked_text.isdigit() and int(checked_text) % 2 != 0:
    print("You have entered an odd number.\n")
else:
    print("You have entered a crazy combination of letters, numbers and/or spaces.\n")


#defining the type of the entered data - not completed due to lack of knowledge
match checked_text:
    case str():
        print(f"The type of entered data is {type(checked_text)}.")
    case int():
        print(f"The type of entered data is {type(checked_text)}.")

#The type of entered data is always returning string as 'input' functions gives us only string type.





