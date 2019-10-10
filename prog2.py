# 'Find Max value program using user Input'
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter Third number: "))

def find_max_of_three(a, b, c):
    if (a > b and a > c):
        print("{0} is Greater than {1} and {2}".format(a, b, c))
    elif (b > a and b > c):
        print("{0} is Greater than {1} and {2}".format(b, a, c))
    else:
        print("{0} is Greater than {1} and {2}".format(c, a, b))

print("Calling find_max_of_three() function...\n")
find_max_of_three(a, b, c)