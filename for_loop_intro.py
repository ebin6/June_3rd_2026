'''

for k in range(7,0,-2):
    print(k)

'''

'''
d=list(range(7,51,7))
print(d)
'''
'''
num=int(input("Enter the number : "))
fact=1
for n in range(1,num+1):
    fact=fact*n
print(f"Factorial of {num} is {fact}")
'''

count=int(input("Enter how many number you wish to enter : "))
numbers=[]
for k in range(1,count+1):
    num=int(input(f"{k}.Enter the number : "))
    numbers=numbers+[num]
print(numbers)