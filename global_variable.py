y=25
x=10

def func1():
    y=10
    print(y)
    global x
    x=5
    x=2
def func2():
    print(y)
    print(x)