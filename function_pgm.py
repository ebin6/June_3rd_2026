'''
def greet(name,age,place="Kochi",course=None):
    print(f"Hello {name} you are {age} years old")
   
    print("You are from",place)

greet(name="Aswin",age=24,place='Kottayam')
greet(age=29,name="Joyal")

'''

'''
*args
def add(*args):
    total=0
    for i in args:
        total+=i
    print(total)

add(34,12)
add(9,12,46)
'''

'''
def greet(**kwargs):
    print(f"Hello {kwargs["name"]} you are {kwargs["age"]} years old")

greet(name="Aswin",age=24,place='Kottayam')

'''


'''def add(*args):
    total=0
    for i in args:
        total+=i
    return total

s=add(34,12)
print(s)'''

'''def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)
    
print("Factrorial of 5 is : ",fact(5))'''
'''
def add(a,b):
    return a+b
print(add(34,12))
'''
add=lambda a,b:a+b

print(add(31,5))

is_even = lambda num: num%2==0 
print(is_even(13))