class Record(object):
    pass

def function_block():
    print("function_block prints the line")
    return None

if function_block():
    print(end="\n")
    print("function_block returned a 'True' value")
else:
    print(end="\n")
    print("function_block returned a 'False' value")

for count in range (0,5):
    print(count,end=" ")
else:
    print("At end of the for loop, count= ",count)
print()

while count>0 :
    print(count, end=" ")
    count=count-1
else:
    print("At the end of the while loop, count= ", count)
