x=5
y=10
y=0x0A
y=0o12
y=0b1010
print("x= ",x,',',"y= ",y)

print("x==y:",x==y)
print("x!=y:",x!=y)
print("x>=y:",x>=y)
print("x>y:",x>y)
print("x<=y:",x<=y)
print("x<y:",x<y)

print("x+y:",x+y)
print("x-y:",x-y)
print("x*y:",x*y)
print("x/y:",x/y)

print("x//y:",x//y)
print("x%y:",x%y)
print("x**y:",x**y)

print("divmod(x,y):",divmod(x,y))
print("pow(x,y):",pow(x,y))
print("abs(-x):",abs(-x))
print("int(5.2):",int(5.2))
print('int("0xff",16):',int("0xff",16))
print("float(x):",float(x))

print("x=x+y:",end='')
x+=y
print(x)
print("x=x-y:",end='')
x-=y
print(x)
print("x=x*y:",end='')
x*=y
print(x)
print("x=x/y:",end='')
x/=y
print(x)

x,y=4,2
print("x= ",x,",","y= ",y)

print("OR: x|y= ",x|y)
print("XOR: x^y= ",x^y)
print("AND: x&y= ",x&y)
print("LEFT SHIFT: x<<y= ",x<<y)
print("RIGHT SHIFT: x>>y= ",x>>y)
print("INVERSION: ~x= ",~x)
