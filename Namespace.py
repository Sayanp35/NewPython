print("List of object names in __main__ namespace: \n",dir())
import math
print("List of object names in __main__ namespace")
print("After 'import math' has executed:\n",dir())
print("The value of pi is: ",math.pi)
print("The tangent of 1 is: ",math.tan(1))
del math
print()

print("List of object names in __main__ namespace: \n",dir())
import math as fun
print("List of object names in __main__ namespace")
print("After 'import math as fun' has executed:\n",dir())
print("The value of pi is: ",fun.pi)
print("The tangent of 1 is: ",fun.tan(1))
del (fun)
print()

print("List of object names in __main__ namespace: \n",dir())
from math import pi, tan
print("List of object names in __main__ namespace")
print("After 'from math import pi, tan' has executed:\n",dir())
print("The value of pi is: ",pi)
print("The tangent of 1 is: ",tan(1))
del (pi)
del(tan)
print()

print("List of object names in __main__ namespace: \n",dir())
from math import pi as pie, tan as tangent
print("List of object names in __main__ namespace")
print("After 'from math import pi as pie, tan as tangent' has executed:\n",dir())
print("The value of pi is: ",pie)
print("The tangent of 1 is: ",tangent(1))
del (pie)
del(tangent)
print()

print("You want to avoid polluting the __main__ namespace like this: ")
print(dir())
