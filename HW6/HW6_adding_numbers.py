#OPTION1  adding unlimited amount of numbers function
#def sum_function(list):
#    result = sum(list)
#    return result
#
#result = sum_function(1,2,3,4,5,6,7,8,9)
#print (f"Result is {result}")

#OPTION 2  adding unlimited amount of numbers with user input - NOT working :(
#def sum_function(*args):
#   result = sum(args)
#   return result

#list = []
#while True:
#    number = float(input("Enter your number for adding. If you want to stop enter blank:"))
#    list.append(number)
#    if number == " ":
#        break

#sum = sum_function(list)
#print(sum)

#OPTION 3  adding numbers using *args
def sum_f(*args):
    for arg in args:
        result = sum(args)
    return result

list = [1,2,3,4,5,6,7,10]
result = sum_f(*list)
print(f"The sum is: {result}")