"""
def my_dec(fun):
    def wrapper():
       print("Hello from my dec")
       fun()
    return wrapper
@my_dec
def greet():
    print("Hello from greet")

greet()
"""

def my_dec(fun):
    def wrapper(a,b):
        if a>b:
            fun(a,b)
        else:
            print("a must be greater than be b")
    return wrapper

@my_dec
def divide(a,b):
    print(a/b)
    
divide(14,7)


