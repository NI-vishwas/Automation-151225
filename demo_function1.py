
m = 100
def func():
    print("Value of m inside func is",m)
    print("Hello World")

def add(a,b):
    global m
    m = 25
    print("Value of m inside add is",m)
    return a+b

func()
print(add(20,30))
print(add(100,25))
print(add(78,90))
func()
k = add(87,90)
print(k**2)
# Step 1: You have a csv or users & emails - Read ( Function)
# Step 2: Generate a template of email with their name (Function)
