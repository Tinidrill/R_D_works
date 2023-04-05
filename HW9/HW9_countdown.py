# RECURSION approach - printing figures from entered to 0
import time
def numbers(n):
    if n == -1:
        return
    else:
        print(n)
        time.sleep(1)
        numbers(n - 1)

user_number = int(input("Enter a number: "))
print("Let's start a countdown")
numbers(user_number)
print("BOOM!!!")

# ITERATION approach - printing figures from entered to 0
# user_number = int(input("Enter a number: "))
# for i in range(user_number, -1, -1):
#    print(i)