#checking and analysing the text symbol by symbol
user_text = input("Input your text: ")
for letters in user_text:
    if letters.isdigit() and int(letters) % 2 == 0:
            print(f"The element '{letters}' is a digit and is an even number.")
    elif letters.isdigit() and int(letters) % 2 != 0:
            print(f"The element '{letters}' is a digit and is an odd number.")
    elif letters.isalpha() and letters.istitle():
        print(f"The element '{letters}' is a letter. It is a title one.")
    elif letters.isalpha() and letters.islower():
        print(f"The element '{letters}' is a letter. It is a small letter.")
    else:
        print(f"The element '{letters}' is a symbol.")


