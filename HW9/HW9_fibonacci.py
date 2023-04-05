def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


user_number = int(input("Enter you number: "))
for x in range(user_number):
    print(fibonacci(x))