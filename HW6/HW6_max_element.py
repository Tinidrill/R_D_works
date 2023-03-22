#OPTION1
# def max_element(A):
#    max = A[0]
#    for item in A:
#        if item > max:
#            max = item
#    return max
#
#list = [1,2,56,7,3,4,99]
#result = max_element(list)
#print(result)

#OPTION2 max element with a help of reduce() function
def max_element(a):
    from functools import reduce
    max = reduce(lambda a,b: a if (a>b) else b, list)
    return max

list = [1,23,4,56,7,89]
result = max_element(list)
print(result)