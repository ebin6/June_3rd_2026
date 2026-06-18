'''
count=1

while count<=10:
    print(count,end=" ")
    count+=1
'''

while True:
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
    s=input("Do you wish to continue (yes/no) ? : ")
    if s=="no":
        print("Exiting ...")
        break