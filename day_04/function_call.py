def mul(a, b):
    c = a * b
    return c
 
def add(a, b):
    c = a + b
    print(c)
    d = mul(a, b)
    print(d)
 
x = 10
y = 20
add(x, y)

def mul1(a, b):
    c = a * b
    return c
 
def add1(x, y):
    c = x + y
    x+=10
    y+=10
    print(c)
    print(x,y)
    d = mul1(x, y)
    print(d)
 
x = 10
y = 20
add1(x, y)
print(x,y)
print(mul(x,y))
