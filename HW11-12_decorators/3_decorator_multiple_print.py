# writing a decorator - printing the name of the function and time of its call

from datetime import datetime

def my_decorator(func):
    print("Let's wrap our function")
    print()

    def wrapper(*args):
        for x in range(times):
            time = datetime.now()
            func(*args)
            print(f"The function name is {func}")
            print(f"The time of function call is {time}")
            print()
    return wrapper

@my_decorator
def main_function(times):
    print("This is main function. It does nothing now. It should be decorated.")

# OPTION1 of making 3rd task
# times = int(input("How many times do you want to print it?"))
# for x in range(times):

# OPTION 2 of making the 3rd task
times = int(input("How many times do you want to print it?"))
main_function(times)

