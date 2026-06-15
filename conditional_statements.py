"""
if condition:
    statements


"""
'''
age=int(input("Enter your age : "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

'''
'''
num=int(input("Enter the number : "))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")

'''

'''
a=int(input("Enter the fist number : "))
b=int(input("Enter the second number : "))
print("1.Addition\n2.Substract\n3.Divide\n4.Multiply")
choice=int(input("Enter your choice (1,2,3,4) : "))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a/b)
elif choice==4:
    print(a*b)
else:
    print("Invalid input")
'''

a=int(input("Enter the fist number : "))
b=int(input("Enter the second number : "))
print("1.Addition\n2.Substract\n3.Divide\n4.Multiply")
choice=int(input("Enter your choice (1,2,3,4) : "))
match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a/b)
    case 4:
        print(a*b)
    case __:
        print("Invalid input")