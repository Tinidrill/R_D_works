# HW8 - set functions
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {4, 5, 6, 7, 8, 9, 10}

# function duplicate of two sets
def duplicates(s1, s2):
    return set(s1).intersection(s2)

set_dupl = duplicates(set1, set2)
print(f"Duplicates of sets are: {set_dupl}")

# unique elements function
def unique_elements(s1, s2):
    return set(s1).symmetric_difference(s2)

set_unique = unique_elements(set1, set2)
print(f"Duplicates of sets are: {set_unique}")

# return the upper case string
def upper_case(str):
    return str.upper()

lst = input("Entere your text: ")
for item in map(upper_case,lst):
    print(item, end = "")
print()

# option 2 - return the upper case string
#for item in map(lambda str: str.upper(), lst):
#    print(item, end = "")

# Filter all digits
def all_digits(str):
    return str.isdigit()

list = input("Enter your data: ")
for item in filter(all_digits, list):
    print(item, end = "")
