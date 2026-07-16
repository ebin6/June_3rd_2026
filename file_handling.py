'''file=open("abc.txt","w")
file.write("This is a sample test file .")
file.close()'''

with open("abc.txt","r") as file:
    print(file.read())


