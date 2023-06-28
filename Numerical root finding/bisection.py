def f(x):
    return x - 3

def root(a,b):
    c = float ((a + b) / 2)
    condition=True
    while condition:
        if f(a) < 0 and f(b) > 0:
            if f(c) > 0:
                b = c 
            else:
                a = c  
        if f(a) > 0 and f(b) < 0:
            if f(c) > 0:
                a = c  
            else:
                b = c  
        condition = abs(a - b) <= 0.001
    print("The root is", c)

a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))

if f(a) == 0:
    print("The value", a, "is itself a root.")
if f(b) == 0:
    print("The value", b, "is itself a root.")
if f(a) * f(b) > 0:
    print("The value is wrong type again")
else:
    root(a,b)
