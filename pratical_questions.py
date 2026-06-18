"""
    Character count from string 
----------------------------------------
s=input("Enter your string : ")
d={}

for k in s:
    if k in d: 
        d[k]=d[k]+1
    else:
        d[k]=1

for n in d:
    print(f"{n} = {d[n]}")

"""
'''
     List sorting 
-----------------------
count=int(input("How many numbers you wish to enter : "))
numbers=[]
for k in range(1,count+1):
    num=int(input(f"{k}. Enter the number : "))
    numbers=numbers+[num]
n=len(numbers) # To find length of given list --> 5 
for k in range(n-1):# Index position starts from 0 So range is 5 - 1 --> 4
    for v in range(n-k-1):
        if numbers[v]>numbers[v+1]:
            numbers[v],numbers[v+1]=numbers[v+1],numbers[v]
print(numbers)
'''

num=int(input("Enter the number : "))
is_prime = True
if num>1:
    for n in range(2,(num//2)+1):
        if num%n==0:
            print(num,"is not a prime number")
            is_prime=False
            break
    else:
        print(num,"is prime number")    
else:
    print(num,"is not a prime number")


