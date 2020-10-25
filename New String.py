List1 = []
print("Blank List: ", List1)

List2 = [10, 20, 14]
print("\nList of numbers: ", List2)

List3 = ["Hey !", "How are", "You ?"]
print("\nList Items: ", List3[0], List3[2])

List4 = [['Hey !', 'How are'], ['You ?']]
print("\nMulti-Dimensional List: ", List4)

# Duplicate List

List5 = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print('\nList with the use of Duplicate Numbers: ', List5)

List6 = [1, 2, 'Hey', 4, 'How are', 6, 'You!!!']
print("\nList with the use of Mixed Values: ", List6)

List7 = []
print("Length of List :", len(List7))

List8 = [10, 20, 14]
print("Length of List :", len(List8))

# Appending in List

List9 = []
print("Initial blank List: ", List9)

List9.append(1)
List9.append(2)
List9.append(4)
print("\nList after Addition of Three elements: ", List9)

for i in range(1, 4):
    List9.append(i)
print("\nList after Addition of elements from 1-3: ", List9)

List9.append((5, 6))
print("\nList after Addition of a Tuple: ", List9)

List10 = ['Hey !', 'You !']
List9.append(List10)
print("\nList after Addition of a List: ", List9)
print("\n")
# Inserting element in a List

List11 = [1, 2, 3, 4]
print("Initial List: ", List11)

# Addition of Element at
# specific Position
# (using Insert Method)
List11.insert(3, 12)
List11.insert(0, "Hey You !")
print("\nList after performing Insert Operation: ", List11)
print("\n")

# Extending element in a List

List12 = [1, 2, 3, 4]
print("Initial List: ", List12)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List12.extend([8, 'Hey!!', 'You !!'])
print("\nList after performing Extend Operation: ", List12)
print("\n")

List13 = ["Hey ", "How are ", "You !!"]

print("Accessing a element from the list")
print(List13[0])
print(List13[2])

List14 = [['Hey ', 'How are '], ['You !!']]

# accessing an element from the
# Multi-Dimensional List using
# index number
print("Acessing a element from a Multi-Dimensional list")
print(List14[0][1])
print(List14[1][0])

# Negative Indexing

List15 = [1, 2, 'Hey ', 4, 'How are ', 6, 'You !!']

# accessing a element using
# negative indexing
print("Accessing element using negative indexing: ", List15[-3])

print("Accessing element using negative indexing: ", List15[-1])
print("\n")

# Removing Elements from the List

List16 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Intial List: ", List16)

# Removing elements from List
# using Remove() method
List16.remove(5)
List16.remove(6)
print("\nList after Removal of two elements: ", List16)

# Removing elements from List
# using iterator method
for i in range(1, 5):
    List16.remove(i)
print("\nList after Removing a range of elements: ", List16)
print("\n")

List17 = [1, 2, 3, 4, 5]

List17.pop()
print("\nList after popping an element: ", List17)

# Removing element at a
# specific location from the
# Set using the pop() method
List17.pop(2)
print("\nList after popping a specific element: ", List17)
print("\n")

# Slicing a List

List18 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
print("Intial List: ", List18)

# Print elements of a range
# using Slice operation
Sliced_List = List18[3:8]
print("\nSlicing elements in a range 3-8: ", Sliced_List)

# Print elements from a
# pre-defined point to end
Sliced_List = List18[5:]
print("\nElements sliced from 5th " "element till the end: ", Sliced_List)

# Printing elements from
# beginning till end
Sliced_List = List18[:]
print("\nPrinting all elements using slice operation: ", List18)
print("\n")

# Negative index List slicing

List19 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
print("Initial List: ", List19)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List = List19[:-6]
print("\nElements sliced till 6th element from last: ", Sliced_List)

# Print elements of a range
# using negative index List slicing
Sliced_List = List19[-6:-1]
print("\nElements sliced from index -6 to -1: ", Sliced_List)

# Printing elements in reverse
# using Slice operation
Sliced_List = List19[::-1]
print("\nPrinting List in reverse: ", Sliced_List)
