class A:
    def greet(self):
        print("Hello from class A")

class B(A):
    def greet(self):
        print("Hello from class B")
    
class C(A):
    def greet(self):
        print("Hello from class C")

ob=B()
ob.greet()

obc=C()
obc.greet()