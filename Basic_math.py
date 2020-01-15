import math

x,y=5.0,10
pi=math.pi
e=math.e
print("the value of pi is:",pi)
print("the rounded value of pi is:",round(pi,4))

pos_inf=float('inf')
neg_inf=float('-inf')
not_a_num=float('nan')

print("math.isinf(pos_inf):",math.isinf(pos_inf))
print("math.isinf(neg_inf):",math.isinf(neg_inf))
print("math.isnan(not_a_num):",math.isnan(not_a_num))

print("pos_inf * x:",pos_inf * x)
print("neg_inf / y:",neg_inf / y)
print("pos_inf + neg_inf:",pos_inf + neg_inf)
print("not_a_num - y:",not_a_num - y)

print("not_a_num == not_a_num:",not_a_num == not_a_num)

print("math.factorial(5):",math.factorial(5))

print("math.log(x):",math.log(x))
print("math.log10(x):",math.log10(x))
print("math.exp(x):",math.exp(x))
print("math.pow(x,x):",math.pow(x,x))
print("math.sqrt(25):",math.sqrt(25))

print("math.cos(x):",math.cos(x))
print("math.acos(0.284):",math.acos(0.284))

print("math.degrees(x):",math.degrees(x))
print("math.radians(286.5):",math.radians(286.5))

print("math.acosh(x):",math.acosh(x))
print("math.asinh(x):",math.asinh(x))
