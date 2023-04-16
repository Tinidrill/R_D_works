# writing a decorator - printing the name of the function and time of its call

from datetime import datetime

def my_decorator(func):
    print("Let's wrap our function")
    def wrapper():
        time = datetime.now()
        func()
        print(f"The function name is {func}")
        print(f"The time of function call is {time}")
    return wrapper

@my_decorator
def main_function():
    print("This is main function. It does nothing now. It should be decorated.")

main_function()


