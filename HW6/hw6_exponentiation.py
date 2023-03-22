#exponentiation function
def exponentiation(a,b):
    result = a ** b
    return result

#calling the function in infinite loop
print("This is an exponentiation calculation program")
while True:
    number = float(input("Enter a number: "))
    degree = int(input("Enter an exponent: "))
    result = exponentiation(number,degree)
    print(f'{number} ** {degree} = {result}\n')

    command = input("Let's continue?\n\tTo continue - Yes \n\tTo stop - No\n")
    if command == "Yes":
        continue
    if command == "No":
        break
        print("Exit")
    if command != "Yes" or command != "No":
        print(f"Invalid command: {command}")
        print("Only 'Yes' and 'No' commands are implemented.")

