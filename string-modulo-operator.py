print("Number : % 2d , Portal : % 5.2f" %(1, 05.333))
print("Total students : % 3d , Boys : % 3d" %(240, 120))

# print octal value
print("% 8.2o"% (20))

# print exponential value
print("% 10E"% (356.08977))



# using format() method
print('I love {} for "{}!"'.format('alphabet', 'reading'))

# using format() method and refering
# a position of the object
print('{0} and {1}'.format('alphabet', 'Portal'))

print('{1} and {0}'.format('alphabet', 'Portal'))


print('Number one portal is {0}, {1}, and {other}.'.format('Geeks', 'For', other ='Geeks'))

# using format() method with number
print("Geeks :{0:2d}, Portal :{1:8.2f}".format(120, 00.546))

# Changing positional argument
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))
print("Geeks: {a:5d},  Portal: {p:8.2f}".format(a = 453, p = 59.058))




# used in dictionary

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; Geeks: {0[geek]:d}'.format(tab))

data = dict(fun ="GeeksForGeeks", adj ="Portal")

# using format() in dictionary
print("I love {fun} computer {adj}".format(**data))

data = dict(fun1 ="Alphabet", adj1 ="Portal")
print("I love {fun1} computer {adj1}".format(**data))



cstr = "I love geeksforgeeks"

# Printing the center aligned
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '-'))

# Printing the left aligned
# string with "-" padding
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print ("The right aligned string is : "  )
print (cstr.rjust(40, '-'))
