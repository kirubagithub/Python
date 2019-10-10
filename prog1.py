# 'Find Max value program using user Input'
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def find_max(a, b):
    if a > b:
        print("{0} is Greater than {1}".format(a, b))
    else:
        print("{0} is Greater than {1}".format(b, a))
    return

print("Calling find_max() function...\n")
find_max(a, b)