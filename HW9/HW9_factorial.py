# Recursion - factorial calculation

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


i = int(input("Enter your number: "))
for x in range(1, i+1):
    print(f"{x}! = {factorial(x)}")


