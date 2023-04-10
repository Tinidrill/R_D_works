# customer exceptions - age check
while True:
    class AgeCheck(Exception):
        pass
    try:
        min_age = 18
        age = int(input("Enter your age. Only digits:  "))
        diff = min_age - age
        if age < 18:
            raise age_check()
    except age_check:
        print(f"You are too young, little one. Welcome back in {diff} years.")
    except ValueError:
        print("Only digit. Think hard.")
    else:
        print("Welcome to the site")
        break