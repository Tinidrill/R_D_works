# Context manager - if give a "r" to open() the mistake will be shown
file = open("text.txt", "w")
print("===========")

try:
    file.write("My first context manager")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()


with open("text.txt", "r") as some_file:
    print(some_file.read())
    print("===========")

# OPTION 2 - didn't really get how it supposed to work
# class MyManager:
#     def __enter__(self):
#         print("==========")
#         return 1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
# #        if exc_type == ValueError:
# #            print(f"{exc_val}: error was found")
#         print("Exit")
#
#
#
# with MyManager() as my_manager:
#     raise ValueError("Error is found")
#     print(my_manager)
#     print("Something inside my context manager")
#
# print("==========")